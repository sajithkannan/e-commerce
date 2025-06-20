from django.db import models
from product_management.models import product
from user_management_system.models import CustomUser


# Create your models here.
class payment(models.Model):
  product = models.ForeignKey(product, on_delete=models.CASCADE)
  customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  payment_method = models.CharField( max_length=50)
  amount = models.DecimalField(max_digits=5, decimal_places=2)
  payment_date = models.DateField( auto_now=False, auto_now_add=False)
  payment_status = models.CharField( max_length=50)
  transaction_id = models.CharField( max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
