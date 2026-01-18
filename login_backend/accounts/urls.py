from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.loginfun,name='login'),
    path('login/',views.loginfun,name='login'),
    path('signup/',views.signupfun,name='signup'),
    path('logout/',views.logoutuserfun,name='logout'),
    path('dashboard/',views.dashboardfun,name='dashboard'),
    path('check_username/',views.check_username,name='check_username'),
    path('check_email/',views.check_email,name='check_email'),
    path('check_phone/',views.check_phone,name='check_phone'),
]