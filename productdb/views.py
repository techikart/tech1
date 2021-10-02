from django.shortcuts import render
from . models import product_details

# Create your views here.
def product_list(request):
    products = product_details.objects.all()
    data = {
        'products':products
    } 
    return render(request, 'product.html', context=data)