from operator import index
from django.urls import path
from adn import views as admin1

urlpatterns = [
    path('', admin1.index),
    path('adminlogin/', admin1.adminlogin),
    path('adminhome/', admin1.adminhome),
    path('adminloginaction/', admin1.adminloginaction),
    path('logout/', admin1.logout),
    path('rf/', admin1.rf),
    path('naviebyes/', admin1.naviebyes),
 
   
]