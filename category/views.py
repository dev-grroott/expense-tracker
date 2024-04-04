from django.shortcuts import render, redirect
from category.models import Category
from category.forms import CategoryForm

def home(request):
    return render(request, "category/home.html")


def list_category(request):

    data = Category.objects.all() # select * from category;

    return render(request, "category/category.html", context={"categories": data})

def add_category(request):

    if request.method == "GET":
        form = CategoryForm()

        return render(request, "category/add_category.html", context={"form": form})
    elif request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            print("Form error", form.errors)

        return redirect("list_category")
        
def edit_category(request, id):

    category = Category.objects.get(id=id)   # select * from category where id=1

    if request.method == "GET":
        form = CategoryForm(instance=category)

        return render(request, "category/edit_category.html", context={"form": form})
    elif request.method == "POST":
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
        else:
            print("Form error", form.errors)

        return redirect("list_category")
    
def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()

    return redirect("list_category")