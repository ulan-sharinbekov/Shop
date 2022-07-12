from django_filters import ChoiceFilter
from rest_framework import filters
from django_filters import rest_framework as filters

from api.models import Product


class ProductSearchFilter(filters.FilterSet):
    #catalog = ChoiceFilter(choices=FILTER_CHOICES)
    price = filters.RangeFilter()
    sum = filters.RangeFilter()
    class Meta:
        model = Product
        fields = ['price', 'sum']

