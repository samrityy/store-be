from rest_framework import serializers
from .models import CustomUser,Cart

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        extra_kwargs={
            'password':{'write_only':True}
        }
    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product', 'user', 'added_date', 'isAuthenticated']

        def validate(self, data):
            if not data['isAuthenticated']:
                raise serializers.ValidationError("User is not authenticated")
            return data
    