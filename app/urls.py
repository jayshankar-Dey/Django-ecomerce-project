from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
     path('home/show/<int:id>',views.show,name='show'),
     path('under/<int:id>',views.under,name='under'),
     path('category/<int:id>',views.category,name='category'),
     path('search/result',views.search,name='search'),
     path('flipkart/login',views.login,name='login'),
     path('flipkart/register',views.register,name='register'),
     path('flipkart/reg',views.reg,name='reg'),
     path('flipkart/log',views.log,name='log'),
     path('flipkart/user/cart',views.cartss,name='cart'),
      path('flipkart/carts',views.addcart,name='add_cart'),
      path('delete/cart/<int:id>',views.delete_cart,name='delete_cart'),
     path('flipkart/order',views.order,name='order'),
     path('flipkart/address',views.address,name='address'),
     path('flipkart/add/address',views.add_address,name='add_address'),
      path('flipkart/add/delete_address/<int:id>',views.delete_address,name='delete_address'),
      path('flipkart/editaddress/<int:id>',views.edit_address,name='edit_address'),
      path('flipkart/add/edit_save_address',views.edit_save_address,name='edit_save_address'),
      path('flipkart/payment',views.payment,name='payment'),
      path('flipkart/user_order',views.user_order,name='user_order'),
      path('flipkart/show_order/<int:id>',views.show_order,name='show_order'),
      path('flipkart/conferm/<int:id>',views.conferm,name='conferm'),
      path('flipkart/conferm/save',views.save_conferm,name='save_conferm'),
]