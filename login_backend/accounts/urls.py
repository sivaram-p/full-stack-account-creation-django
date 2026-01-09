from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.loginfun,name='login'),
    path('login/',views.loginfun,name='login'),
    path('signup/',views.signupfun,name='signup'),
    #path('dashboard/',views.dashboardfun,name='dashboardpage'),
    path('logout/',views.logoutuserfun,name='logout'),
]