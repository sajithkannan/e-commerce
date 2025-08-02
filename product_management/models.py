from django.db import models
from user_management_system.models import CustomUser
import datetime
import os

# Create your models here.
class product(models.Model):
  product_category = models.CharField(max_length=20)
  seller = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
  product_name = models.CharField(max_length=20)
  product_description = models.TextField()
  price = models.IntegerField()
  stock = models.IntegerField()
  image = models.ImageField()
  manufacture_date = models.DateField()
  expiry_date = models.DateField()
  is_expired = models.BooleanField()
  discount_percentage = models.IntegerField(default=0)
  trending=models.BooleanField(default=False,help_text="0-Default,1-Trending")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


