from django.urls import path
from . import views
urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),

    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('shop_fav/<int:pro_id>', views.shop_fav, name="shop_fav"),
    path('show_shop_fav', views.show_shop_fav, name='show_shop_fav'),



]
