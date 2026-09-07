from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name="homepage"),
    path('all-products/',views.all_products, name="productpage"),
    path('product/<int:pk>/', views.product_detail, name="product-detail"),
    path('my-cart/', views.cart_page, name="cart-page"),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name="add-to-cart"),
    path('delete-cart-item/<int:cart_id>/', views.delete_cart_item, name="delete-cart-item")
]