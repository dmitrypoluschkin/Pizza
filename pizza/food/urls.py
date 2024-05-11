from django.urls import path
from . import views

app_name = 'food'

urlpatterns =[
    path('pizza', views.pizza, name='pizza'),
    path('rolls', views.rolls, name='rolls'),
    path('drinks', views.drinks, name='drinks'),
    path('order', views.order, name='order'),
    path('success', views.success, name='success'),
]