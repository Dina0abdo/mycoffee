from django.shortcuts import get_object_or_404, render
from datetime import datetime

from .models import Shop

# Create your views here.


def shops(request):
    pro = Shop.objects.all()
    name = None
    desc = None
    pfrom = None
    pto = None
    cs = None
    if 'cs' in request.GET:
        cs = request.GET["cs"]
        if not cs:
            cs = 'off'
    if 'searchname' in request.GET:
        name = request.GET["searchname"]
        if name:
            if cs == 'on':
                pro = pro.filter(name__contains=name)
            else:
                pro = pro.filter(name__icontains=name)

    if 'searchdescription' in request.GET:
        desc = request.GET["searchdescription"]
        if desc:
            if cs == 'on':
                pro = pro.filter(description__contains=desc)
            else:
                pro = pro.filter(description__icontains=desc)

    if 'searchprice_from' in request.GET and 'searchprice_to' in request.GET:
        pfrom = request.GET['searchprice_from']
        pto = request.GET['searchprice_to']
        if pfrom and pto:
            if pfrom.isdigit() and pto.isdigit():
                pro = pro.filter(price__gte=pfrom, price__lte=pto)

    context = {
        'shops': pro,

    }
    return render(request, 'shops/shops.html', context)


def product_single(request, pro_id):
    context1 = {
        'pro': get_object_or_404(Shop, pk=pro_id)
    }
    return render(request, 'shops/product_single.html', context1)


def search(request):

    return render(request, 'shops/search.html')
