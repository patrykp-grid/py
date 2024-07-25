from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Pizza, Order
from django.shortcuts import get_object_or_404
from .decorators import admin_required
import json

def list_menu(request):
    pizzas = Pizza.objects.all()
    menu = [{"id": pizza.id, "name": pizza.name, "description": pizza.description, "price": pizza.price} for pizza in pizzas]
    return JsonResponse(menu, safe=False)

def create_order(request):
    data = json.loads(request.body)
    pizza_id = data.get("pizza_id")
    address = data.get("address")
    pizza = Pizza.objects.get(id=pizza_id)
    order = Order.objects.create(pizza=pizza, address=address)
    return JsonResponse({"order_id": order.id})

# @require_http_methods(["GET"])
# def check_order_status(request, order_id):
#     order = Order.objects.get(id=order_id)
#     return JsonResponse({"status": order.status})

def order_view(request, order_id):
    if request.method == 'GET':
        order = get_object_or_404(Order, id=order_id)
        return JsonResponse({"status": order.status})

    elif request.method == 'DELETE':
        order = get_object_or_404(Order, id=order_id)
        if order.status != 'delivered':
            order.status = 'cancelled'
            order.save()
            return JsonResponse({"message": "Order cancelled"})
        else:
            return JsonResponse({"message": "Cannot cancel a delivered order"}, status=400)

    return JsonResponse({"message": "Method not allowed"}, status=405)
    
@admin_required
def add_pizza(request):
    data = json.loads(request.body)
    pizza = Pizza.objects.create(name=data['name'], description=data['description'], price=data['price'])
    return JsonResponse({"message": "Pizza added", "pizza_id": pizza.id})
