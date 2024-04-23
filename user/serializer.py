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
        read_only=True
    )  # Field to accept product id from frontend
    quantity = serializers.IntegerField(default=1)

    class Meta:
        model = CartLine
        fields = ["product_id", "quantity"]

    # def create(self, validated_data):
    #     user = self.context["request"].user
    #     cart = Cart.objects.get_or_create(user=user)
    # product_ids = validated_data.pop("product_id")
    # # import ipdb; ipdb.set_trace()
    # user = self.context["request"].user
    # cart = Cart.objects.get_or_create(user=user)

    # if user.cart.exists():
    #     cart = user.cart.first()
    #     cart.product.add(*product_ids)
    #     return cart
    # else:
    #     cart = Cart.objects.create(user=user)
    #     cart.product.add(*product_ids)
    #     return cart
    # product = Product.objects.get(pk=product_id)
    # cart_item = Cart.objects.create(product=product, **validated_data)
    # return cart

    # def destroy(self,request,pk):
    #     try:
    #         cart=Cart.objects.get(pk=pk)
    #         cart.delete()
    #         return Response({'message':'Deleted'})
    #     except Cart.DoesNotExist:
    #         return Response({'message':'Cart not found'})
