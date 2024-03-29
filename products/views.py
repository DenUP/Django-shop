from django.shortcuts import render

from products.models import Product, ProductCategory

# Create your views here.

def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


context = {
    'title': 'Store - Каталог',
    "products": Product.objects.all(),
    'categories': ProductCategory.objects.all(),
}


def products(request):
    return render(request, 'products/products.html', context)
