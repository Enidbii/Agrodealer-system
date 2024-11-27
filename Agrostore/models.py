import uuid

from django.db.models import ForeignKey
from django.utils import timezone
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="created at")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="updated at")

    class Meta:
        abstract = True


class Product(BaseModel):
    category_choices = [
        ('seeds', 'Seeds'),
        ('tools', 'Tools'),
        ('herbicides', 'Herbicides'),
        ('pesticides', 'Pesticides'),
        ('fertilizers', 'Fertilizers')
    ]
    product_name = models.CharField(max_length=100, blank=False, null=False)
    category = models.CharField(max_length=150, choices=category_choices, blank=False, null=False)
    unit_price = models.IntegerField()
    stock_quantity = models.CharField(max_length=200)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "%s" % self.product_name

class Supplier(BaseModel):
    supplier_name = models.CharField(max_length=100, blank=False, null=False)
    contact = models.CharField(max_length=150, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return "%s" % self.supplier_name

class Customer(BaseModel):
    customer_name = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=150, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return "%s" % self.customer_name

# class Employee(models.Model):
#     employee_choices = [
#         ('manager', 'Manager'),
#         ('storekeeper', 'Storekeeper'),
#         ('cashier', 'Cashier')
#     ]
#     position = models.CharField(max_length=150, choices=employee_choices, blank=False, null=False)
#     salary = models.CharField(max_length=200, blank=False, null=False)
#     hire_date = models.DateTimeField(default=timezone.now, verbose_name='date_hired')

class Sale(BaseModel):
    sale_date = models.DateTimeField(default=timezone.now, verbose_name='date_sold')
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, blank=True, null=True)
    employee = models.CharField(max_length=150, default='employee')
    total_amount = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return "%s - sale" % self.customer

class SaleItem(BaseModel):
    sale = models.ForeignKey("Sale", on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return "%s" % self.product

class Task(BaseModel):
    choices = [
        ('not approved', 'Not approved'),
        ('pending', 'Pending'),
        ('complete', 'Complete'),
        ('overdue', 'Overdue')
    ]
    priority_choices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]
    title = models.CharField(max_length=100, default="Task")
    description = models.TextField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=150, choices=choices, default="Pending")
    priority = models.CharField(max_length=150, choices=priority_choices, default="medium")
    due_date = models.DateTimeField(blank=True,null=True)
    sale_item = models.ForeignKey(SaleItem, on_delete=models.CASCADE, null=True)
    employee = models.CharField(max_length=150, default=True)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.title

class Inventory(BaseModel):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, blank=True, null=True)
    date_changed = models.DateTimeField(default=timezone.now, verbose_name="date_changed")
    quantity =models.IntegerField()
    reason = models.TextField(max_length=200, blank=False, null=False)

    def __str__(self):
        return "product-%s" % self.product