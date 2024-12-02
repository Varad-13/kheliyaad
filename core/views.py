from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .models import *
# Create your views here.

def home(request):
    return render(request, 'core/index.html')

class login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(home)
        else:
            return render(request, 'core/login.html')
    def post(self, request):
        email = request.POST.get("username")
        password = request.POST.get("password")
        auth = authenticate(request, username=email, password=password)

        if auth is not None:
            login(request, auth)
            return redirect(home)
        
        else:
            if not User.objects.filter(email=email).exists():
                messages.error(request, "Invalid email address.")
            else:
                messages.error(request, "Incorrect password. Please try again.")

        return render(request, 'core/login.html')