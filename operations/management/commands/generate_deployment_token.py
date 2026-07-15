from django.core.management.base import BaseCommand
from rest_framework_simplejwt.tokens import AccessToken
from accounts.models import User


class Command(BaseCommand):
    help = 'Génère un token JWT de déploiement pour un administrateur'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email de l\'administrateur')

    def handle(self, *args, **options):
        email = options['email']
        
        try:
            user = User.objects.get(email=email, is_staff=True, is_superuser=True)
            token = AccessToken.for_user(user)
            
            self.stdout.write(self.style.SUCCESS(f'✅ Token de déploiement généré avec succès !'))
            self.stdout.write(self.style.SUCCESS(f'Voici votre DEPLOYMENT_API_TOKEN :'))
            self.stdout.write(self.style.WARNING(f'\n{str(token)}\n'))
            self.stdout.write(self.style.SUCCESS(f'Copiez-le et ajoutez-le dans les secrets GitHub !'))
            
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'❌ Aucun administrateur trouvé avec l\'email "{email}"'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Erreur : {str(e)}'))