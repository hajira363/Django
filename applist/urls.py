from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('single/<int:index>',views.single,name='single' ),
    path ('cart/',views.addtocart,name='cart')
]