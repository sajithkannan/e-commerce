from django.db import models
from product_management.models import product
from user_management_system.models import CustomUser
from payment_system.models import payment

class cart_item(models.Model):
  payment = models.ForeignKey(payment, on_delete=models.CASCADE)
  customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  product_id = models.ForeignKey(product, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class order_details(models.Model):
  cart_item = models.ForeignKey(cart_item, on_delete=models.CASCADE)
  order_date = models.DateField()
  status = models.CharField(max_length=50)
  total_amount = models.DecimalField(max_digits=5, decimal_places=2)
  payment_status = models.CharField(max_length=50)
  shipping_address = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


