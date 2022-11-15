from django.contrib import admin
from .models import *
from cart.models import *

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('title',)

admin.site.register(Category, CategoryAdmin)

class DrinkAdmin(admin.ModelAdmin):
    model = Drink
    list_display = ('title', 'size')

admin.site.register(Drink, DrinkAdmin)

class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('created_at',)

admin.site.register(Cart, CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    model = CartItem
    list_display = ('item', 'quantity')

admin.site.register(CartItem, CartItemAdmin)