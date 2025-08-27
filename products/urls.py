from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductImageViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(r"product-images", ProductImageViewSet, basename="product-images")

urlpatterns = router.urls
