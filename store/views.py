from django.shortcuts import render
from .models import Category

def home_page(request):
    category  = Category.objects.all()
    # for item in category:
    #     print(item.category_image.values("image"))
    context = {
        "category": category, 
    }

    return render(request, "store/index.html", context=context)

def product_category_page(request):
    return render(request, "store/product_category.html")

def product_detail_page(request):
    return render(request, "store/product_card_detail.html")
