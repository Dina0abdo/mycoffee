from django.shortcuts import render, redirect
from django.contrib import messages
from shops.models import Shop
from orders.models import Order
from orders.models import order_details
from django.utils import timezone
# Create your views here.


def add_to_cart(request):

    if 'pro_id' in request.GET and 'qty' in request.GET and 'price' in request.GET and request.user.is_authenticated and not request.user.is_anonymous:
        pro_id = request.GET['pro_id']
        qty = request.GET['qty']

        order = Order.objects.all().filter(user=request.user, is_finished=False)
        if not Shop.objects.all().filter(id=pro_id).exists():
            # messages.error(request, 'not have product')
            return redirect('shops')

        pro = Shop.objects.get(id=pro_id)

        if order:
            messages.success(request, 'old order')
            old_order = Order.objects.get(user=request.user, is_finished=False)
            orderdetails = order_details.objects.create(
                shop=pro, order=old_order, price=pro.price, quantity=qty)

        else:
            messages.success(request, 'new order')
            new_order = Order()
            new_order.user = request.user
            new_order.order_date = timezone.now()
            new_order.is_finished = False
            new_order.save()
            orderdetails = order_details.objects.create(
                shop=pro, order=new_order, price=pro.price, quantity=qty)
        return redirect('/shops/' + request.GET['pro_id'])

    else:

        return redirect('shops')


def cart(request):
    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        if Order.objects.all().filter(user=request.user, is_finished=False):
            order = Order.objects.get(user=request.user, is_finished=False)
            orderdetails = order_details.objects.filter(order=order)
            total = 0
            for sub in orderdetails:
                total += sub.price*sub.quantity

            context = {
                'order': order,
                'orderdetails': orderdetails,
                'total': total,

            }
    return render(request, 'orders/cart.html', context)


def remove_from_cart(request, orderdetails_id):
    if request.user.is_authenticated and not request.user.is_anonymous and orderdetails_id:
        orderdetails = order_details.objects.get(id=orderdetails_id)
        orderdetails.delete()
    return redirect('cart')


def add_qty(request, orderdetails_id):
    if request.user.is_authenticated and not request.user.is_anonymous and orderdetails_id:
        orderdetails = order_details.objects.get(id=orderdetails_id)
        orderdetails.quantity += 1
        orderdetails.save()
        return redirect('cart')


def sub_qty(request, orderdetails_id):
    if request.user.is_authenticated and not request.user.is_anonymous and orderdetails_id:
        orderdetails = order_details.objects.get(id=orderdetails_id)
        if orderdetails.quantity > 1:
            orderdetails.quantity -= 1
            orderdetails.save()
        return redirect('cart')
