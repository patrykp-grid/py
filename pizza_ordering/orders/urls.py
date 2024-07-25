from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.list_menu, name='list_menu'),
    path('order/', views.create_order, name='create_order'),
    path('order/<int:order_id>/', views.order_view, name='order_view'),
    path('menu/add/', views.add_pizza, name='add_pizza'),
]