from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path
from . import views
from . views import CreateStripeCheckoutSessionView

urlpatterns = [
    path("",views.index,name='index'),
    path("login",views.login1,name='login'),
    path("signup",views.signup,name='signup'),
    path("logout" ,views.logout1,name='logout'),
    path("contact" ,views.contact,name='contact'),
    path("checkout",views.checkout,name='checkout'),
    path('placeorder',views.placeorder,name='placeorder'),
    path('Success',views.Success,name='Success'),




     path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart-detail/',views.cart_detail,name='cart_detail'),

    path(
        "create-checkout-session",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    




  

    
]
