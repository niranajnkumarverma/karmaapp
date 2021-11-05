from django.contrib import admin
from .models import Billing_Address, Cart, Order, Product, User, UserProfile

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Billing_Address)
