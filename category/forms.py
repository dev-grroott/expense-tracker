from django import forms

from category.models import Category

class CategoryForm(forms.ModelForm):

    name = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            {
                "class": "form-control",
                "placeholder": "Enter category name"
            }
        )
    )

    class Meta:
        model = Category
        fields = ["name"]    # "__all__"
    