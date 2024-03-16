
from django.urls import path
from category.views import list_category, add_category

urlpatterns = [
    path('', list_category, name="list_category"),
    path('add', add_category, name="add_category")
]
