from django.urls import path
from .import  views


urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('product_detail/<slug:slug>/', views.product_detail, name='product_detail'),
    path('categoty_list/', views.category_list, name='category_list'),
    path('category_detail/<slug:slug>/', views.category_detail, name='category_detail')     
]

