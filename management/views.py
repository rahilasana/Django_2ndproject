from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import (
    Department,
    Teacher,
    Course,
    Student,
    Profile,
    Product,
)

from .forms import (
    StudentSearchForm,
    TeacherSearchForm,
    DepartmentSearchForm,
)


# Management home
@login_required
def management_home(request):
    return render(
        request,
        "management/management_home.html"
    )


# Search student by name
@login_required
def student_search(request):

    form = StudentSearchForm()
    student = None

    if request.method == "POST":

        form = StudentSearchForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data["name"]

            # ORM search
            student = Student.objects.filter(
                name__icontains=name
            ).first()

    return render(
        request,
        "management/student_search.html",
        {
            "form": form,
            "student": student,
        }
    )


# Student details
@login_required
def student_detail(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    # Many-to-Many: Student → Courses
    courses = student.courses.all()

    # One-to-One: Student → Profile
    profile = getattr(
        student,
        "profile",
        None
    )

    return render(
        request,
        "management/student_detail.html",
        {
            "student": student,
            "courses": courses,
            "profile": profile,
        }
    )


# Search teacher by name
@login_required
def teacher_search(request):

    form = TeacherSearchForm()
    teacher = None

    if request.method == "POST":

        form = TeacherSearchForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data["name"]

            # ORM search
            teacher = Teacher.objects.filter(
                name__icontains=name
            ).first()

    return render(
        request,
        "management/teacher_search.html",
        {
            "form": form,
            "teacher": teacher,
        }
    )


# Teacher details
@login_required
def teacher_detail(request, id):

    teacher = get_object_or_404(
        Teacher,
        id=id
    )

    # ForeignKey: Teacher → Department
    department = teacher.department

    return render(
        request,
        "management/teacher_detail.html",
        {
            "teacher": teacher,
            "department": department,
        }
    )


# Search department by name
@login_required
def department_search(request):

    form = DepartmentSearchForm()
    department = None

    if request.method == "POST":

        form = DepartmentSearchForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data["name"]

            # ORM search
            department = Department.objects.filter(
                name__icontains=name
            ).first()

    return render(
        request,
        "management/department_search.html",
        {
            "form": form,
            "department": department,
        }
    )


# Department details
@login_required
def department_detail(request, id):

    department = get_object_or_404(
        Department,
        id=id
    )

    # Reverse ForeignKey: Department → Teachers
    teachers = department.teacher_set.all()

    return render(
        request,
        "management/department_detail.html",
        {
            "department": department,
            "teachers": teachers,
        }
    )


# Student profile
@login_required
def profile_detail(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    # One-to-One: Student → Profile
    profile = get_object_or_404(
        Profile,
        student=student
    )

    return render(
        request,
        "management/profile_detail.html",
        {
            "student": student,
            "profile": profile,
        }
    )


# Product list
@login_required
def product_list(request):

    # Get all products
    products = Product.objects.all()

    return render(
        request,
        "management/product_list.html",
        {
            "products": products,
        }
    )