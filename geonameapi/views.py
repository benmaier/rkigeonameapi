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
            FeaturecodeSerializer,
            CountryinfoSerializer,
            ContinentSerializer,
            GeonameSerializer,
            GeonameChildrenUpdateSerializer,
            RegionSerializer,
            RegionCountriesUpdateSerializer,
        )

# Create your views here.

class FeaturecodeList(generics.ListCreateAPIView):
    queryset = Featurecode.objects.all()
    serializer_class = FeaturecodeSerializer

class FeaturecodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Featurecode.objects.all()
    serializer_class = FeaturecodeSerializer

class CountryinfoList(generics.ListCreateAPIView):
    queryset = Countryinfo.objects.all()
    serializer_class = CountryinfoSerializer

class CountryinfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Countryinfo.objects.all()
    serializer_class = CountryinfoSerializer

class ContinentList(generics.ListCreateAPIView):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer

class ContinentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer

class GeonameList(generics.ListCreateAPIView):
    queryset = Geoname.objects.all()
    serializer_class = GeonameSerializer

class GeonameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Geoname.objects.all()
    serializer_class = GeonameSerializer

class GeonameChildrenUpdateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Geoname.objects.all()
    serializer_class = GeonameChildrenUpdateSerializer

class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionCountriesUpdateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionCountriesUpdateSerializer


