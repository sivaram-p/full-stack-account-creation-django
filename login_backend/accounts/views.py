from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
try:
    from .models import addons
except ImportError:
    addons = None 

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
            messages.error(request, "400 Bad Request - Didnt recieve all fields")
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
        #if addons.phone.filter(phone=phone).exists():
        #    messages.error(request, "Phone number already registered.")
         #   return render(request, 'signup.html')

        
    return render(request,'signup.html')

def dashboardfun(request):
    return render(request,'dashboard.html')
