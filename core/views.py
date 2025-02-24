from django.shortcuts import render, get_object_or_404
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

def vendor_list_view(request):
    vendors = Vendor.objects.all()

    context = {
        'vendors': vendors
    }
    return render(request, 'core/vendor-list.html', context)

def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status="published")

    context = {
        'vendor': vendor,
        'products': products
    }
    return render(request, 'core/vendor-detail.html', context)


def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    # product = get_object_or_404(Product, pid=pid)
    products = Product.objects.filter(category=product.category).exclude(pid=pid)
    
    p_image = product.p_images.all()

    context = {
        "p": product,
        "p_image": p_image,
        "products": products,
    }

    return render(request, "core/product-detail.html", context)