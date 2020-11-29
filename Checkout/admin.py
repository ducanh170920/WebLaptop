from django.contrib import admin
from .models import Order_Product
from .models import Order
admin.site.register(Order_Product)
admin.site.register(Order)
