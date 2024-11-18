from django import forms
from django.forms.widgets import DateInput

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'product_name', 'quantity', 'order_date']
        # widgets = {
        #     'date_field': DateInput(
        #         attrs={
        #             'type': 'date',
        #             'class': 'form-control',
        #             # needed to send correct date format to html 5
        #             'data-date-format': 'yyyy-mm-dd'
        #         }
        #     )
        # }
        
    