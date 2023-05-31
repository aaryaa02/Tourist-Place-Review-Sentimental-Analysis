from operator import index
from django.urls import path
from user import views as user

urlpatterns = [
    path('',user.index),
    path('viewuserdata', user.viewuserdata),
    path('activateuser', user.activateuser),
    path('userlogincheck', user.userlogincheck),
    path('userregister', user.userregister),
    path('userlogin', user.userlogin),
    path('search', user.search),
    path('usersearchresult1', user.usersearchresult1),
    path('usersearchresult1', user.usersearchresult1),
    

]