from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from product.models import Product, Category, Images


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
    context = {'products' : products,
               'category' : category,
               'category_data' : category_data}
    return render(request,'products.html',context)

def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(id=id)
    images = Images.objects.filter(product_id=id)
    context = {
        'page': 'product_detail',
        'product': product,
        'category': category,
        'images': images
    }
    return render(request,'product_detail.html',context)