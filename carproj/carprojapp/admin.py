from django.contrib import admin
from . models import *
# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    list_display = [
        "carid",
        "carname",
        "carprice",
        "carmodel",
        "yom",
        "fueltype"
    ]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        "empid",
        "empname",
        "dob",
        "empmail",
        "empdesignation",
        "empsalary"
    ]


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "cusid",
        "cusname",
        "cusaddress",
        "phoneno",
        "cusmail"
    ]

class SalesAdmin(admin.ModelAdmin):
    list_display = [
        "invoiceno",
        "scarid",
        "scusid",
        "spempid",
        "sdate",
        "mop",
        "selling_price"
    ]

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Sales, SalesAdmin)










