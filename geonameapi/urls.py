from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
        FeaturecodeList,
        FeaturecodeDetail,
        )

urlpatterns = [
    path('featurecodes/', FeaturecodeList.as_view()),
    path('featurecodes/<str:pk>', FeaturecodeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
