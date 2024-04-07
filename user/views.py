from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializer import UserSerializer 
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
        
class CartView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return Response({'cart': user.cart_set.all()})
        else:
            return Response({'error': 'User is not authenticated'}, status=401)
    
    def post(self, request):
        user = request.user
        if user.is_authenticated:
            user.cart_set.create(product=request.data['product'])
            return Response({'cart': user.cart_set.all()})
        else:
            return Response({'error': 'User is not authenticated'}, status=401)
    
    def delete(self, request):
        user = request.user
        if user.is_authenticated:
            user.cart_set.filter(product=request.data['product']).delete()
            return Response({'cart': user.cart_set.all()})
        else:
            return Response({'error': 'User is not authenticated'}, status=401)