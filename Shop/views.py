import json

from django.http import JsonResponse
from django.shortcuts import render
from  .models import *
# Create your views here.
def Home(request):
    newProduct = Product.objects.order_by('dateAdded')[0:6]
    topSelling = Product.objects.order_by('-quantitySelled')[0:6]
    (cart,cart_product) = Same(request)
    context = {
        'newProduct' : newProduct,
        'topSelling' : topSelling,
        'cart'       : cart,
        'cart_product' : cart_product,
    }
    return render(request,'Shop/Home.html',context)
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('productId:', productId)
    print('action:', action)
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    cart,created = Cart.objects.get_or_create(customer = customer)
    cart_product,created = Cart_Product.objects.get_or_create(cart = cart,product = product)
    if action == 'add':
        cart_product.quantity = (cart_product.quantity+1)
        cart_product.save()
    elif action == 'remove':
         cart_product.delete()

    return JsonResponse("cart is updated", safe=False)
def Same(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer)
        cart_product = cart.cart_product_set.all()
    else:
        cart_product=[]
        cart = {'get_total_product': 0,'get_total_price_product':0}

    return  (cart,cart_product)