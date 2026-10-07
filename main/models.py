from django.db import models

# Create your models here.
""""`__str__()` method Student model mein is liye use kiya hai taake Django mein Student object ka naam readable form mein show ho.
Ye student ka `name` return karta hai, is liye Admin mein “Student object” ki jagah student ka naam nazar aata hai.
Student ke naam par click karne se us student ka complete record, jaise email aur age, dekh sakte hain.
"""
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
    

    