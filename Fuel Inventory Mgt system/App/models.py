from django.db import models

# Create your models here.
class Stock(models.Model):
    fuel = models.CharField(max_length=200)
    elitres = models.FloatField()
    mlitres = models.FloatField()
    volatility = models.FloatField()

def __str__(self):
        return f"Stock: {self.fuel} {self.elitres}, {self.volatility}"
class Calculation(models.Model):
    fuel = models.CharField(max_length=200)
    purchase = models.FloatField()
    sales = models.FloatField()
    expense = models.FloatField()
    costPerLitre=models.FloatField()
    netprofit = models.FloatField()
   