from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action


from basket.models import Cart, DeliveryCost
from basket.serializers import CartFullSerializer, CartShortSerializer, DeliveryCostSerializer


class CartViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)

    queryset = Cart.objects.all().order_by('id')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            if self.kwargs.get('pk'):
                return CartFullSerializer
            return CartFullSerializer
        else:
            return CartShortSerializer

    def perform_create(self, serializer):

        if self.request.user.id ==  None:
            serializer.save()
        else:
            serializer.save(user=self.request.user)




class DeliveryCostViewSet(viewsets.ModelViewSet):
    queryset = DeliveryCost.objects.all().order_by('id')
    serializer_class = DeliveryCostSerializer