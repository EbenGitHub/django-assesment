from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_lists, name='user-list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('change-password/', views.change_password, name='change-password'),
    path('profile/', views.profile, name='profile'),
]