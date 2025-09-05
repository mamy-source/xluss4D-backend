from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
from categories.views import CategoryViewSet, SubCategoryViewSet
# from cart.views import CartViewSet
# from orders.views import OrderViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"subcategories", SubCategoryViewSet, basename="subcategory")
# router.register(r"cart", CartViewSet, basename="cart")
# router.register(r"orders", OrderViewSet, basename="order")

urlpatterns = [
    path('api/', include('cart.urls')),
    path("api/", include(router.urls)),
]