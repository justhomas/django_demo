from django.urls import path
from .consumer import WSConsumer
ws_urlpatterns = [
    path('ws/students/',WSConsumer.as_asgi()) 
]