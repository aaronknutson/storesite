from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('my-account/', views.my_account, name='my_account'),
    path('product-detail', views.product_detail, name='product_detail'),
    path('product-list', views.product_list, name='product_list'),
    path('wishlist', views.wishlist, name='wishlist'),
]
