from django.db import models


class Sqtable_cont(models.Model):
    name=models.CharField(max_length=30)
    gmail=models.CharField(max_length=30)
    msg=models.TextField(max_length=100)


class Products(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=30)
    price =models.IntegerField()
    image = models.ImageField(upload_to='products/') 

