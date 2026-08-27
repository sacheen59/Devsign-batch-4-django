from django.shortcuts import render
from product.models import Product

# Create your views here.

def homepage(request):
    products = Product.objects.all().order_by("-id")[:8]
    return render(request, "userpage/homepage.html", {
        "products": products
    })