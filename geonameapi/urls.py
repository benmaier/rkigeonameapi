from django.urls import path, include
from django.conf.urls import url
#from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
            FeaturecodeList,
            FeaturecodeDetail,
            CountryinfoList,
            CountryinfoDetail,
            GeonameList,
            GeonameDetail,
            GeonameChildrenUpdateDetail,
            ContinentList,
            ContinentDetail,
            RegionList,
            RegionDetail,
            RegionCountriesUpdateDetail,
        )

urlpatterns = [
    path('featurecode/', FeaturecodeList.as_view()),
    path('featurecode/<str:pk>', FeaturecodeDetail.as_view()),
    path('country/', CountryinfoList.as_view()),
    path('country/<str:pk>', CountryinfoDetail.as_view()),
    path('continent/', ContinentList.as_view()),
    path('continent/<str:pk>', ContinentDetail.as_view()),
    path('geoname/', GeonameList.as_view()),
    path('geoname/<int:pk>', GeonameDetail.as_view()),
    path('geonamechildren/<int:pk>', GeonameChildrenUpdateDetail.as_view()),
    path('region/', RegionList.as_view()),
    path('region/<str:pk>', RegionDetail.as_view()),
    path('regioncountries/<str:pk>', RegionCountriesUpdateDetail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
