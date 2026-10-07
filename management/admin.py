from django.contrib import admin
from .models import Product

# Register your models here.

from .models import Department, Teacher, Course, Student, Profile


# Register all models in Django Admin
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Profile)

admin.site.register(Product)
