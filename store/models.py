from django.db import models
from django.contrib.auth.models import User

class CategoryImage(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photo/category/%Y/%m/%d/")

    def __str__(self):
        return self.category.title

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

class ProductStatus(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product Status"
        verbose_name_plural = "Product Status"

class ProductTag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey("Product", related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photo/product/%Y/%m/%d/")

    def __str__(self):
        return self.product.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    status = models.ForeignKey("ProductStatus", on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey("ProductTag", on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    like = models.ManyToManyField(User, blank=True)
    subcategory = models.ForeignKey("SubCategory", on_delete=models.SET_NULL, null=True)

   

    def __str__(self):
        return self.title 
        
    class Meta:
        verbose_name = "Product"