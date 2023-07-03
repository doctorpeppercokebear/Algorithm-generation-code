from django.urls import path
from .views import ai 

urlpatterns = [
    path('ai/', ai, name='모민규')
]