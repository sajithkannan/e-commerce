from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request,"index.html")

def login(request):
  return render(request,"login.html")

def customer(request):
  return render(request,"customer_register.html")

def seller(request):
  return render(request,"seller_register.html")

def order(request):
  return render(request,"order.html")


