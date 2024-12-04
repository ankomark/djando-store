from django.contrib import admin
from .models import Product,Rating,Payment, Order,OrderItem,Cart,CartItem, ProductReview,Category,UserProfile

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ProductReview)
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderItem)
admin.site.register(Rating)
admin.site.register(Payment)

