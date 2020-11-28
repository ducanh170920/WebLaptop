from django.db import models

# Create your models here.
from Account.models import Customer
from Shop.models import Product


class Order(models.Model):
    status =(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer,on_delete = models.SET_NULL,null=True,blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,null=True,choices=status)
    shippedDate = models.DateTimeField()


class Orderdetail(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=0,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
