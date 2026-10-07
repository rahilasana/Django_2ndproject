from django.urls import path
from . import views


urlpatterns = [

    # Management home
    path("", views.management_home, name="management_home"),

    # Student search and details
    path("students/", views.student_search, name="student_search"),
    path("students/<int:id>/", views.student_detail, name="student_detail"),

    # Teacher search and details
    path("teachers/", views.teacher_search, name="teacher_search"),
    path("teachers/<int:id>/", views.teacher_detail, name="teacher_detail"),

    # Department search and details
    path("departments/", views.department_search, name="department_search"),
    path("departments/<int:id>/", views.department_detail, name="department_detail"),

    # Products
    path("products/", views.product_list, name="product_list"),
    path(
    "students/<int:id>/profile/",
    views.profile_detail,
    name="profile_detail"
),
]