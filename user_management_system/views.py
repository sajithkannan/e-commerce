from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request,"home.html")

def login(request):
  return render(request,"login.html")

def register(request):
  return render(request,"registration.html")

def forgot_password(request):
    return render(request, "forgot_password.html")



