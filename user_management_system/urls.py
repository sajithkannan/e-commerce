from django.contrib import admin
from django.urls import path
from user_management_system.views import home,login_view,registration,forgot_password,logout_view,user_profile,features,support 

app_name = 'user_management_system'  

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('/', home, name="home"),
    path('registration/',registration, name='registration'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('profile/',user_profile, name='profile'),
    path('forgot-password/',forgot_password, name='forgot_password'),
    path('features/',features, name='features'),
    path('support/',support, name='support')
]


