from django.db import models
from django.contrib.auth.models import User
from icecream.models import Icecream
# Create your models here.

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    icecreams=models.ManyToManyField(Icecream,through="CartItem")

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    icecreams=models.ForeignKey(Icecream,on_delete=models.PROTECT)

class Order(models.Model):
    order_id=models.CharField(primary_key=True,max_length=50)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    address_line_1=models.CharField(null=False,max_length=100)
    address_line_2=models.CharField(null=False,max_length=100)
    city=models.CharField(null=False,max_length=100)
    state=models.CharField(null=False,max_length=100)
    pincode=models.IntegerField(null=False)
    phone_no=models.BigIntegerField(null=False)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name}   ||  {self.created_at}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    icecreams=models.ForeignKey(Icecream,on_delete=models.PROTECT)

