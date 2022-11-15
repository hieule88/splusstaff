from django.urls import path
from .views import cartview 

urlpatterns = [
    path("", cartview, name="cartview"),
]
