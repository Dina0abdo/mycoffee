from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def menu(request):
    return render(request, 'pages/menu.html')


def services(request):
    return render(request, 'pages/services.html')


def blog(request):
    return render(request, 'pages/blog.html')


def blog_single(request):
    return render(request, 'pages/blog_single.html')


def content(request):
    return render(request, 'pages/content.html')


def cart(request):
    return render(request, 'pages/cart.html')


def checkout(request):
    return render(request, 'pages/checkout.html')
