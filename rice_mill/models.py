from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, related_name="branch_name", blank=True, null=True)
    is_superuser = models.BooleanField(default=False)

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_name_bn = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    updated_by = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.customer_name
