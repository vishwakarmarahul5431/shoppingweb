from django.contrib import admin
from .models import Product,Catogery

# Register your models here.
class AdminProduct(admin.ModelAdmin):
       list_display = ['product_name','price','description','image','category',]
       list_editable = ['category']
       search_fields = ['product_name']

class AdminCatogery(admin.ModelAdmin):
       list_display = ['id','name']



admin.site.register(Product,AdminProduct)
admin.site.register(Catogery,AdminCatogery)
