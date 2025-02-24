from django.shortcuts import render
from django.http import HttpResponse
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, wishlist, Address
from django.db.models import Count

def index(request):
    # products = Product.objects.all().order_by('-id')
    products = Product.objects.filter(product_status="published", featured=True)

    context = {
        'products': products
    }
    
    return render(request, 'core/index.html', context)


def product_list_view(request):
    products = Product.objects.filter(product_status="published")

    context = {
        'products': products
    }
    
    return render(request, 'core/product-list.html', context)

def category_list_view(request):
    categories = Category.objects.all()

    context = {
        'categories': categories 
    }
    
    return render(request, 'core/category-list.html', context)

def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published" ,category=category)

    context = {
        'products': products,
        'category': category
    }
    return render(request, 'core/category-product-list.html', context)