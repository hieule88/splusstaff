from django.shortcuts import render
from splus.models import *
from cart.models import *
# from pyngrok import ngrok
...
# url = ngrok.connect(8000).public_url
# print('Henzy Tunnel URL:', url)

# Create your views here.

def menu(request):
    return render(request, 'menu.html')

def trend(request):
    return render(request, 'trend.html')