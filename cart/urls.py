from django.urls import path
from . import views

urlpatterns = [
    path('api/cart/<int:id>', views.cart_detail, name='cart_detail'),
    path('api/cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('api/cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]
