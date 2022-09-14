from django.shortcuts import render

from products.models import Product


def home(request):
    form = ['register', 'login']
    products = Product.objects.all()
    return render(request, 'home.html', {"form": form, 'products': products})
