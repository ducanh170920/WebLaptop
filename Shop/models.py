from django.db import models

# Create your models here.
from Account.models import Customer


class Brand(models.Model):
    brandName = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.brandName


class Category(models.Model):
    categoryName = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.categoryName


class Product(models.Model):
    brand = models.ForeignKey(Brand,on_delete = models.SET_NULL,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200,null=True)
    price = models.PositiveBigIntegerField()
    quantity = models.IntegerField()
    quantitySelled = models.IntegerField(default=0)
    dateAdded =models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True)

    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name




class Cart(models.Model):
    dateAdded = models.DateField(auto_now_add=True)
    quantity = models.IntegerField();

class Cart_Product(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)