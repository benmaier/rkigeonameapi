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

class NestedFeaturecodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Featurecode
        fields = ['code', 'name']

class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ['code','name','englishname','geoname']

class NestedCountryinfoSerializer(serializers.ModelSerializer):
    continent = ContinentSerializer()
    class Meta:
        model = Countryinfo
        fields = ['iso_alpha2', 'name', 'continent','population']

class CountryinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countryinfo
        fields = [
            'iso_alpha2',        
            'iso_alpha3',        
            'iso_numeric',       
            'fips_code',         
            'name',              
            'englishname',       
            'capital',           
            'areainsqkm',        
            'population',        
            'continent',         
            'tld',               
            'currency',          
            'currencyname',      
            'phone',             
            'postalcodeformat',  
            'postalcoderegex',   
            'geonameid',         
            'languages',         
            'neighbours',        
            'equivalentfipscode',
            ]

class NestedAlternatenameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternatename
        fields = ['alternatename','isolanguage','ispreferredname','isshortname','iscolloquial','ishistoric']
            
class NestedGeonameSerializer(serializers.ModelSerializer):
    fcode = NestedFeaturecodeSerializer()
    class Meta:
        model = Geoname
        fields = ['geonameid', 'name','fcode']

class GeonameSerializer(serializers.ModelSerializer):
    country = NestedCountryinfoSerializer()
    children = NestedGeonameSerializer(many=True)
    allalternatenames = NestedAlternatenameSerializer(many=True)
    class Meta:

        model = Geoname
        fields = [
        'geonameid',               
        'name',                    
        'englishname',             
        'asciiname',               
        'allalternatenames',          
        'latitude',                
        'longitude',               
        'fclass',                  
        'fcode',                   
        'country',                 
        'cc2',                    
        'admin1',                 
        'admin2',                 
        'admin3',                 
        'admin4',                 
        'population',             
        'elevation',              
        'gtopo30',                
        'timezone',               
        'moddate',                
        'children',               
        ]

    #def create(self, validated_data):
    #    children_data = validated_data.pop('children')
    #    geoname = Geoname.objects.create(**validated_data)
    #    for track_data in tracks_data:
    #        Track.objects.create(album=album, **track_data)
    #    return album

class RegionSerializer(serializers.ModelSerializer):
    laender = NestedCountryinfoSerializer(many=True)
    class Meta:
        model = Region
        fields = [
        'region_id',     
        'name',          
        'englishname',   
        'geonameid',     
        'fcode',         
        'laender',
        ]

