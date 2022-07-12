from django.shortcuts import render
from rest_framework import mixins, viewsets

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny
from auth_.models import MyUser, Profile
from auth_.serializers import MyUserSerializer, ProfileGetSerializer, ProfileSerializer


class MyUserAPIView(generics.CreateAPIView,):
    permission_classes = (AllowAny,)
    serializer_class = MyUserSerializer

    def get_queryset(self):
        return MyUser.objects.all()

    def perform_create(self, serializer):
        username = self.request.data.get('username')
        password = self.request.data.get('password')
        email = self.request.data.get('email')
        # print(username)
        # print('-------------------------------------------------')
        user, created = MyUser.objects.get_or_create(username=username)
        user.email = email
        user.set_password(password)
        user.save()

class UserViewset(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = MyUserSerializer

    def perform_destroy(self, instance):
        user_name = instance.username
        instance.delete()

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()

    def get_serializer_class(self):
        return MyUserSerializer

    def get_queryset(self):
        if self.request.user.role == 2:
            return MyUser.objects.filter(id=self.request.user.id)
        return MyUser.objects.all()



class ProfileViewset(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProfileGetSerializer
        else:
            return ProfileSerializer


    def get_queryset(self):
        if self.request.user.role==2:
            return Profile.objects.filter(user=self.request.user)
        return Profile.objects.all()




