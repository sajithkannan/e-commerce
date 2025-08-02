from django.db import models
from product_management.models import product
from user_management_system.models import CustomUser

class payment(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    
    amount = models.DecimalField(max_digits=7, decimal_places=2)  # increased max_digits in case amount > 999.99
    
    discount_percentage = models.IntegerField(default=0)  # ✅ No max_length, with default
    
    payment_date = models.DateField(auto_now=False, auto_now_add=False)
    
    alternative_number = models.CharField(max_length=15, default='0000000000')  # ✅ Default added to avoid migration issues
    
    payment_status = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)