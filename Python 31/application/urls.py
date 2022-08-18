from django.urls import path
from .views import index, show_user_orders, show_order, sign_up, show_orders

urlpatterns = [
    path('', index, name='index'),
    path('user_orders/page<int:page>/', show_user_orders, name='show_user_orders'),
    path('orders/page<int:page>/', show_orders, name='show_orders'),
    path('order<int:id>/', show_order, name='show_order'),
    path('registration/sign_up', sign_up, name='sign_up'),
]
