"""
The user urls
custom made urls

"""

from django.urls import path
from . import views

urlpatterns = [  
    path('', views.signup, name='signup'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_user, name='logout_user'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
