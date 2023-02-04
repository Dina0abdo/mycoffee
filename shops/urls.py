from django.urls import path
from . import views
urlpatterns = [
    path('', views.shops, name='shops'),
    path('product_single', views.product_single, name='product_single'),
]
