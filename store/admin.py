from django.contrib import admin

from .models import Category, SubCategory, CategoryImage, Product, ProductStatus, ProductImage, ProductTag

@admin.register(CategoryImage)
class CategoryImageAdmin(admin.ModelAdmin):
    list_display = ["id", "category", "image"]
    list_display_links = ["id", "category"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "category"]
    list_display_links = ["id", "title"]
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "quantity", "status", "tag", "subcategory"]
    list_display_links = ["id", "title"]
    list_filter = ["status", "subcategory"]
    search_fields = ["title", "price"]

@admin.register(ProductStatus)
class ProductStatusAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "image"]
    list_display_links = ["id", "product"]

@admin.register(ProductTag)
class ProductTag(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]


