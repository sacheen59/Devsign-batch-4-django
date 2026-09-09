from django import forms

from userpage.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address','phone_number','quantity', 'payment_method',]
