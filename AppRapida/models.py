from django.db import models

# Create your models here.
class Tarif(models.Model):
    zone = models.IntegerField(blank=True, null=True)
    poidsmin = models.DecimalField(max_digits=10, decimal_places=2)
    poidsmax = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__ (self):
        return f"{self.id} zone: {self.zone}, price: {self.price}"  

class Bureaux(models.Model):
    codique = models.IntegerField()
    province = models.IntegerField(blank=True, null=True)
    codeclasse = models.IntegerField(blank=True, null=True)
    nombureau = models.CharField(max_length=50, blank=True, null=True)
    classe = models.CharField(max_length=50, blank=True, null=True)
    ccp = models.CharField(max_length=10, blank=True, null=True)
    sigle = models.CharField(max_length=5, blank=True, null=True)
    nompublic = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bureaux'


class Zonify(models.Model):
    depart = models.CharField(max_length=50)
    ncodiquebur1 = models.IntegerField()
    arrive = models.CharField(max_length=50)
    ncodiquebur2 = models.IntegerField()
    longueur = models.FloatField()
    zone = models.IntegerField()
    zonemodifier = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zonify'