"""Define URL patterns for the tasks"""

from django.urls import path
# from django.views.generic import RedirectView

from . import views

app_name = 'ecommerce'

urlpatterns = [
    # path('', RedirectView.as_view(pattern_name='order_list')),
    path('orders/', views.order_list, name='order_list'), # URL to list tasks
    path('order/delete/<int:order_id>/', views.order_delete, name='order_delete'),
    path('order/edit/<int:order_id>/', views.order_edit, name='order_edit'),
    path('order/new/', views.order_new, name='order_new'),
]