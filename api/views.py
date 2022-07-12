import logging
from django.shortcuts import render
from rest_framework import views, mixins, generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from api.service import ProductSearchFilter
from auth_.permissions import IsAdmin
from api.serializers import CatalogSerializer, ProductFullSerializer, ProductShortSerializer, ProductPostPutSerializer

from api.models import Catalog, Product
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

logger = logging.getLogger('main')

class ResultSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class CatalogViews(viewsets.ModelViewSet):
   permission_classes = (IsAuthenticatedOrReadOnly,)
   queryset = Catalog.objects.all()
   serializer_class = CatalogSerializer
   pagination_class = ResultSetPagination




class ProductView(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = ResultSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductSearchFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            if self.kwargs.get('pk'):
                return ProductFullSerializer
            return ProductShortSerializer
        else:
            return ProductPostPutSerializer

    def get_queryset(self):
        return Product.objects.all()


    def perform_destroy(self, instance):
        print(self.name)
        product_id = Product.objects.get(pk=self.kwargs['pk'])
        if self.request.user.role == 1:
            instance.delete()
            logger.info(f'Данный товар успешно удален: {product_id}')
        else:
            logger.info(f'у вас нет прав для удалении данного товара:  {product_id}')

    def perform_update(self, serializer):
        product_id = Product.objects.get(pk=self.kwargs['pk'])
        if self.request.user.role == 1:
            serializer.save()
            logger.info(f'Данный товар успешно изменен: {product_id}')
        else:
            logger.info(f'у вас нет прав для изменения данного товара:  {product_id}')
