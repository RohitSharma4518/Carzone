from django.db import models

# Create your models here.
class Inventory(models.Model):
    carid = models.IntegerField(primary_key = True)
    carname = models.TextField(null = False, max_length= 50)
    carprice = models.DecimalField(max_digits = 5, decimal_places = 2)
    carmodel = models.TextField(max_length = 50)
    carphoto= models.ImageField(upload_to="images", default =  None)
    # year of manufacturing
    yom = models.TextField(max_length = 5)
    fueltype = models.TextField(max_length = 20, null = False)

class Employee(models.Model):
    empid = models.IntegerField(primary_key = True)
    empname = models.TextField(max_length = 40, null = False)
    # Date of birth
    dob = models.DateField(None)
    empmail = models.EmailField(unique = True, null = False)
    empdesignation = models.TextField(max_length = 40)
    empsalary = models.DecimalField(max_digits = 5, decimal_places = 2)


class Customer(models.Model):
    cusid = models.IntegerField(primary_key = True)
    cusname = models.TextField(max_length = 40, null = False)
    cusaddress = models.TextField(max_length = 100, null = False)
    # Date of birth
    phoneno = models.IntegerField(unique = True)
    cusmail = models.EmailField(unique = True, null = False)


class Sales(models.Model):
    invoiceno = models.IntegerField(primary_key = True)
    scarid = models.ForeignKey(Inventory, on_delete = models.CASCADE)
    scusid = models.ForeignKey(Customer, on_delete = models.CASCADE)
    # sales person emp id
    spempid = models.ForeignKey(Employee, on_delete = models.CASCADE)
    sdate = models.DateTimeField(auto_now_add = True)
    # mode of payment
    mop = models.CharField(max_length = 10)
    selling_price = models.DecimalField(max_digits = 5, decimal_places = 2)
