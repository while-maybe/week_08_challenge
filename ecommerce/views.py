from django.shortcuts import render, redirect, get_object_or_404

from .forms import OrderForm
from .models import Order

# Create your views here.

# '/' forwarder
def forwarder(request):
    return redirect('ecommerce:order_list')

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
            # form['order_date'] = form['order_date'].strftime('%Y-%m-%d')
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
        form = OrderForm(data=request.POST, instance=order)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('ecommerce:order_list')
    else:
        form = OrderForm(instance=order)

    context = {'form': form, 'order': order}
    return render(request, 'ecommerce/order_edit.html', context)

# Delete order
def order_confirm_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    if request.method == "POST":
        order.delete()
        return redirect("ecommerce:order_list")
    
    context = {'order': order}
    return render(request, 'ecommerce/order_confirm_delete.html', context)

