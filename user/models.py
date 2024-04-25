from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import CustomUserManager
from rest_framework.authtoken.models import Token
from product.models import Product

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def get_or_create_token(self):
        token, created = Token.objects.get_or_create(user=self)
        return token.key

    def __str__(self):
        return self.email
    
class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

class CartLine(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_lines")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)