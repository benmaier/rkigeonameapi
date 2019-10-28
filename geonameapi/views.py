from django.shortcuts import render
from rest_framework import generics, permissions

from .models import (
            Featurecode,
            Continent,
            Countryinfo,
            Geoname,
            Hierarchy,
            Alternatename,
            Region,
        )

from .serializers import (
            FeaturecodeSerializer
        )

# Create your views here.

class FeaturecodeList(generics.ListCreateAPIView):
    queryset = Featurecode.objects.all()
    serializer_class = FeaturecodeSerializer

class FeaturecodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Featurecode.objects.all()
    serializer_class = FeaturecodeSerializer

