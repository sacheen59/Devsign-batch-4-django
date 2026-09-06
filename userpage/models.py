from django.db import models
from product.models import Product
from django.contrib.auth.models import User

# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.product_name}"
