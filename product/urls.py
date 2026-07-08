from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.index,name="test"),
    path('second-test/', views.second_test),
    path('list/', views.product_list, name="list"),
    path('category-list/',views.get_all_categories, name="category_list")
]