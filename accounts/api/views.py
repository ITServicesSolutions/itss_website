from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

# from rest_framework.permissions import IsAuthenticated


from accounts.models import User
from .serializers import UserSerializer
from django.db.models import Q


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/users',
        'GET /api/users/:id'
    
    ]
    return Response(routes)



@api_view(['GET', "POST"])

# @permission_classes([IsAuthenticated])

def getUsers(request):
    
    if request.method == 'GET':
        
        query = request.GET.get('query')
        
        if query == None:
            query = ''
            
        users = User.objects.filter(Q(phone__icontains=query) | Q(email__icontains=query) | Q(password__icontains=query))
        
        # users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    
    if request.method == 'POST':
        
        user = User.objects.create(
            phone = request.data['phone'],
            email = request.data['email'],
            password = request.data['password']
            )
        
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

#Methode avec utilisation des classes

class GetUser(APIView):
    
    
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise JsonResponse('User does not exist.')
    
    def get(self, request, pk):
        user = self.get_object(pk=pk)
        
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk=pk)
        
        user.phone = request.data['phone'],
        user.email = request.data['email'],
        user.password = request.data['password']
        user.save()
        
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        user = self.get_object(pk=pk)
        
        user.delete()
        return Response('User was deleted.')

#Utiliser cette method pour ne pas utiliser les classes

# @api_view(['GET', 'PUT', 'DELETE'])
# def getUser(request, pk):
    
#     user = User.objects.get(id=pk)
    
#     if request.method == 'GET':
        
#         serializer = UserSerializer(user, many=False)
#         return Response(serializer.data)
    
    
#     if request.method == 'PUT':
    
#         user.phone = request.data['phone'],
#         user.email = request.data['email'],
#         user.password = request.data['password']
#         user.save()
        
#         serializer = UserSerializer(user, many=False)
#         return Response(serializer.data)
    
#     if request.method == 'DELETE':
        
#         user.delete()
#         return Response('User was deleted.')
        