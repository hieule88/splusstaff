from django.db import models
from splus.models import Drink

# Create your models here.


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    floor = models.IntegerField(default=1)
