
from django.urls import path
from .views import change_password,billing_page, order_page,  confirmation_page, contact_page, index, login_page, order_page, register_page, profile_page , logout_page, search_page, shop_page, update_page,delete_cart,add_to_cart,update_cart
urlpatterns = [
    path('',index, name="index"),
    path('login_page',login_page, name="login_page"),
    path('register_page',register_page, name="register_page"),
    path('contact_page',contact_page, name="contact_page"),
    path('profile_page',profile_page, name="profile_page"),
    path('change_password',change_password, name="change_password"),
    path('update_page/<int:id>',update_page, name="update_page"),
    path('shop_page',shop_page, name="shop_page"),
    
    path('order_page',order_page, name="order_page"),
    path('add_to_cart/<int:pk>/' , add_to_cart, name='add_to_cart'),
    path('delete_cart/<int:pk>/' , delete_cart, name='delete_cart'),
    path('update_cart/<int:pk>/' , update_cart, name='update_cart'),
    path('search_page' , search_page, name='search_page'),
    path('billing_page' , billing_page, name='billing_page'),
    path('confirmation_page',confirmation_page, name="confirmation_page"),
    path('logout_page',logout_page, name="logout_page"),



   
]
