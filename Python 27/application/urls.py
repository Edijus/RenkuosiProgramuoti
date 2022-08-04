from django.urls import path
from .views import Show, Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('show/', Show.as_view(), name='show')
]