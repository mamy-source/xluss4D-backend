from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(read_only=True)
    total_price = serializers.FloatField(read_only=True)


    class Meta:
        model =Product
        fields = ['id','name','price','quantity']