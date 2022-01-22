from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('Hanya mampu tayang nama new')
