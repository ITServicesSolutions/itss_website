from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.conf import settings
from django.utils.html import strip_tags
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import validate_email
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect
from django.views import View

from .serializers import SendNotificationSerializer, RegisterUserSerializer
from .decorators import *
from .forms import *
from .models import *
from customer.models import *
from accounts.models import *
from service.models import *
import random
import uuid, logging, base64


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError as DRFValidationError



def profil(request):
    logos = Logo.objects.filter(is_active=True)
    carousels = Carousel.objects.filter(is_active=True)
    typeservice = TypeService.objects.filter(is_public=True, name__icontains="service")
    principals_services = Service.objects.filter(type__in=typeservice, is_public=True, is_principal=True)
    formations = Formation.objects.filter(is_public=True, is_principal=True)
    services = Service.objects.filter(type__in=typeservice, is_public=True)
    comments = Comments.objects.filter(is_public=True)
    partners = Partner.objects.filter(is_public=True)
    context = {
        'carousels': carousels,
        'logos': logos,
        'principals_services': principals_services,
        'formations': formations,
        'services': services,
        'comments': comments,
        'partners': partners,
    }
    return render(request, 'accounts/profil.html', context)



def login(request):
    logos = Logo.objects.filter(is_active=True)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_auth(request, user)
            return redirect('profil')
        else:
            return render(request, 'accounts/login.html', {'error_message': "Nom d'utilisateur ou mot de passe incorrect.", 'logos': logos})
    else:
        context = {'logos': logos}
        return render(request, 'accounts/login.html', context)

logger = logging.getLogger(__name__)

class RegisterUserView(CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            self.perform_create(serializer)
            #return Response({'success': True})
            return redirect('afterregister')
        else:
            return render(request, 'accounts/register.html', {'form': serializer})

    
    def perform_create(self, serializer):
        user = serializer.save()
        self.send_registration_email(user)
        ftoken = str(uuid.uuid4())
        Profile.objects.create(user=user, forget_token=ftoken)

    def send_registration_email(self, user):
        subject = 'Bienvenue chez ITServices & Solutions'
        html_message = render_to_string('accounts/registration.html', {'user': user})
        plain_message = strip_tags(html_message)
        from_email = 'gnancadjagillesdereck@gmail.com'
        to_email = [user.email] 
        

        send_mail(subject, plain_message, from_email, to_email, html_message=html_message)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return redirect('afterregister')


def afterregister(request):
    return render(request, 'accounts/afterregistration.html', status=200)

def passwordconfirm(request):
    return render(request, 'accounts/passwordconfirm.html', status=200)
    
def page_register(request):
	return render(request, 'accounts/register.html')
    
# Social connexion
def signup_redirect(request):
    messages.error(request, "Oups! Quelque chose s'est mal passé !")
    return redirect('login')

def logout(request):
    logout_auth(request)
    return redirect('home')


# def request_password(request):
    
#     lower = "abcdefghijklmnopqrstuvwxyz"
#     upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     numbers = "0123456789"
#     symbols = "!@#$%^&*()."
#     string = lower + upper + numbers + symbols
#     length = 10

#     generate_password = "".join(random.sample(string,length))
    
#     return render(request, 'accounts/request_password.html')


class RequestPasswordResetEmail(View):
    def get(self, request):
        return render(request, 'accounts/request_password.html')

    def post(self, request):
        email = request.POST.get('email')
        if email:
            try:
                validate_email(email)
            except DjangoValidationError:
                messages.error(request, 'Veuillez entrer un email valide.')
                return render(request, 'accounts/request_password.html')

            user = get_user_model().objects.filter(email=email).first()
            if user:
                uri = urlsafe_base64_encode(force_bytes(user.pk))

                token = default_token_generator.make_token(user)
                
                
                reset_url = request.build_absolute_uri(reverse('reset_user_password', kwargs={'uidb64': uri, 'token': token}))

                email_subject = 'Mot de passe oublié'
                email_message = f"Bonjour, \nVeuillez cliquer sur le lien suivant pour changer votre mot de passe \n{reset_url}"
                from_email = settings.EMAIL_HOST_USER

                try:
                    email = EmailMessage(email_subject, email_message, from_email, [email])
                    email.send(fail_silently=False)
                    messages.success(request, 'Un mail vous a été envoyé.')
                except BadHeaderError:
                    messages.error(request, 'Erreur lors de l\'envoi de l\'e-mail.')
                    return render(request, 'accounts/request_password.html')

                return redirect('passwordconfirm')
            else:
                messages.error(request, "Aucun utilisateur n'est associé à cet email.")
        else:
            messages.error(request, 'Veuillez entrer votre email.')

        return render(request, 'accounts/request_password.html')


from django.contrib.auth import update_session_auth_hash

def reset_password_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            if request.method == 'POST':
                new_password = request.POST.get('password')
                confirm_password = request.POST.get('confirm_password')

                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user)  # Maintenir la session active
                    messages.success(request, 'Votre mot de passe a été réinitialisé avec succès.')
                    return redirect('login')
                else:
                    messages.error(request, 'Les mots de passe ne correspondent pas.')
            return render(request, 'accounts/reset_user_password.html', {'user': user, 'uidb64': uidb64, 'token': token})
        else:
            return redirect('password_reset_invalid_token')
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None
        return redirect('reset_user_password')



logger = logging.getLogger(__name__)

@api_view(['POST'])
def send_email(request):
    try:
        nom = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')

        if not nom or not email or not message:
            raise DjangoValidationError("Tous les champs sont obligatoires.")

        validate_email(email)

        subject = f'Nouveau message de {nom}'
        from_email = email
        to_email = settings.EMAIL_HOST_USER

        send_mail(subject, message, from_email, [to_email], fail_silently=False)

        messages.success(request, 'Email envoyé avec succès.')
        return redirect('home')

    except DjangoValidationError as e:
        logger.error(f"Erreur de validation : {str(e)}")
        return Response({'error': str(e)}, status=400)
    except Exception as e:
        logger.error(f"Erreur lors de l'envoi de l'e-mail : {str(e)}")
        return Response({'error': 'Une erreur est survenue lors de l\'envoi de l\'email.'}, status=500)



class SendNotificationViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = SendNotificationSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            subject = serializer.validated_data.get('subject', 'Sujet de la notification')
            message = serializer.validated_data.get('message', 'Corps du message de la notification')

            from_email = settings.EMAIL_HOST_USER

            all_users = get_user_model().objects.all()
            if not all_users.exists():
                return Response({'message': 'Aucun utilisateur trouvé.'}, status=status.HTTP_404_NOT_FOUND)

            for user in all_users:
                email_subject = f'Notification: {subject}'
                email_message = f'Bonjour {user.email},\n\n{message}'

                send_mail(email_subject, email_message, from_email, [user.email], fail_silently=False)

            return Response({'message': 'Notifications envoyées avec succès à tous les utilisateurs.'}, status=status.HTTP_200_OK)

        except (DjangoValidationError, DRFValidationError) as e:
            return Response({'message': 'Erreur lors de la validation des données.', 'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except BadHeaderError:
            return Response({'message': 'Erreur lors de l\'envoi de l\'e-mail.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'message': f'Erreur inattendue: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
