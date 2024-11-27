from django.contrib import admin
from .models import Product, Supplier, Customer, Task, Sale, SaleItem, Inventory

# Register your models here.
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Task)
admin.site.register(Sale)
admin.site.register(SaleItem)
admin.site.register(Inventory)