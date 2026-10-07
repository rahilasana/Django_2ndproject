from django.urls import path
from . import views


urlpatterns = [
    path("student/", views.student_view, name="student"),
    path("profile/", views.profile_view, name="profile"),
    path("department/", views.department_view, name="department"),
    path("teacher/", views.teacher_view, name="teacher"),
    path("course/", views.course_view, name="course"),
        # Product URLs
    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.add_product, name="add_product"),
    path("products/edit/<int:id>/",views.edit_product, name="edit_product"),
]