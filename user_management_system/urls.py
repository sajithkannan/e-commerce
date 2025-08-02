from django.contrib import admin
from django.urls import path
from user_management_system.views import home,login_view,registration,forgot_password,logout_view,user_profile,features,support 

app_name = 'user_management_system'  


from django.urls import path
from . import views

urlpatterns = [
    
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('features/', views.features, name='features'),
    path('support/', views.support, name='support'),
]



