from django.shortcuts import render, redirect
from .models import CustomUser, Customer, Seller
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.db import IntegrityError

User = get_user_model()

# Registration view
def registration(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            role = request.POST.get('role')

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
                return redirect('registration')

            # Common user creation
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                role=role,

            )

            # Role-specific details
            if role == 'Customer':
                Customer.objects.create(
                    user=user,
                    name=request.POST.get('name'),
                    lastName=request.POST.get('lastName'),
                    phone=request.POST.get('phone'),
                    alternative=request.POST.get('alternative'),
                    gender=request.POST.get('gender'),
                    pinCode=request.POST.get('pinCode'),
                    address=request.POST.get('address'),
                    landmark=request.POST.get('landmark'),
                    country=request.POST.get('country'),
                    state=request.POST.get('state'),
                    city=request.POST.get('city')
                )

            elif role == 'Seller':
                Seller.objects.create(
                    user=user,
                    business_name=request.POST.get('business_name'),
                    category=request.POST.get('category'),
                    subcategory=request.POST.get('subcategory'),
                    business_address=request.POST.get('business_address'),
                    gst_number=request.POST.get('gst_number')
                )

            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect(' ')

        except IntegrityError:
            messages.error(request, "A database error occurred. Please try again.")
        except Exception as e:
            print("Unexpected error:", e)
            messages.error(request, f"Unexpected error: {str(e)}")

    return render(request, 'registration.html')


# Login view
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f"Login attempt with email: {email}")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            messages.success(request, f"Welcome, {user.user_name}!")

            if user.role == 'Customer':
                return redirect('customer_dashboard')
            elif user.role == 'Seller':
                return redirect('seller_dashboard')
            else:
                return redirect('home')

        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')
    return render(request, 'login.html')


# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
    


# User profile view
def user_profile(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login first.")
        return redirect('login')

    user = request.user
    context = {
        'profile': user,
    }
    return render(request, 'profile.html', context)


# Static pages
def home(request):
    return render(request, "home.html")

def forgot_password(request):
    return render(request, "forgot_password.html")

def features(request):
    return render(request, "features.html")

def support(request):
    return render(request, "support.html")
