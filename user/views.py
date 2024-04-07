from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from rest_framework.exceptions import AuthenticationFailed

from .serializer import UserSerializer 
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class RegisterView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
        def post(self,request):
            email=request.data['email']
            password=request.data['password']
            user=CustomUser.objects.filter(email=email).first()
            if user is None:
                raise AuthenticationFailed('User not found')
            if not user.check_password(password):
                raise AuthenticationFailed('Incorrect password')
            return Response({'message':'Success'})
# class CartView(APIView):
#     def get(self, request):
#         user = request.user
#         if user.is_authenticated:
#             return Response({'cart': user.cart_set.all()})
#         else:
#             return Response({'error': 'User is not authenticated'}, status=401)
    
#     def post(self, request):
#         user = request.user
#         if user.is_authenticated:
#             user.cart_set.create(product=request.data['product'])
#             return Response({'cart': user.cart_set.all()})
#         else:
#             return Response({'error': 'User is not authenticated'}, status=401)
    
#     def delete(self, request):
#         user = request.user
#         if user.is_authenticated:
#             user.cart_set.filter(product=request.data['product']).delete()
#             return Response({'cart': user.cart_set.all()})
#         else:
#             return Response({'error': 'User is not authenticated'}, status=401)