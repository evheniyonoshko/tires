from django.shortcuts import render
from rest_framework import generics, permissions, status

from tiresapp.models import Tire
from tiresapp.serializers import TireSerializer

# Create your views here.


class TireList(generics.ListCreateAPIView):
    serializer_class = TireSerializer
    queryset = Tire.objects.all()


class TireDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TireSerializer
    queryset = Tire.objects.all()
