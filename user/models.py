from django.db import models

# Create your models here.
from admins.models import Prodcuts


class RegisterModel(models.Model):
    firstname=models.CharField(max_length=300)
    lastname=models.CharField(max_length=200)
    userid=models.CharField(max_length=200)
    password=models.IntegerField()
    mblenum=models.BigIntegerField()
    email=models.EmailField(max_length=400)
    gender=models.CharField(max_length=200)
    category=models.CharField(max_length=200)

class Purchase(models.Model):
    customer = models.ForeignKey(RegisterModel,on_delete=models.CASCADE)
    purhased = models.ForeignKey(Prodcuts,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=200,default='incart')
    cate=models.CharField(max_length=200)
    proname=models.CharField(max_length=200)

class ReviewModel(models.Model):
    usid = models.ForeignKey(RegisterModel, on_delete=models.CASCADE)
    proid = models.ForeignKey(Prodcuts, on_delete=models.CASCADE)
    review=models.CharField(max_length=500)
    sentiment=models.CharField(max_length=200)

class Visual_Sequence(models.Model):
    prosid = models.ForeignKey(Prodcuts, on_delete=models.CASCADE)
    cateogory = models.CharField(max_length=200)
    vals=models.IntegerField()
class Visual_Sequences(models.Model):
    prosid = models.ForeignKey(Prodcuts, on_delete=models.CASCADE)
    cateogory = models.CharField(max_length=200)
    vals=models.IntegerField()
