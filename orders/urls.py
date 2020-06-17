from django.urls import path

from . import views

urlpatterns = [
    path("", views.registerUser, name="registerUser"),
    path("login", views.loginUser, name="loginUser"),
    path("menu", views.menu, name="menu"),
    path("logout", views.logoutUser, name="logoutUser"),
    path("cart", views.cart, name="cart"),
    path("cart/<int:user_id>", views.user_order, name="user_order")
]
