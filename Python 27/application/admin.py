from django.contrib import admin
from .models import User, Parent, Child

# Register your models here.
admin.site.register(User)
admin.site.register(Parent)
admin.site.register(Child)