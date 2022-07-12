from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from auth_.views import *

router = DefaultRouter()

router.register('users', UserViewset, basename='user')
router.register('profiles',ProfileViewset , basename='profile')



urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', MyUserAPIView.as_view()),
]

urlpatterns += router.urls