from django.shortcuts import render

# Create your views here.


def shops(request):
    return render(request, 'shops/index.html')


def product_single(request):
    return render(request, 'shops/product_single.html')
