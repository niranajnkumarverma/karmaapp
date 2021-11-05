from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    IsActive = models.BooleanField(default=False)
    Datecreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=10)
    address  =models.CharField(max_length=100)
    pincode = models.IntegerField(max_length=5)
    city = models.CharField(max_length=100)
   
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname
        
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    image = models.FileField(upload_to="products/")
    
    name = models.CharField(max_length=50, default='')
    
    price = models.DecimalField(max_digits=8, decimal_places=2)
    DateTime = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.name
   

class Cart(models.Model):
   
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    DateTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Cart"

class Billing_Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=10)
    address  =models.CharField(max_length=100)
    pincode = models.IntegerField(max_length=5)
    city = models.CharField(max_length=100)
    Districk = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class Order(models.Model):
    billing_Address=ForeignKey(Billing_Address,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)
    Total = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "Order"
        
    def __str__(self):
        return self.Product.name

