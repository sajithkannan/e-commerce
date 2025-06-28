from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout,get_user_model
from django.contrib import messages
from django.db import IntegrityError

User = get_user_model()


def registration(request):
    print('000000000')
    if request.method == 'POST':
        print("Received POST request for registration.")
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            name = request.POST.get('name')
            lastName = request.POST.get('lastName')
            phone = request.POST.get('phone')
            alternative = request.POST.get('alternative')
            gender = request.POST.get('gender')
            pinCode = request.POST.get('pinCode')
            address = request.POST.get('address')
            landmark = request.POST.get('landmark')
            country = request.POST.get('country')
            state = request.POST.get('state')
            city = request.POST.get('city')
            role = request.POST.get('role')

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
                return redirect('registration')

            print("Creating user...")

            user = User.objects.create_user(
                email=email,
                password=password,
                name=name,
                lastName=lastName,
                phone=phone,
                alternative=alternative,
                gender=gender,
                pinCode=pinCode,
                address=address,
                landmark=landmark,
                country=country,
                state=state,
                city=city,
                role=role,
            )

            

            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('/')

        except IntegrityError:
            messages.error(request, "A database error occurred. Please try again.")
        except Exception as e:
            print("Unexpected error:", e)
            messages.error(request, f"Unexpected error: {str(e)}")

    print("Rendering registration form.")
    return render(request, 'registration.html')


# def registration(request):
    print('a')
    if request.method == 'POST':
        print("Received POST request for registration.")
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            name = request.POST.get('name')
            lastName = request.POST.get('lastName')
            phone = request.POST.get('phone')
            alternative = request.POST.get('alternative')
            gender = request.POST.get('gender')
            pinCode = request.POST.get('pinCode')
            address = request.POST.get('address')
            landmark = request.POST.get('landmark')
            country = request.POST.get('country')
            state = request.POST.get('state')
            city = request.POST.get('city')
            role = request.POST.get('role')

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
                return redirect('user_app:registration')
            print("AAAAAAAAAAAAA")
            user = User.objects.create_user(
                email=email,
                password=password,
                name=name,
                lastName=lastName,
                phone=phone,
                alternative=alternative,
                gender=gender,
                pinCode=pinCode,
                address=address,
                landmark=landmark,
                country=country,
                state=state,
                city=city,
                role=role,
            )
   
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('/')

        except IntegrityError:
            messages.error(request, "A database error occurred. Please try again.")
        except Exception as e:
            print("Unexpected error:", e)
            messages.error(request, f"Unexpected error: {str(e)}")

    print("Rendering registration form.")
    return render(request, 'registration.html')
        

#login view         
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f"Login attempt with email: {email}")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            messages.success(request, f"Welcome, {user.full_name}!")

            if user.role == 'customer':
                return redirect('customer_dashboard')  
            else:
                return redirect('landing')  

        else:
            messages.error(request, "Invalid credentials.")
            return redirect('index')
    return redirect('index')


# Logout view
def logout_view(request):
    request.session.flush() 
    messages.success(request, "You have been logged out.")
    return redirect('index') 


def user_profile(request):
    user = request.user
    profile = User.objects.get(email=user.email)  
    context = {
        'profile': profile,
        'user': request.user,
    }
    return render(request, 'login.html', context)




def home(request):
  return render(request,"home.html")

def login(request):
  return render(request,"login.html")

def register_view(request):
  return render(request,"registration.html")

def forgot_password(request):
    return render(request, "forgot_password.html")



