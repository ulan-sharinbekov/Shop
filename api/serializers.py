from rest_framework.serializers import ModelSerializer
from api.models import Catalog, Product, SIZE_Prod

class CatalogSerializer(ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'

class SizeSerializer(ModelSerializer):
    class Meta:
        model = SIZE_Prod
        fields = '__all__'


class ProductFullSerializer(ModelSerializer):
    catalog =CatalogSerializer(read_only=True)
    size = SizeSerializer(read_only=True)
    #fields = ('id', 'user', 'city', 'card_number')  # 'card_number'
    class Meta:
        model = Product
        fields = '__all__'



class ProductShortSerializer(ModelSerializer):
    catalog = CatalogSerializer(read_only=True)
    class Meta:
        model = Product
        #fields = ('name', 'description', 'venCode' )
        fields = ('catalog', 'name', 'image','price' )

class ProductPostPutSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('catalog', 'name', 'description', 'article', 'image', 'size','price', 'quantity', 'description' )


    def create(self, validated_data):
        order = Product(**validated_data)
        order.get_sum()
        order.save()
        return order
    #
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.catalog = validated_data.get('catalog', instance.catalog)
        instance.venCode = validated_data.get('venCode', instance.venCode)
        instance.price = validated_data.get('price', instance.price)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.RemaniningStock = validated_data.get('RemaniningStock', instance.RemaniningStock)
        #instance.sum = validated_data.get('sum', instance.sum)
        instance.get_sum()
        instance.save()

        return instance