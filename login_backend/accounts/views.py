from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import addons
from django.db import IntegrityError
from django.http import HttpResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def logoutuserfun(request):
    logout(request)
    return redirect('loginpage')
def loginfun(request):
    return render(request,'login.html')


def check_username(request):
    username= request.GET.get('userid')
    if len(username) < 1:
        return HttpResponse('')
    if not username.isalnum():
        return HttpResponse("<span class='error'>User-ID should have only whole numbers and alphabets</span>")
    if User.objects.filter(username=username).exists():
        return HttpResponse("<span class='error'>User-ID already in use</span>")
    return HttpResponse("<span class='success'>User-ID available for use</span>")

def check_email(request):
    email= request.GET.get('email')
    if len(email) < 1:
        return HttpResponse('')
    try:
        validate_email(email)
    except ValidationError:
        return HttpResponse("<span class='error'>Enter a valid email address</span>")

    if User.objects.filter(email=email).exists():
        return HttpResponse("<span class='error'>Email already in use</span>")
    return HttpResponse('')

def check_phone(request):
    phone= request.GET.get('phone')
    if not phone.isdigit():
        return HttpResponse("<span class='error'>Phone number must contain only digits</span>")
    if len(phone) < 10:
        return HttpResponse('')
    if addons.objects.filter(phone=phone).exists():
        return HttpResponse("<span class='error'>Phone number already in use</span>")
    return HttpResponse('')



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
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Enter a valid email address.")
            return render(request, 'signup.html')

        
        if User.objects.filter(username=username).exists():
            messages.error(request, "HTTP 409 Conflict - Username already taken.")
            return render(request, 'signup.html')
        if not username.isalnum():
            messages.error(request, "User-ID should have only whole numbers and alphabets.")
            return render(request, 'signup.html')
        
        if not password1.isascii():
            messages.error(request, "Password must not contain emojis.")
            return render(request, 'signup.html')
        if len(password1) < 8:
            messages.error(request, "Password must be at least 8 characters.")
            return render(request, 'signup.html')
        if not any(c.isalpha() for c in password1) or not any(c.isdigit() for c in password1):
            messages.error(request, "Password must contain letters and numbers.")
            return render(request, 'signup.html')
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')
        
        if addons.objects.filter(phone=phone).exists():
           messages.error(request, "HTTP 409 Conflict - Phone number already registered.")
           return render(request, 'signup.html')
        if not phone.isdigit():
            messages.error(request, "Phone number must contain only digits.")
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

    messages.warning(request," WARNINNG:  In case of incorrect input, the page may refresh and you may be required to re-enter your details. Please make use of the green and red validation messages displayed during form entry to verify your inputs.")

    return render(request,'signup.html')

def dashboardfun(request):
    return render(request,'dashboard.html')
