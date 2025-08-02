from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    # path('home/', TemplateView.as_view(template_name='landing.html'), name='landing'),

    path('user_management_system/', include('user_management_system.urls')),

]

if settings.DEBUG:
 urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

