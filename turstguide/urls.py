from operator import index
from django.urls import path
from turstguide import views as guide





urlpatterns = [
    
    # ... other URL patterns ...
    path('', guide.index),
    path('viewguidedata/', guide.viewguidedata),
    path('activateguide/', guide.activateguide),
    path('guidelogincheck/', guide.guidelogincheck),
    path('guideregister/', guide.guideregister),
    path('guidelogin/', guide.guidelogin),
    path('guidehome/', guide.guidehome),
    path('uploaddata/', guide.uploaddata),
    path('touristplaces/', guide.touristplaces),
    path('viewplaces/', guide.viewplaces),
    






]
