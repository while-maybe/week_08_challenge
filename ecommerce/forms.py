from django import forms
from django.forms.widgets import DateInput

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'product_name', 'quantity', 'order_date']

    def clean_customer_name(self):
        customer_name = self.cleaned_data.get('customer_name')
        customer_name = customer_name.strip().title()
        return customer_name

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name').title()
        product_name = product_name.strip()
        return product_name
