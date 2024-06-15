"""
The user urls
custom made urls

"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
]