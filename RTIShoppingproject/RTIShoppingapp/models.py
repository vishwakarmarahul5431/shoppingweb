from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Catogery(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.FloatField(default=0)
    Discount = models.FloatField(default=0)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='static/products')
    category = models.ForeignKey(Catogery, on_delete=models.CASCADE,default=1)

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_product_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_product();

class Product_save(models.Model):
    name=models.CharField(max_length=100,default='',blank=True)
    phone_no=models.BigIntegerField(default=0,blank=True)
    pincode=models.BigIntegerField(default='',blank=True)
    city=models.CharField(max_length=100,default='',blank=True)
    locality=models.CharField(max_length=200,default='',blank=True)
    state=models.CharField(max_length=100,default='',blank=True)
    landmark=models.CharField(max_length=100,default='',blank=True)
    alt_no=models.BigIntegerField(default=0,blank=True,)
    address=models.CharField(max_length=200,default='',blank=True)












