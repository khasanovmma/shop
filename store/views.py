from django.shortcuts import render

def home_page(request):
    return render(request, "store/index.html")

def product_category_page(request):
    return render(request, "store/product_category.html")

def product_detail_page(request):
    return render(request, "store/product_card_detail.html")
