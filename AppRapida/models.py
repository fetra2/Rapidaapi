from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarif(models.Model):
    zone = models.IntegerField(blank=True, null=True)
    poidsmin = models.DecimalField(max_digits=10, decimal_places=2)
    poidsmax = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__ (self):
        return f"{self.id} zone: {self.zone}, price: {self.price}"  
"""    class Meta:
        managed = True
        db_table = 'tarif'"""

class Bureaux(models.Model):
    codique = models.IntegerField(primary_key=True)
    province = models.IntegerField(blank=True, null=True)
    codeclasse = models.IntegerField(blank=True, null=True)
    nombureau = models.CharField(max_length=50, blank=True, null=True)
    classe = models.CharField(max_length=50, blank=True, null=True)
    ccp = models.CharField(max_length=10, blank=True, null=True)
    sigle = models.CharField(max_length=5, blank=True, null=True)
    nompublic = models.CharField(max_length=50, blank=True, null=True)
    def __str__ (self):
        return str(self.codique) 
"""    class Meta:
        managed = True
        db_table = 'bureaux'"""


class Zonify(models.Model):
    depart = models.CharField(max_length=50)
    ncodiquebur1 = models.IntegerField()
    arrive = models.CharField(max_length=50)
    ncodiquebur2 = models.IntegerField()
    longueur = models.FloatField()
    zone = models.IntegerField()
    zonemodifier = models.IntegerField()

"""    class Meta:
        managed = True
        db_table = 'zonify'"""

#for auth search 
class Company(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
"""    class Meta:
        managed = True
        db_table = 'company'"""

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
"""    class Meta:
        managed = True
        db_table = 'userprofile'"""

#for Envoi #see appRapidaCorps