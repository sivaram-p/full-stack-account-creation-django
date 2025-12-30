from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.loginpage,name='login'),
    path('login/',views.loginpage,name='login'),
    path('signup/',views.signuppage,name='signup'),
    path('dashboard/',views.dashboardpage,name='dashboard'),
    path('logout/',views.logoutuser,name='logout'),
]