from django.urls import path
from .import  views


urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('product_detail/<slug:slug>/', views.product_detail, name='product_detail'),
    path('categoty_list/', views.category_list, name='category_list'),
    path('category_detail/<slug:slug>/', views.category_detail, name='category_detail'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('update_cartitem_quantity/', views.update_cartitem_quantity, name='update_cartitem_quantity'),
    path('add_review/', views.add_review, name='add_review'),
    path('update_review/<int:pk>/', views.update_review, name='update_review'),
    path('delete_review/<int:pk>/', views.delete_review, name='delete_review'),
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('delete_cartitem/<int:pk>/', views.delete_cartitem, name='delete_cartitem'),
    path('search/', views.product_search, name='search'),
    path('create_checkout_session/', views.create_checkout_session, name='create_checkout_session'),
    path('webhook/', views.my_webhook_view, name='webhook'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_cancel/',views.payment_cancel, name='payment_cancel')
]

