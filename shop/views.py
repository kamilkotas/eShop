from django.shortcuts import render
from .models import *
# Create your views here.


def shop(request):
    """Shows the main site of the store"""
    products = Product.objects.all()
    print(products.get(id=2))
    context = {"products": products}
    return render(request, "shop/shop.html", context)
