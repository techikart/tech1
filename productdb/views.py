from django.shortcuts import render
from .models import product_details
from .resources import productResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

# Create your views here.
def dataUpload(request):
    if request.method == 'POST':
        product_resource =productResource()
        dataset = Dataset()
        new_product = request.FILES['myfile']

        if not new_product.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'upload.html')

        imported_data = dataset.load(new_product.read(),format='xlsx')
        for data in imported_data:
            value = product_details(
                data[0],
                data[1],
                data[2],
                data[3]
                )
            value.save()
    return render(request,'upload.html')


def product_list(request):
    products = product_details.objects.all()
    data = {
        'products':products
    } 
    return render(request, 'product.html', context=data)