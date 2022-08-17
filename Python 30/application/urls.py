from django.urls import path
from .views import index, show_orders, show_order, sign_up

urlpatterns = [
    path('', index, name='index'),
    path('orders/page<int:page>/', show_orders, name='show_orders'),
    path('order<int:id>/', show_order, name='show_order'),
    path('registration/sign_up', sign_up, name='sign_up'),
]

