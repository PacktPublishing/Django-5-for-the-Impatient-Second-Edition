from django.contrib import admin
from .models import Order, Item

admin.site.register(Order)
admin.site.register(Item)