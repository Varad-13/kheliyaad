from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout, password_validation
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .models import *
# Create your views here.

def Home(request):
    return render(request, 'core/index.html')

class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return render(request, 'core/login.html')
    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        auth = authenticate(request, username=email, password=password)

        if auth is not None:
            login(request, auth)
            messages.success(request, "You have successfully logged in.")
            return redirect("home")
        
        else:
            if not User.objects.filter(email=email).exists():
                messages.error(request, "Invalid email address.")
            else:
                messages.error(request, "Incorrect password. Please try again.")

        return render(request, 'core/login.html')
    
class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "You have successfully logged out.")
        else:
            messages.warning(request, "You are not logged in.")
        return redirect("login")

class Signup(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'core/signup.html')

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")

        # Check if email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email address is already in use.")
            return render(request, 'core/signup.html')

        if confirm_password != password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'core/signup.html')

        # Password validation
        try:
            password_validation.validate_password(password=password)
        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)
            return render(request, 'core/signup.html')

        # Create User and UserProfile
        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=make_password(password),
                first_name=fname,
                last_name=lname
            )
            UserProfile.objects.create(
                user=user,
                fname=fname,
                lname=lname,
                phone=phone,
                address=address,
                city=city,
                state=state,
                pincode=pincode
            )
            login(request, user)  # Log in the user after signup
            messages.success(request, "Account created successfully!")
            return redirect('home')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return render(request, 'core/signup.html')
