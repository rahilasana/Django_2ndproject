from django.db import models


# ==============================
# ONE-TO-MANY RELATIONSHIP
# Department 1 → MANY Teachers
# ==============================

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)

    # ONE-TO-MANY relationship
    # One Department can have MANY Teachers
    # Each Teacher belongs to ONE Department
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


# ==============================
# MANY-TO-MANY RELATIONSHIP
# Student MANY ↔ MANY Course
# ==============================

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)

    # MANY-TO-MANY relationship
    # One Student can have MANY Courses
    # One Course can have MANY Students
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


# ==============================
# ONE-TO-ONE RELATIONSHIP
# Student 1 ↔ 1 Profile
# ==============================

class Profile(models.Model):

    # ONE-TO-ONE relationship
    # One Student has ONE Profile
    # One Profile belongs to ONE Student
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE
    )

    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student.name} Profile"
    
    
# products
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name