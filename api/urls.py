from django.urls import path, include

from api.views import CatalogViews, ProductView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('catalog',CatalogViews , basename='catalogs')
router.register('product',ProductView, basename='product')


urlpatterns = [
      # path('g', ProductViewSet.as_view())

]
urlpatterns += router.urls





