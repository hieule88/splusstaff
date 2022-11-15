from django.urls import path
from .views import menu, trend

urlpatterns = [
    path("", menu, name="menu"),
]
