from django.contrib.auth import logout
from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cart, CartLine, CustomUser, Product
from .serializer import CartSerializer, UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        user = CustomUser.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("User not found")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # import ipdb; ipdb.set_trace()
        logout(request)
        return Response({"message": "Logout successful"})


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["POST"], url_path="add-to-cart")
    def add_to_cart(self, request):
        user = request.user
        validate = CartSerializer(data=request.data)
        is_valid = validate.is_valid()
        if not is_valid:
            return Response(validate.errors)
        # if validate.is_valid():
        #     cart = Cart.objects.get_or_create(user=user)
        #     product = Product.objects.get(pk=request.data.get("product_id"))
        #     cart_line = CartLine.objects.create(product=product, cart=cart, quantity=request.data.get("quantity", 1))
        #     return Response({"message": "Product added to cart"})
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)
        product = Product.objects.get(pk=product_id)
        cart = Cart.objects.get_or_create(user=user)[0]
        # import ipdb; ipdb.set_trace()
        cart_line_qs = user.cart.cart_lines.filter(product=product)
        if cart_line_qs.exists():
            cart_line = cart_line_qs.first()
            cart_line.quantity += quantity
            cart_line.save()
        else:
            cart_line = CartLine.objects.create(
                product=product, cart=cart, quantity=quantity
            )
        import ipdb

        ipdb.set_trace()
        return Response({"message": "Product added to cart"})
