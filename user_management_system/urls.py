from django.contrib import admin
from django.urls import path
from user_management_system.views import home,login,registration,forgot_password 

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('login/',login,name="login"),
    path('registration/', registration, name='registration'),

    path('forgot_password/',forgot_password, name='forgot_password'),
]


