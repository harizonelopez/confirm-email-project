"""
The user urls
custom made urls

"""

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [  
    path('', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]