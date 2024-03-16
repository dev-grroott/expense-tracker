from django.shortcuts import render
from category.models import Category
from category.forms import CategoryForm

def home(request):
    return render(request, "category/home.html")


def list_category(request):

    data = Category.objects.all()

    return render(request, "category/category.html", context={"categories": data})

def add_category(request):

    if request.method == "GET":
        form = CategoryForm()

        return render(request, "category/add_category.html", context={"form": form})
    elif request.method == "POST":
        pass