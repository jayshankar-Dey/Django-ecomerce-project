from django.db import models


# Create your models here.

class cat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    
class product(models.Model):
    pname = models.CharField(max_length=100)
    pimg = models.ImageField(upload_to="images/")
    pdetails = models.TextField
    pprice = models.IntegerField(max_length=20)
    pdiscount = models.IntegerField(max_length=20)
    pcategary = models.ForeignKey(cat,on_delete=models.CASCADE)
    pdelivary_fee = models.IntegerField(max_length=20)

class registers(models.Model):
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20)   

class cart(models.Model):
    price = models.IntegerField(max_length=20)
    user = models.IntegerField(max_length=20)
    pname = models.CharField(max_length=50)
    img = models.CharField(max_length=200)

class carts(models.Model):
    price = models.IntegerField(max_length=20)
    pid = models.ImageField(max_length=20)
    user = models.IntegerField(max_length=20)
    pname = models.CharField(max_length=50)
    img = models.CharField(max_length=200)
class addaddress(models.Model):
    user = models.IntegerField(max_length=20)
    address = models.CharField(max_length=240)
class odderss(models.Model):
    STATUS_CHOICES = (
        ('25','order'),
        ('50','shipped'),
        ('75','out for delivary'),
        ('100','deliverd'),
    )
    price = models.IntegerField(max_length=20)
    pid = models.IntegerField(max_length=20)
    user = models.IntegerField(max_length=20)
    pname = models.CharField(max_length=50)
    img = models.CharField(max_length=200)
    payment = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='25')
    order = models.CharField(max_length=20, default='order')
    address = models.CharField(max_length=240)

