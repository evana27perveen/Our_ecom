from django.urls import path
from . import views

app_name = 'App_store'


urlpatterns = [
    path('', views.home, name='home'),
    path('add-to-cart', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart_sys, name='cart'),

]
