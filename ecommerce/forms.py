from django import forms

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer_name', 'product_name', 'quantity', 'order_date')
        
    