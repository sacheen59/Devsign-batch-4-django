from django.db import models
from product.models import Product
from django.contrib.auth.models import User

# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.product_name}"


class Order(models.Model):
    PAYMENT_METHOD = (
        ('cash', 'Cash On Delivery'),
        ('esewa', 'Esewa'),
        ('khalti', 'Khalti')
    )
    DELIVERY_STATUS = (
        ('pending', 'Pending'),
        ('way', 'On your Way'),
        ('delivered', 'Delivered')
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField(default=1)
    payment_method = models.CharField(choices=PAYMENT_METHOD, default='cash')
    delivery_status = models.CharField(choices=DELIVERY_STATUS, default='pending')

    def __str__(self):
        return f"{self.user.username} - order - {self.product.product_name}"

