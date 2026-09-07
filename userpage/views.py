from django.shortcuts import render,redirect
from product.models import Product
from django.contrib.auth.decorators import login_required
from accounts.auth import user_only
from .models import CartItem
from django.contrib import messages

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

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "userpage/product-detail.html", {
        "product": product
    })


@login_required
@user_only
def add_to_cart(request,product_id):
    product = Product.objects.get(id = product_id)
    user = request.user
    presence_in_cart = CartItem.objects.filter(product=product, user = user)
    if not presence_in_cart:
        cart = CartItem.objects.create(
            product=product,
            user=user
        )
        cart.save()
    else:
        messages.warning(request, "Item already added to cart.")
        return redirect(product)
    return redirect("cart-page")


@login_required
@user_only
def cart_page(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, "userpage/cart.html",{
        "cart_items": cart_items,
        "is_empty": len(cart_items) <= 0
    })

@login_required
@user_only
def delete_cart_item(request, cart_id):
    cart_item = CartItem.objects.get(id=cart_id)
    cart_item.delete()
    return redirect('cart-page')