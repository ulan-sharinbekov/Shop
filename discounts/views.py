from django.shortcuts import render
from rest_framework import viewsets
from discounts.models import Campaign, Coupon
from discounts.serializers import CampaignSerializer, CouponSerializer
# Create your views here.

class CampaignViwSet(viewsets.ModelViewSet):

    queryset = Campaign.objects.all().order_by('id')
    serializer_class = CampaignSerializer


class CouponViwSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all().order_by('id')
    serializer_class = CouponSerializer
