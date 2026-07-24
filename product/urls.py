from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.index,name="test"),
    path('second-test/', views.second_test),
    path('list/', views.product_list, name="list"),
    path('category-list/',views.get_all_categories, name="category_list"),
    path('add-category/',views.add_category, name="add_category"),
    path('delete-category/<int:category_id>/', views.delete_category, name="delete_category"),
    path('edit-category/<int:category_id>/', views.edit_category, name="edit_category"),
]

# localhost:8000/delete-category/
#