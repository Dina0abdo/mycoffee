from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('services', views.services, name='serivces'),
    path('blog', views.blog, name='blog'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('content', views.content, name='content'),
    path('cart', views.cart, name='cart'),

    path('checkout', views.checkout, name='checkout'),





]
