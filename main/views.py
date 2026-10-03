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

"CRUD Oprations"
# create 
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
#Read
#Ab agar tum SQL directly likho:
#SELECT * FROM student;
#Django mein ORM (Object-Relational Mapping) se:
#Student.objects.all()
def students(request):
    all_students = Student.objects.all()

    return render(request, "students.html", {
        "students": all_students
    })
# update operation
def update(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.name = request.POST["name"]
        student.email = request.POST["email"]
        student.age = request.POST["age"]

        student.save()

        return redirect("students")  #redirect() mein URL ka name dena hota hai, template ka naam nahi.                            
    return render(                   #path("students/", views.students, name="students")
                            
        request,
        "update_student.html",
        {"student": student}
    )
    
#delete operation
def delete(request,id):
    student = Student.objects.get(id=id)
    
    student.delete()
    return redirect("students")
    