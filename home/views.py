from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from product.models import Product, Category, Images, Brand


def index(request):
    sliderdata = Category.objects.all()[1:5]
    category = Category.objects.all()
    dayproducts = Product.objects.all()[:5]
    lastproducts = Product.objects.all().order_by('-id')[:4]
    randomproducts = Product.objects.all().order_by('?')[:4]

    context = {'page':'home',
               'sliderdata':sliderdata,
               'category':category,
               'dayproducts':dayproducts,
               'lastproducts':lastproducts,
               'randomproducts':randomproducts}
    return render(request,'index.html',context)


def category_products(request,id,slug):
    category = Category.objects.all()
    category_data = Category.objects.get(id=id)
    products = Product.objects.filter(category_id=id)
    brands = Product.objects.filter(category_id=id).values_list("brand_id", flat=True)
    blist = list(brands)
    brand_list = Brand.objects.filter(id__in=blist)
    cat_id=id
    context = {'products': products,
               'brand_list': brand_list,
               'category': category,
               'category_data': category_data,
               'cat_id': cat_id}
    return render(request,'products.html',context)


def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(id=id)
    images = Images.objects.filter(product_id=id)
    s1 = Product.objects.get(id=id)
    s = s1.status
    context = {
        'x': 'x',
        's': s,
        'product': product,
        'category': category,
        'images': images
    }
    return render(request,'product_detail.html',context)


def product_filter_brand(request, cat_id, br_id):
    category = Category.objects.all()
    category_data = Category.objects.get(id=cat_id)
    products = Product.objects.filter(category_id=cat_id).filter(brand_id=br_id)
    brands = Product.objects.filter(category_id=cat_id).values_list("brand_id", flat=True)
    blist = list(brands)
    brand_list = Brand.objects.filter(id__in=blist)
    cat_id = cat_id
    context = {
        'products': products,
        'brand_list': brand_list,
        'category': category,
        'category_data': category_data,
        'cat_id': cat_id
        }
    return render(request, 'products.html', context)
