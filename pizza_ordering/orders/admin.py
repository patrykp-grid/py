from django.contrib import admin
from .models import Pizza, Order

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    search_fields = ('name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'pizza', 'address', 'status', 'created_at')
    list_filter = ('status', 'pizza')
    search_fields = ('address',)