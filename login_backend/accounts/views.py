from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def logoutuserfun(request):
    logout(request)
    return redirect('loginpage')
def loginfun(request):
    return render(request,'login.html')
def signupfun(request):
    return render(request,'signup.html')

def dashboardfun(request):
    return render(request,'dashboard.html')
