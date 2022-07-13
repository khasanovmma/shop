from django.urls import path

from .views import home_page, product_category_page, product_detail_page

urlpatterns = [
    path("", home_page, name="home"),
    path("category/", product_category_page, name="category"),
    path("product/<int:pk>/detail/", product_detail_page, name="prodcut_detail"),
]
