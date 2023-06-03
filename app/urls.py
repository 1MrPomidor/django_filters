from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('create/product/', create_product)
]