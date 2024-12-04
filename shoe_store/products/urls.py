from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet,CartViewSet,RatingViewSet,PaymentViewSet,OrderItemViewSet,CategoryViewSet,UserProfileViewSet,CartItemViewSet,ProductReviewViewSet
from .views import ProductViewSet, rate_product
# Initialize router
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)  # Handle product listing
router.register(r'orders', OrderViewSet)
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'carts', CartViewSet)
router.register(r'Rating', RatingViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'order_items', OrderItemViewSet)
router.register(r'product_reviews', ProductReviewViewSet)
router.register(r'cart_items', CartItemViewSet)  # Handle cart item listing



urlpatterns = [
    # Automatically include the URL routes from the router
    path('api/', include(router.urls)),
    path('products/api/products/<int:product_id>/rate/', rate_product, name='rate_product'),
]
