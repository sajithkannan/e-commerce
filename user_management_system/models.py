from django.contrib.auth.models import AbstractUser, Group,Permission,PermissionsMixin,BaseUserManager
from django.db import models


class CustomUserManager( BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)



class CustomUser(AbstractUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    role = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Provide unique related_name for groups
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Provide unique related_name for permissions
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )


class Customer(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=False,blank=False)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, default='0000000000')
    alternative_number = models.CharField(max_length=15, default='0000000000')
    gender = models.CharField(max_length=6)
    postal_code = models.IntegerField(6)
    address = models.TextField(max_length=255)
    land_mark = models.TextField(max_length=255)
    country = models.CharField(max_length=50, default=None)
    state = models.CharField(max_length=50, default=None)
    city = models.CharField(max_length=50, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Seller(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=30, default=None)
    business_address = models.TextField(max_length=255, default=None)
    gst_number = models.CharField(max_length=15, default=None)
    # postal_code = models.IntegerField(6, default=0)
    # phone_number = models.CharField(max_length=15, default=None)
    # country = models.CharField(max_length=50, default=None)
    # state = models.CharField(max_length=50, default=None)
    # city = models.CharField(max_length=50, default=None)
    status = models.CharField(max_length=15, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
