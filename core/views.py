from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, wishlist, Address
from django.db.models import Count, Avg
from taggit.models import Tag

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

    # Getting all reviews
    reviews = ProductReview.objects.filter(product=product).order_by("-date")

    # Getting average Review
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    # 获取每个星级的数量
    star_counts = (
        ProductReview.objects.filter(product=product)
        .values('rating')
        .annotate(count=Count('rating'))
        .order_by('-rating')
    )

    # 计算总评分数量
    total_reviews = ProductReview.objects.filter(product=product).count()

    # 计算每个星级的百分比
    star_percentage = {}
    for star in range(1, 6):  # 从 1 星到 5 星
        count = next((item['count'] for item in star_counts if item['rating'] == star), 0)
        percentage = round((count / total_reviews) * 100) if total_reviews > 0 else 0
        star_percentage[star] = percentage
    
    p_image = product.p_images.all()

    context = {
        "p": product,
        "p_image": p_image,
        "average_rating": average_rating,
        "products": products,
        "reviews": reviews,
        "star_percentage": star_percentage,
        
    }

    return render(request, "core/product-detail.html", context)


def tag_list(request, tag_slug=None):
    products = Product.objects.filter(product_status="published").order_by("-id")

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    context = {
        "products": products,
        "tag": tag
    }
    return render(request, "core/tag.html", context)