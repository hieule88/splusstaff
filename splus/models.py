from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(default='', max_length=256)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)

SIZE_CHOICE = (
    ("S", "S"),
    ("M", "M"),
    ("L", "L")
)
class Drink(models.Model):
    title = models.CharField(default='', max_length=256)
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(default='M', choices=SIZE_CHOICE, max_length=20)
    price = models.IntegerField()
    active = models.BooleanField(default=True)

