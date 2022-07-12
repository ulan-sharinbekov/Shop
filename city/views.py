from django.shortcuts import render
import logging

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from city.models import City
from city.serializers import CitySerializer
from auth_.permissions import IsAdmin

@api_view(['GET', 'POST'])
@permission_classes([IsAdmin, ])
def city_list(request, format=None):
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            city_name = serializer.data['name']
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAdmin, ])
def city_detail(request, pk,format=None):
    try:
        city = City.objects.get(pk=pk)
    except City.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = CitySerializer(city)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            city_name = serializer.data['name']
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        city_id = city.id
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


