
from auth_.models import MyUser, Profile
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from city.models import City
from city.serializers import CitySerializer

class MyUserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        # fields = '__all__'
        fields = ['id','username','is_staff','email','password','is_admin',]


class ProfileSerializer(ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ('id', 'user', 'city',  'card_number')#'card_number'

class ProfileGetSerializer(ModelSerializer):
    user = MyUserSerializer(read_only=True)
    city = CitySerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id','user', 'city', 'card_number']

class UserShortSerializer(MyUserSerializer):

    class Meta:
        model = MyUser
        # fields = '__all__'
        fields = ['username', 'email']

