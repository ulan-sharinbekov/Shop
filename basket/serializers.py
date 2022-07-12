from rest_framework import serializers
from auth_.serializers import MyUserSerializer
from api.models import Product
from basket.models import Cart, DeliveryCost  # , Item #ShoppingCart,


class CartFullSerializer(serializers.ModelSerializer):
    # user = MyUserSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = '__all__'#['id', 'user', 'item', 'quantity', 'created_at', 'updated_at']



class CartShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id',  'item', 'quantity', 'created_at', 'updated_at']


class DeliveryCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCost
        fields = ['id', 'status', 'cost_per_delivery', 'cost_per_product', 'fixed_cost', 'created_at', 'updated_at']