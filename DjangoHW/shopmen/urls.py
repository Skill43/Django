from django.contrib import admin
from django.urls import path, include
from .views import index, data, basket

urlpatterns = [
    path('', index),
    path('data/', data),
    path('basket/', basket)
]