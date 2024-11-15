from django.shortcuts import render

from .forms import OrderForm
from .models import Order

# Create your views here.

# list orders
def order_list(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'ecommerce/order_list.html', context)

# Create order
def order_new(request):
    pass

# Edit order
def order_edit(request):
    pass

# Delete order
def order_delete(request):
    pass
