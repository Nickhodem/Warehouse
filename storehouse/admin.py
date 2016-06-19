from django.contrib import admin
from .models import Ware, Provider,Product, Order


class PageWare(admin.ModelAdmin):
    list_display = ('id','idx', 'name', 'quantity')
    search_fields = ['name', 'quantity']
    list_filter = ('id','idx', 'name', 'quantity')

class PageProduct(admin.ModelAdmin):
    list_display = ('name', 'model')


class PageOrder(admin.ModelAdmin):
    list_display = ('name', 'product', 'status_open', 'client', 'notes')


admin.site.register(Ware, PageWare)
admin.site.register(Provider)
admin.site.register(Product,PageProduct)
admin.site.register(Order, PageOrder)
