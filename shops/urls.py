from django.urls import path
from . import views
urlpatterns = [
    path('shops', views.shops, name='shops'),
    path('search', views.search, name='search'),




    path('<int:pro_id>', views.product_single, name='product_single'),
]
