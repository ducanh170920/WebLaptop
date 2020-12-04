from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    newProduct = Product.objects.all().order_by('dateAdded')
    print(newProduct)
    context = {

    }
    return render(request,'Shop/Home.html',context)