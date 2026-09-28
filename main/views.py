from django.shortcuts import render, redirect
from .models import Student
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')


def add_student(request):

    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        age = request.POST["age"]

        Student.objects.create(
            name=name,
            email=email,
            age=age
        )

        return redirect("/students/")

    return render(request, "add_student.html")

def students(request):
    all_students = Student.objects.all()

    return render(request, "students.html", {
        "students": all_students
    })