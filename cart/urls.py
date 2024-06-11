from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('main_cart', views.main_cart, name='cart'),

    path('create/<slug:slug>', views.create_cart, name='create_cart'),
    path('delete/<int:product_id>', views.delete_cart, name='delete_cart'),
    path('update/<slug:slug>', views.update_cart, name='update_cart'),
    path('empty_cart', views.empty_cart, name='empty_cart'),
]