from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser,Cart
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import viewsets

from .serializer import UserSerializer, CartSerializer
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
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # permission_classes = [permissions.IsAuthenticated]