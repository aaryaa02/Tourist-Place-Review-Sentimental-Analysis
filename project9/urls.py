"""project9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django import views
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from user import views as user
from adn import views as admin1
from turstguide import views as guide
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('user/', include('user.urls')),
    path('adn/', include('adn.urls')),
    path('turstguide/', include('turstguide.urls')),

    path('admin/',admin.site.urls),
    path('index/',admin1.index, name="index"),
    path('adminlogin/',admin1.adminlogin, name="adminlogin"),
    path('adminloginaction/',admin1.adminloginaction, name="adminloginaction"),
    path('svm/',admin1.svm, name="svm"),
    path('naviebiase/',admin1.naviebyes, name="naviebiase"),
    path('rf/',admin1.rf,name="rf"),
    path('logout/',admin1.logout,name="logout"),
    path('userlogincheck/',user.userlogincheck,name="userlogincheck"),
    path('userregister/',user.userregister,name="userregister"),
    path('viewuserdata/',user.viewuserdata,name="viewuserdata"),
    path('activateuser/',user.activateuser,name="activateuser"),
    path('userlogin/',user.userlogin,name="userlogin"),
    path('userhome/',user.userhome,name="userhome"),
    path('search/',user.search,name="search"),
    path('usersearchresult1/',user.usersearchresult1,name="usersearchresult1"),
    path('usersearchresult1/',user.usersearchresult1,name="usersearchresult1"),



    path('guidelogin/',guide.guidelogin,name="guidelogin"),
    path('guidelogincheck/',guide.guidelogincheck,name="guidelogincheck"),
    path('guideregister/',guide.guideregister,name="guideregister"),
    path('viewguidedata/',guide.viewguidedata,name="viewguidedata"),
    path('activateguide/',guide.activateguide,name="activateguide"),
    path('guidelogin/',guide.guidelogin,name="guidelogin"),
    path('guidehome/',guide.guidehome,name="guidehome"),
    path('uploaddata/',guide.uploaddata,name="uploaddata"),
    path('touristplaces/',guide.touristplaces,name="touristplaces"),
    path('viewplaces/',guide.viewplaces,name="viewplaces"),
   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









