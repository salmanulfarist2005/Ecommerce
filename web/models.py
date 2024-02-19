from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name1=models.CharField(max_length=30,blank=True)
    image=models.ImageField(upload_to='media')
    name2=models.CharField(max_length=30)
    name =models.TextField()
    com=models.CharField(max_length=30)
    price=models.FloatField()
    oldpirce=models.FloatField()
    colour=models.CharField(max_length=50,blank=True)


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    telephone=models.IntegerField()
    subject=models.CharField(max_length=50)
    message=models.TextField()

class Checkout(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    baddress=models.TextField()
    baddress2=models.TextField()
    select=models.TextField()
    city=models.TextField()
    zipcode=models.IntegerField()
    phone=models.IntegerField()
    cname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)



class OrderItem(models.Model):
    checkout=models.ForeignKey(Checkout,on_delete=models.CASCADE)
    porduct=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/order_image')
    qunatity=models.IntegerField()
    price=models.FloatField()
    total=models.IntegerField()
    paid=models.BooleanField(default=False)

     
        




