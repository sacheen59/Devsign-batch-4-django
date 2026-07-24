from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Category
from .forms import CategoryForm,EditCategoryForm

# Create your views here.

# MVT => Model, View and Templates
# Model => data or databases
# Views => businesss logic
# Templates => html file or UI

# views => function based views and class based views
# function based views

def index(request):
    # data = {
    #     "name": "Dipesh Kharel",
    #     "age": 21,
    #     "course": "Python with django"
    # }
    student_info = [
    {
        "name": "Ram",
        "marks": {
            "math": 90,
            "social": 20,
            "english": 40,
        },
        "is_active": True
    },
    {
        "name": "Hari",
        "marks": {
            "math": 85,
            "social": 45,
            "english": 35,
        },
        "is_active": False
    },
    {
        "name": "Geeta",
        "marks": {
            "math": 55,
            "social": 58,
            "english": 29,
        },
        "is_active": True
    },
    {
        "name": "Sita",
        "marks": {
            "math": 56,
            "social": 86,
            "english": 49,
        },
        "is_active": False
    },
]
    return render(request, "product/index.html", {
        "infos": student_info
    })

def second_test(request):
    return HttpResponse("This is second test page.")

def product_list(request):
    products = [
        {
            "id": 1,
            "product_name": "Mobile Phone",
            "product_price": 120000,
            "is_available": True,
            "image_url": "https://m.media-amazon.com/images/I/41cslOLNecL._SY300_SX300_QL70_FMwebp_.jpg"
        },
        {
            "id": 2,
            "product_name": "TV",
            "product_price": 45000,
            "is_available": False,
            "image_url": "https://m.media-amazon.com/images/I/81qtWbsLU4L._SX679_.jpg"
        },
        {
            "id": 3,
            "product_name": "Laptop",
            "product_price": 120000,
            "is_available": True,
            "image_url": "https://m.media-amazon.com/images/I/717WZ7WriwL._SX679_.jpg"
        }
    ]
    return render(request, "product/list.html",{
        "products": products
    })


def get_all_categories(request):
    categories = Category.objects.all()
    return render(request, "product/category_list.html",{
        "categories": categories,
        "is_empty": len(categories) <= 0
    })

def add_category(request):
    # if request.method == "POST":
    #     category_name = request.POST.get('category_name')
    #     category = Category.objects.create(category_name=category_name)
    #     category.save()
    #     return redirect("category_list")
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm()
    return render(request, "product/add_category.html", {
        "form": form
    })

def delete_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return HttpResponse("The product with this category id doesnot exists")
    category.delete()
    return redirect("category_list")


# localhost:8000/product/delete-category/1

# Edit catgory
def edit_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = EditCategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = EditCategoryForm(instance=category)
    return render(request, 'product/edit_category_form.html', {
         'form': form
        })