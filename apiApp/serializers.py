from rest_framework import serializers
from .models import Product,Category,Cart,CartItem,Review,Wishlist
from django.contrib.auth import get_user_model
User = get_user_model()

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','slug','price','image']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','slug', 'description','price','image']        

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','image','slug']        

class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id','name','image']   

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only = True)
    sub_total = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'sub_total']

    def get_sub_total(self,cartitem):
        total = cartitem.product.price * cartitem.quantity
        return total
        

class CartSerializer(serializers.ModelSerializer):
    cartitems = CartItemSerializer(read_only=True, many=True)
    cart_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'cart_code', 'cartitems', 'cart_total']    

    def get_cart_total(self, obj):  
        total = sum([item.quantity * item.product.price for item in obj.cartitems.all()])
        return total

        
class CartStatSerializer(serializers.ModelSerializer):
    total_quantity = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ['id', 'cart_code', 'total_quantity']    

    def get_total_quantity(self,cart):
        items = cart.cart_items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total    
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'profile_picture_url']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'ratings', 'review', 'created', 'updated', 'user']


class WishlistSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only= True)
    product= ProductListSerializer(read_only=True)
    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'product', 'created']
        
             