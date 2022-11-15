#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatbot.settings")
import django
django.setup()
from splus.models import *
from cart.models import *


def update_cart():
    pass

def update_cartitem():
    pass

def update_drink(data, active=True):
    title, description, category, size, price = data
    context = Drink()
    context.title = title 
    context.description = description
    context.category = Category.objects.get(title=category)
    context.size = size
    context.price = price
    context.active = active
    context.save()

def update_category():
    pass


def main():
    """Run administrative tasks."""
    fruit = [
        ('coconut', 'Dừa trái', 'fruit', 'L', 45),
        ('pineapple', 'Ép dứa', 'fruit', 'L', 45),
        ('avocadosmoothie', 'Sinh tố bơ', 'fruit', 'L', 59),
        ('orange', 'Cam nguyên chất', 'fruit', 'L', 65),
    ]

    specialtea = [
        ('lotustea', 'Trà sen lá nếp', 'specialtea', 'M', 49), 
        ('peachytea', 'Trà đào cam sả', 'specialtea', 'M', 49),
        ('lycheetea', 'Oolong vải trà', 'specialtea', 'M', 49),
        ('grapefruittea', 'Trà bưởi hồng', 'specialtea', 'M', 49),
        ('honeykumquat', 'Trà quất mật ong', 'specialtea', 'M', 49),
        ('chamomileappletea', 'Trà hoa cúc táo xanh', 'specialtea', 'M', 49),
        ('lotustea', 'Trà sen lá nếp', 'specialtea', 'L', 55), 
        ('peachytea', 'Trà đào cam sả', 'specialtea', 'L', 55),
        ('lycheetea', 'Oolong vải trà', 'specialtea', 'L', 55),
        ('grapefruittea', 'Trà bưởi hồng', 'specialtea', 'L', 55),
        ('honeykumquat', 'Trà quất mật ong', 'specialtea', 'L', 55),
        ('chamomileappletea', 'Trà hoa cúc táo xanh', 'specialtea', 'L', 55),
    ]

    ice_blended = [
        ('greenteajelly', 'Thạch matcha', 'ice_blended', 'M', 55), 
        ('almondchocolate', 'Sô-cô-la hạnh nhân', 'ice_blended', 'M', 55), 
        ('saltedcaramel', 'Caramel mặn', 'ice_blended', 'M', 55), 
        ('blueberryyogurt', 'Sữa chua việt quất', 'ice_blended', 'M', 55), 
        ('greenteajelly', 'Thạch matcha', 'ice_blended', 'L', 65), 
        ('almondchocolate', 'Sô-cô-la hạnh nhân', 'ice_blended', 'L', 65), 
        ('saltedcaramel', 'Caramel mặn', 'ice_blended', 'L', 65), 
        ('blueberryyogurt', 'Sữa chua việt quất', 'ice_blended', 'L', 65), 

    ]

    signature = [
        ('sunshine', 'Nước ép dứa, mít, nha đam', 'signature', 'L', 69), 
        ('supergreen', 'Sinh tố bưa sữa dừa hạnh nhân', 'signature', 'L', 69), 
    ]


    espresso = [
        ('espresso', 'espresso', 'espresso', 'M', 39), 
        ('americano', 'americano', 'espresso', 'M', 39), 
        ('cafelatte', 'cafelatte', 'espresso', 'M', 50), 
        ('cappuccino', 'cappuccino', 'espresso', 'M', 50), 
        ('cafemocha', 'cafemocha', 'espresso', 'M', 59), 
        ('espresso', 'espresso', 'espresso', 'L', 45), 
        ('americano', 'americano', 'espresso', 'L', 45), 
        ('cafelatte', 'cafelatte', 'espresso', 'L', 59), 
        ('cappuccino', 'cappuccino', 'espresso', 'L', 59), 
        ('cafemocha', 'cafemocha', 'espresso', 'L', 69), 
    ]

    categories = [signature, espresso]

    for category in categories:
        for item in category:
            update_drink(item)



if __name__ == "__main__":
    main()
