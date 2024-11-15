from django.contrib import admin

from .models import Order

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'product_name', 'quantity', 'order_date']
    list_filter = ['customer_name', 'product_name', 'order_date']
    show_facets = admin.ShowFacets.ALWAYS
    
# admin.site.register(Order)
