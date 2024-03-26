from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, Client, Product

def index(request):
    return render(request, 'shopmen/base.html')

def data(request):
    return render(request, 'shopmen/index.html')

def basket(request, client_id):
    products = []
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(customer=client).all()
    for order in orders:
        products.append(order.products.all())
    products.reverse()
    return render(request, 'shopmen/client.html', {'client': client, 'orders': orders, 'products': products} )

