from django import forms
from .models import Category

# there are two type of forms in django
# Form => each field should be defined by us
# ModelForm => Form is generated on the basis of model that we defined

# normal form
# class CategoryForm(forms.Form):
#     category_name = forms.CharField(max_length=200, required=True, label="Name of Category")

# model form

class CategoryForm(forms.ModelForm):
    # price = forms.IntegerField()

    class Meta:
        model = Category
        fields = ["category_name","description"]
        # fields = "__all__"
        # exclude = ["description"]


# {'category_name' : value}