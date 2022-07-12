from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token
from city import views



urlpatterns = [
    path('',views.city_list),
    path('<int:pk>/',views.city_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)