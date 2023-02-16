from django.db import models
from django.contrib.auth.models import User
from shops.models import Shop
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_fav = models.ManyToManyField(Shop)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_number = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
