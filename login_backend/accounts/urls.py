from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.loginfun,name='loginpage'),
    path('login/',views.loginfun,name='loginpage'),
    path('signup/',views.signupfun,name='signuppage'),
    path('dashboard/',views.dashboardfun,name='dashboardpage'),
    path('logout/',views.logoutuserfun,name='logoutpage'),
]