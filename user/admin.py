from django.contrib import admin

# Register your models here.
from .models import CustomUser,Cart
admin.site.register(CustomUser)
admin.site.register(Cart)