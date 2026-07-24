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

    # field level validation
    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')
        if Category.objects.filter(category_name=category_name).exists():
            raise forms.ValidationError("The category name already exists.")
        if len(category_name) < 3:
            raise forms.ValidationError("The category name must be greater than 3 characters")
        return category_name

    def clean_description(self):
        # extract the description
        description = self.cleaned_data.get("description")
        # check whether it is more than 10 character or not
        if len(description) < 10:
            raise forms.ValidationError("The description must be more than 10 characters")
        return description

    def clean(self):
        category_name = self.cleaned_data.get("category_name")
        description = self.cleaned_data.get("description")
        if category_name == description:
            raise forms.ValidationError("Category name and Description must not be same.")
        return super().clean()


class EditCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['category_name']

    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')
        if Category.objects.filter(category_name=category_name).exists():
            raise forms.ValidationError("The category name already exists.")
        if len(category_name) < 3:
            raise forms.ValidationError("The category name must be greater than 3 characters")
        return category_name