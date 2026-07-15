from django.shortcuts import render, redirect
from .models import Product

cart = []

def home(request):

    products = Product.objects.all()

    total = sum(item.price for item in cart)

    return render(request,
                  'home.html',
                  {
                      'products': products,
                      'cart': cart,
                      'total': total
                  })

def add_to_cart(request, id):

    product = Product.objects.get(id=id)

    cart.append(product)

    return redirect('home')

def remove_from_cart(request, id):

    for item in cart:

        if item.id == id:

            cart.remove(item)

            break

    return redirect('home')