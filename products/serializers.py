from rest_framework import serializers
from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image"]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    # afaka mampiasa upload amin'ny fotoana iray koa
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "slug",
            "price",
            "stock",
            "is_active",
            "category",
            "subcategory",
            "images",
            "uploaded_images",
        ]
        read_only_fields = ["slug"]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])
        product = super().create(validated_data)
        for image in uploaded_images[:8]:  # max 8 images
            ProductImage.objects.create(product=product, image=image)
        return product

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])
        product = super().update(instance, validated_data)
        for image in uploaded_images[:8]:
            ProductImage.objects.create(product=product, image=image)
        return product
