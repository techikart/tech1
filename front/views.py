from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')


def product(request):
    return render(request,'product.html')
    


def product_view(request):
    return render(request,'product_view.html')


def question(request):
    return render(request,'question.html')

def about(request):
    return render(request,'about.html')

def cart(request):
    return render(request,'cart.html')
    
def buyer(request):
    return render(request,'buyer.html')


