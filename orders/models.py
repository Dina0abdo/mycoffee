from django.db import models
from django.contrib.auth.models import User
from shops.models import Shop
from datetime import datetime
from django.utils import timezone

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    details = models.ManyToManyField(Shop, through="order_details")
    is_finished = models.BooleanField()

    def __str__(self):
        return 'User: ' + self.user.username + '; Order ID: ' + str(self.id)


class order_details(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return 'User:  ' + self.order.user.username + '; Product: ' + self.shop.name + '; Order ID: ' + str(self.order.id)

    class Meta:
        ordering = ['-id']
