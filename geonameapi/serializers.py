from rest_framework import serializers, permissions
from .models import (
            Featurecode,
            Continent,
            Countryinfo,
            Geoname,
            Hierarchy,
            Alternatename,
            Region,
        )

class FeaturecodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Featurecode
        fields = ['code', 'name', 'description', 'searchorder_detail']
