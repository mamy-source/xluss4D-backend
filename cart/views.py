from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def cart_detail(request, id):
    # id = request.get("id")
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        items.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "quantity": quantity,
            "subtotal": subtotal
        })
        total += subtotal

    return Response({"cart": items, "total": total , "id":id})


@api_view(['POST'])
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return Response({"message": "Produit ajouté au panier"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return Response({"message": "Produit retiré du panier"}, status=status.HTTP_200_OK)
