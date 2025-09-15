from django.contrib import admin
from .models import Product, Category, Cart, CartItem,Review,ProductRating,Wishlist,Order,OrderItem
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'featured')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register([Cart, CartItem,Review,ProductRating,Wishlist,Order,OrderItem])
