import base64
import json
import uuid

from django.shortcuts import render,redirect
from django.urls import reverse
from product.models import Product
from django.contrib.auth.decorators import login_required
from accounts.auth import user_only
from .models import CartItem,Order
from django.contrib import messages
from .forms import OrderForm

from utils.signature import generate_signature

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


@login_required
@user_only
def order_now(request,product_id):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        product = Product.objects.get(id=product_id)
        user = request.user
        cart_items = CartItem.objects.filter(product=product, user=user)
        cart = cart_items.first()
        if form.is_valid():
            data = form.cleaned_data
            address = data['address']
            phone_number = data['phone_number']
            quantity = data['quantity']
            payment_method = data['payment_method']
            total_price = int(product.product_price * quantity)
            order = Order.objects.create(
                user=user,
                product=product,
                total_price=total_price,
                address=address,
                phone_number=phone_number,
                quantity=quantity,
                payment_method=payment_method,
                delivery_status='pending'
            )
            if payment_method == "esewa":
                cart_id = cart.id if cart else 0
                return redirect(reverse('esewa_form')+"?o_id="+str(order.id)+"&c_id="+str(cart_id))
            order.save()
            cart_items.delete()
            return redirect("homepage")
    else:
        form = OrderForm()
    return render(request, "userpage/order_form.html",{
        'form': form
    })



def esewa_view(request):
    o_id = request.GET.get('o_id')
    c_id = request.GET.get('c_id')
    cart = CartItem.objects.filter(id=c_id).first() if c_id else None
    order = Order.objects.get(id=o_id)

    uuid_val = uuid.uuid4()
    secret_key = "8gBm/:&EnhH.1/q"
    data_to_sign = f"total_amount={order.total_price},transaction_uuid={uuid_val},product_code=EPAYTEST"
    signature = generate_signature(secret_key, data_to_sign)
    data = {
            'amount': order.product.product_price,
            'total_amount': order.total_price,
            'transaction_uuid': uuid_val,
            'product_code': 'EPAYTEST',
            'signature': signature
    }
    return render(request,"userpage/esewaform.html",{
            'order':order,
            'cart': cart,
            'data': data
        })


@login_required
def esewa_verify(request,order_id, cart_id):
    data = request.GET.get('data')
    decoded_data = base64.b64decode(data).decode('utf-8')
    map_data = json.loads(decoded_data)
    order = Order.objects.get(id=order_id)
    cart = CartItem.objects.filter(id=cart_id).first()

    if map_data.get('status') == 'COMPLETE':
        order.payment_status = 'paid'
        order.save()
        if cart:
            cart.delete()

    return redirect('cart-page')