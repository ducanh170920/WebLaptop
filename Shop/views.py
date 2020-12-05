from django.shortcuts import render
from  .models import *
# Create your views here.
def Home(request):
    newProduct = Product.objects.order_by('dateAdded')[0:6]
    topSelling = Product.objects.order_by('-quantitySelled')[0:6]
    print(newProduct)
    print(topSelling)
    context = {
        'newProduct' : newProduct,
        'topSelling' : topSelling,
    }
    return render(request,'Shop/Home.html',context)