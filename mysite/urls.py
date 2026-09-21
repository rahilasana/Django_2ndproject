from django.contrib import admin
from django.urls import path,include

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('services/', views.services,name="services"),
    path('contact/', views.contact,name="contact"),
    
    path('__reload__/', include('django_browser_reload.urls')),
]