from django import forms
from django.core.exceptions import ValidationError
from .models import Category

# there are two type of forms in django
# Form => each field should be defined by us
# ModelForm => Form is generated on the basis of model that we defined

# normal form
# class CategoryForm(forms.Form):
#     category_name = forms.CharField(max_length=200, required=True, label="Name of Category")

# model form

# form validation in django
# field level validation => validating each individual field
# clean_<field_name>(self)
# object level validation => validating between two or more fields

class CategoryForm(forms.ModelForm):
    # price = forms.IntegerField()

    class Meta:
        model = Category
        fields = ["category_name","description"]
        # fields = "__all__"
        # exclude = ["description"]

    # field level validation
    def clean_category_name(self):
        # extract the category_name
        category_name = self.cleaned_data.get('category_name')
        # check whether the category name already exists in db or not
        if len(category_name) < 3:
            raise forms.ValidationError("Category name must be more than 3 characters")
        # if yes show validation
        # else return the category_name
        return category_name

# {'category_name' : value}