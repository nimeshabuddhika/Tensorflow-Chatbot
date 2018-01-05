from django.urls import path
from . import controller

urlpatterns = [
    path('', controller.index),
]
