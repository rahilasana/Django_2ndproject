from django.contrib import admin

# Register your models here.

from .models import Student,product

admin.site.register(Student)
admin.site.register(product)
