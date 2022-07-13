from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Category, Product

def home_page(request):
    category  = Category.objects.all()
    products  = Product.objects.all()
    context = {
        "category": category, 
        "products": products[:6]
    }

    return render(request, "store/index.html", context=context)

def product_category_page(request):
    page = int(request.GET.get('page')) if request.GET.get('page') else 1

    products_obj  = Product.objects.all()
    pagination = Paginator(products_obj, 1)
    current_page = pagination.get_page(page)

    products = pagination.page(page)
    context = {
        "products": products,
        "pagination": pagination,
        "current_page": current_page
    }
    return render(request, "store/product_category.html", context=context)

def product_detail_page(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product
    }
    return render(request, "store/product_card_detail.html", context=context)
