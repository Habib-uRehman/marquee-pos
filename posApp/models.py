from datetime import datetime
from unicodedata import category
from django.db import models
from django.utils import timezone


# Create your models here.

# class Employees(models.Model):
#     code = models.CharField(max_length=100,blank=True) 
#     firstname = models.TextField() 
#     middlename = models.TextField(blank=True,null= True) 
#     lastname = models.TextField() 
#     gender = models.TextField(blank=True,null= True) 
#     dob = models.DateField(blank=True,null= True) 
#     contact = models.TextField() 
#     address = models.TextField() 
#     email = models.TextField() 
#     department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
#     position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
#     date_hired = models.DateField() 
#     salary = models.FloatField(default=0) 
#     status = models.IntegerField() 
#     date_added = models.DateTimeField(default=timezone.now) 
#     date_updated = models.DateTimeField(auto_now=True) 

# def __str__(self):
#     return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '
class Category(models.Model):
    name = models.TextField()
    description = models.TextField()
    status = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    code = models.CharField(max_length=100, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    price = models.FloatField(default=0)
    status = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code + " - " + self.name


class Sales(models.Model):
    customer_name = models.CharField(max_length=30, blank=True, null=True)
    customer_number = models.CharField(max_length=11, blank=True, null=True)
    event_date = models.DateTimeField(default=timezone.now)
    seriel_no = models.IntegerField(default=0, blank=True, null=True)
    cnic = models.CharField(max_length=15, default='nill', blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    ladies = models.IntegerField(default=0, blank=True, null=True)
    gents = models.IntegerField(default=0, blank=True, null=True)
    sub_total = models.FloatField(default=0, blank=True, null=True)
    grand_total = models.FloatField(default=0, blank=True, null=True)
    tax_amount = models.FloatField(default=0, blank=True, null=True)
    tax = models.FloatField(default=0, blank=True, null=True)
    perhead_charges = models.FloatField(default=0, blank=True, null=True)
    hall = models.FloatField(default=0, blank=True, null=True)
    tendered_amount = models.FloatField(default=0, blank=True, null=True)
    amount_change = models.FloatField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    extra_charges = models.IntegerField(default=0, blank=True, null=True)
    sub = models.IntegerField(default=0, blank=True, null=True)
    cash_received = models.IntegerField(default=0, blank=True, null=True)
    event_time = models.CharField(max_length=6, blank=True, null=True)
    customer_address = models.CharField(max_length=200, default='Nill', blank=True, null=True)
    balance_due = models.IntegerField(blank=True, null=True)

    # def __str__(self):
    #     return self.id


class salesItems(models.Model):
    sale_id = models.ForeignKey(Sales, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)
