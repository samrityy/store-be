from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import UserManager

class CustomUser(AbstractBaseUser):
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    username=models.CharField(max_length=255, blank=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=UserManager()

class Cart(models.Model):
    product = models.ManyToManyField("product.Product")
    user = models.OneToOneField("CustomUser", on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    isAuthenticated=models.BooleanField(default=False)

 