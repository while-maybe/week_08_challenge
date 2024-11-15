from django.db import models
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    order_date = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['-order_date']
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return f"{self.customer_name} ordered {self.quantity}X {self.product_name} on {self.order_date}"
