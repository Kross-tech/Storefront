from django.shortcuts import render
from store.models import Product


def index(request):
    products = Product.objects.all()[0:6]
    return render(request, 'index.html', {
        'products': products
    })

