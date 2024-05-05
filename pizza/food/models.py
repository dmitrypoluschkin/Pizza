from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=4, decimal_places=2)
    priceL = models.DecimalField(max_digits=4, decimal_places=2)
    pImage = models.URLField()


class Roll(models.Model):
    name = models.CharField(max_length=120)
    price5 = models.DecimalField(max_digits=4, decimal_places=2)
    price10 = models.DecimalField(max_digits=4, decimal_places=2)
    rImage = models.URLField()


class Drink(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=4, decimal_places=2)
    priceL = models.DecimalField(max_digits=4, decimal_places=2)
    dImage = models.URLField()
