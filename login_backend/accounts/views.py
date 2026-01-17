from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import addons
from django.db import IntegrityError
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def logoutuserfun(request):
    logout(request)
    return redirect('loginpage')
def loginfun(request):
    return render(request,'login.html')
def signupfun(request):
    if request.method == 'POST':
        username = request.POST.get('userid')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        profilepic = request.FILES.get('profilepic')
        phone = request.POST.get('phone')
        about = request.POST.get('about')
        if not all([fullname, email, username, phone, password1, password2]):
            messages.error(request, "HTTP 422 - Didnt recieve all fields")
            return render(request, 'signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "HTTP 409 Conflict - Email already registered.")
            return render(request, 'signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "HTTP 409 Conflict - Username already taken.")
            return render(request, 'signup.html')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')
        
        if addons.objects.filter(phone=phone).exists():
           messages.error(request, "HTTP 409 Conflict - Phone number already registered.")
           return render(request, 'signup.html')
        try:
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=fullname)
            addons.objects.create(user=user, phone=phone, about=about, profilepic=profilepic)
        except IntegrityError:
            messages.error(request,"400 Bad Request - sorry account creation failed")
            return render(request,'signup.html')
        except Exception:
            logger.exception("Unexpected error during signup")
            raise

        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request,'signup.html')

def dashboardfun(request):
    return render(request,'dashboard.html')
