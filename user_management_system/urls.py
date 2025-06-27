from django.contrib import admin
from django.urls import path
from user_management_system.views import home,login,register,forgot_password 

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('login/',login,name="login"),
    path('register/',register,name="register"),
    path('forgot_password/',forgot_password, name='forgot_password'),
]


