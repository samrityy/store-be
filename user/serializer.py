from rest_framework import serializers

from .models import CartLine, CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


# class CartLineSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartLine
#         fields = ["product", "quantity"]

# def create(self, validated_data):

# product = validated_data.pop("product")
# cart = Cart.objects.get(user=self.context["request"].user)
# cart_line = CartLine.objects.create(product=product, cart=cart, **validated_data)
# return cart_line


class CartSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        read_only=True,source='product'
    )
    quantity = serializers.IntegerField(default=1)

    class Meta:
        model = CartLine
        fields = ["product_id", "quantity"]

