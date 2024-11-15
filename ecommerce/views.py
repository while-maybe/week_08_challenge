from django.shortcuts import render, redirect, get_object_or_404

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
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ecommerce:order_list')
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, 'ecommerce/order_edit.html', context)

# Edit order
def order_edit(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('ecommerce:order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'ecommerce/order_edit.html', {'form': form})

# Delete order
def order_delete(request):
    pass
