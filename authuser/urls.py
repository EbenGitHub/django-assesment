from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_lists, name='user-list'),
    path('profile/', views.profile, name='profile'),
]