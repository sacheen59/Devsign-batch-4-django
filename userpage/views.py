from django.shortcuts import render,redirect
from product.models import Product
from django.contrib.auth.decorators import login_required
from accounts.auth import user_only
from .models import CartItem

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


@login_required
@user_only
def add_to_cart(request,product_id):
    product = Product.objects.get(id = product_id)
    user = request.user
    cart = CartItem.objects.create(
        product=product,
        user=user
    )
    cart.save()
    return redirect("cart-page")


@login_required
@user_only
def cart_page(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, "userpage/cart.html",{
        "cart_items": cart_items
    })