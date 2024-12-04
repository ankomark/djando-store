from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    Category, Product, UserProfile, Cart, CartItem, Order, OrderItem, ProductReview, Rating, Payment
)
from .serializers import (
    CategorySerializer, ProductSerializer, UserProfileSerializer, CartSerializer, CartItemSerializer,
    OrderSerializer, OrderItemSerializer, ProductReviewSerializer, RatingSerializer, PaymentSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = self.queryset
        category_id = self.request.query_params.get('category_id')

        if category_id:
            try:
                # Attempt to convert to int, handle case where category_id is not a number
                category_id = int(category_id)
                queryset = queryset.filter(category_id=category_id)
            except ValueError:
                # Handle the case where conversion fails
                pass  # Or return an appropriate response

        return queryset

    @action(detail=True, methods=['post'])
    def decrease_stock(self, request, pk=None):
        product = self.get_object()
        quantity = int(request.data.get('quantity', 1))
        if product.decrease_stock(quantity):
            return Response({"message": "Stock updated"}, status=status.HTTP_200_OK)
        return Response({"message": "Insufficient stock"}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        product = Product.objects.get(pk=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()
        return Response({"message": "Product added to cart"}, status=status.HTTP_200_OK)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

@api_view(['POST'])
def rate_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    rating_value = request.data.get('rating')
    if rating_value is None:
        return Response({"error": "Rating is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Assuming you have a Rating model defined that takes product and rating as fields
    rating = Rating.objects.create(product=product, rating=rating_value)
    rating.save()

    return Response({"message": "Rating submitted"}, status=status.HTTP_201_CREATED)



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
