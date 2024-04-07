from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    username=None
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

class Cart(models.Model):
    product = models.ManyToManyField("product.Product")
    user = models.OneToOneField("CustomUser", on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    isAuthenticated=models.BooleanField(default=False)

 