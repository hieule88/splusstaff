from django.shortcuts import render
from rest_framework.decorators import api_view
from .backend import get_cart_data
from django.http import HttpResponse
# Create your views here.

dict_drinkimg = {

}

@api_view(['GET'])
def cartview(request):
    cart_items = get_cart_data()

    title = request.GET.get('title') if request.GET.get('title') != None else '' 
    size = request.GET.get('size') if request.GET.get('size') != None else ''
    quantity = request.GET.get('quantity') if request.GET.get('quantity') != None else ''
    floor = request.GET.get('floor') if request.GET.get('floor') != None else ''

    cart_items = [
        [
            title, 
            size,
            quantity,
            floor,
        ],
    ]
    
    context = {
        "items": cart_items,
        "drinkimage": dict_drinkimg[title],
    }

    response = render(request, "payment.html", context=context)
    return response
