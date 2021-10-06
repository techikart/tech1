"""techicart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from front.views import home, product, product_view, about, cart, question, buyer
from productdb import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('product/', product),
    path('product_view/', product_view),
    path('about/', about),
    path('cart/', cart),
    path('question/', question),
    path('buyer/', buyer),
    path('a/', views.dataUpload),
]
