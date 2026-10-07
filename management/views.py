from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required, permission_required

from .forms import ProductForm

from .models import Product


# Create your views here.


def student_view(request):

    return render(request, "management/student.html")


def profile_view(request):

    return render(request, "management/profile.html")


def department_view(request):

    return render(request, "management/department.html")


def teacher_view(request):

    return render(request, "management/teacher.html")


def course_view(request):

    return render(request, "management/course.html")


@login_required
@permission_required("management.add_product")
def add_product(request):

    if request.method == "POST":

        form = ProductForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("product_list")

    else:

        form = ProductForm()

    return render(
        request,
        "management/add_product.html",
        {"form": form}
    )


@login_required
@permission_required("management.view_product")
def product_list(request):

    products = Product.objects.all()

    return render(
        request,
        "management/product_list.html",
        {"products": products}
    )


@login_required
@permission_required("management.change_product")
def edit_product(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            instance=product
        )

        if form.is_valid():

            form.save()

            return redirect("product_list")

    else:

        form = ProductForm(
            instance=product
        )

    return render(
        request,
        "management/edit_product.html",
        {
            "form": form,
            "product": product
        }
    )