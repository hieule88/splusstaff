from django.shortcuts import render
from rest_framework.decorators import api_view
from .backend import get_cart_data
# Create your views here.


@api_view(['GET'])
def cartview(request):
    cart_items = get_cart_data()

    context = {
        "items": cart_items,
    }

    return render(request, "cart.html", context=context)
