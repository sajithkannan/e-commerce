from django.urls import path
from  .import views

urlpatterns = [
    path('',views.index,name="landing"),
    path('login',views.login,name="login"),
    path('customer',views.customer,name="customer"),
    path('seller',views.seller,name="seller"),
    path('order',views.order,name="order"),
    
]


