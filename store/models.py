from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)

class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

class ProductStatus(models.Model):
    title = models.CharField(max_length=50)

class ProductTag(models.Model):
    title = models.CharField(max_length=50)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    status = models.ForeignKey("ProductStatus", on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey("ProductTag", on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    like = models.ManyToManyField(User)