from django.shortcuts import render
from product.models import Product

# Create your views here.

def homepage(request):
    products = Product.objects.all().order_by("-id")[:8]
    return render(request, "userpage/homepage.html", {
        "products": products
    })

def all_products(request):
    products = Product.objects.all()
    return render(request, "userpage/products.html", {
        "products": products
    })

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "userpage/product-detail.html", {
        "product": product
    })