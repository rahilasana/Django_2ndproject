from django import forms


# Student search form
class StudentSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Student Name"
    )


# Teacher search form
class TeacherSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Teacher Name"
    )


# Department search form
class DepartmentSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Department Name"
    )