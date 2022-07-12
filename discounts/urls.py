from django.urls import include, path
from rest_framework import routers
from discounts.views import CouponViwSet, CampaignViwSet

router = routers.DefaultRouter()
router.register(r'campaign', CampaignViwSet)
router.register(r'coupon', CouponViwSet)

urlpatterns = [
    path('', include((router.urls, 'Shop.discounts'))),
]