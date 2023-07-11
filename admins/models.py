from django.db import models

# Create your models here.
from admins.choises import CHOICES


class Prodcuts(models.Model):
    category = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    vendor_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    price = models.FloatField(max_length=200)
    featuers = models.CharField(max_length=200)
    images = models.FileField()

    def  __str__(self):
        return self.product_name