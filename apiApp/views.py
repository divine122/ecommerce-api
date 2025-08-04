from django.shortcuts import render
from .models import Category,Product
from rest_framework.decorators import api_view
from .serializers import ProductListSerializer, CategoryDetailSerializer,ProductDetailSerializer,CategoryListSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def product_list(request):
    products = Product.objects.filter(featured=True)
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request,slug):
    product = Product.objects.get(slug=slug)
    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_detail(request,slug):
    category = Category.objects.get(slug=slug) 
    serializer = CategoryDetailSerializer(category)
    return Response(serializer.data)