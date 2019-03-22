from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.WishCreate.as_view(), name='wish_create'),
    # path('add/', views.add, name='add'),

]