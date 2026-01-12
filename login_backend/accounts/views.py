from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def logoutuserfun(request):
    logout(request)
    return redirect('loginpage')
def loginfun(request):
    return render(request,'login.html')
def signupfun(request):
    if request.method == 'POST':
        username = request.POST.get('userid')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        profilepic = request.FILES.get('profilepic')
        phone = request.POST.get('phone')
        about = request.POST.get('about')
        if not all([fullname, email, username, password, password2]):
            messages.error(request, "didnt recieve all fields")
            return render(request, 'signup.html')
        else:
            messages.success(request, "all fields received")
            return render(request, 'signup.html')
    return render(request,'signup.html')

def dashboardfun(request):
    return render(request,'dashboard.html')
