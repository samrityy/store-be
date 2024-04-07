from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

class Cart(models.Model):
    product = models.ManyToManyField("product.Product")
    user = models.OneToOneField("CustomUser", on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    isAuthenticated=models.BooleanField(default=False)

 