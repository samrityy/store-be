from rest_framework import serializers
from .models import CustomUser,Cart

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product', 'user', 'added_date', 'isAuthenticated']

        def validate(self, data):
            if not data['isAuthenticated']:
                raise serializers.ValidationError("User is not authenticated")
            return data
    