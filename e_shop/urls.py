"""e_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from e_shop import settings
from home import views
from order import views as orderviews
from opencv_app import views as opviews

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('product/',include('product.urls')),
    path('home/',include('home.urls')),
    path('', include('home.urls')),
    path('category/<int:id>/<slug:slug>/',views.category_products, name='category_products'),
    path('category_br/<int:cat_id>/<int:br_id>/',views.product_filter_brand, name='product_filter_brand'),
    path('product/<int:id>/<slug:slug>/',views.product_detail, name='product_detail'),
    path('order/',include('order.urls')),
    path('shopcart/',orderviews.shopcart, name='shopcart'),
    path('editimages/',opviews.IndexView, name='IndexView'),
    path('editimages/edit/<int:id>/',opviews.EditCv2ImageView, name='EditCv2ImageView')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
