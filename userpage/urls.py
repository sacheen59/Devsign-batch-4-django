from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name="homepage"),
    path('all-products/',views.all_products, name="productpage"),
    path('product/<int:product_id>/', views.product_detail, name="product-detail")
]