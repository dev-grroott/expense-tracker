
from django.urls import path
from category.views import list_category, add_category, edit_category, delete_category

urlpatterns = [
    path('', list_category, name="list_category"),
    path('add/', add_category, name="add_category"),
    path('edit/<id>/', edit_category, name="edit_category"),
    path('delete/<id>/', delete_category, name="delete_category"),
]
