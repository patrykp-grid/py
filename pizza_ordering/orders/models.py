from django.db import models
from django.contrib.auth.models import User

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('ready', 'Ready to be delivered'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)