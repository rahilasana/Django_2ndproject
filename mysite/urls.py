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
    
    path("student_add/", views.add_student, name="add_student"),
    path("students/", views.students, name="students"),
    # account app is made for authentication concept
    path("accounts/", include("accounts.urls")),
    
    path('update/<int:id>/', views.update, name='update_student'),
    path('delete/<int:id>/', views.delete, name='delete_student'),
    #  management app is made for relationships concepts
    path("management/", include("management.urls")),
    
]