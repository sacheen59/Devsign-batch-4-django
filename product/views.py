from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

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
        "categories": categories
    })