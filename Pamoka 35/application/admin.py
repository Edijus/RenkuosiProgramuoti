from django.contrib import admin
from django.contrib.auth.models import Permission, ContentType
from .models import User, Service, OrderDetail, Order

# Register your models here.
admin.site.register(User)
admin.site.register(Permission)
admin.site.register(ContentType)
admin.site.register(Service)
admin.site.register(OrderDetail)
admin.site.register(Order)
