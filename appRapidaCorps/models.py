from django.db import models
from django.contrib.auth.models import User
from AppRapida.models import Bureaux

# Create your models here.
class Personne(models.Model):
    nom = models.CharField(max_length=50, db_column='nom')
    prenom = models.CharField(max_length=50, db_column='prenom')
    tel = models.CharField(max_length=50, db_column='tel')
    adresse = models.CharField(max_length=50, db_column='adresse')
    mail = models.CharField(max_length=50, db_column='mail')
    numeroId = models.CharField(max_length=50, db_column='numeroId')#eg:CIN
    categorie = models.IntegerField(default=0, db_column='categorie')#particulier ou entreprise
    def __str__(self):
        return self.nom
    class Meta:
        managed = True
        db_table = 'rapida_personne'

class Envoi(models.Model):
    num_envoi = models.CharField(max_length=50, primary_key=True, db_column='num_envoi')
    poids = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, db_column='poids')
    bureau_exp = models.ForeignKey(Bureaux, on_delete=models.CASCADE, related_name='bureau_exp')
    bureau_dest = models.ForeignKey(Bureaux, on_delete=models.CASCADE, related_name='bureau_dest')
    #type_envoi = models.ForeignKey(TypeEnvoi, on_delete=models.CASCADE, related_name='type_envoi')
    type_envoi = models.IntegerField(default=0)
    dateEnvoi = models.DateTimeField(auto_now_add=True)
    #prixRapida = models.CharField(max_length=50, db_column='prixRapida') #voir facture

    def __str__(self):
        return str(self.num_envoi)
    class Meta:
        managed = True
        db_table = 'rapida_envoi'

class Facture(models.Model):
    class TypePayment(models.IntegerChoices):  # Corrected the class name
        DEPOT = 0, "0 depot"
        COLLECT = 1, "1 collect"

    numero_facture = models.CharField(max_length=50, db_column='numero_facture', null=True, blank=True)
    numero_bordereau = models.CharField(max_length=50, db_column='numero_bordereau', null=True, blank=True)
    prix_rapida = models.CharField(max_length=50, db_column='prix_rapida')
    type_paiement = models.IntegerField(choices=TypePayment.choices, default=TypePayment.DEPOT, db_column='type_paiement')
    bureau = models.ForeignKey(Bureaux, on_delete=models.CASCADE)
    envoi = models.ForeignKey(Envoi, on_delete=models.CASCADE)
    expediteur = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name='expediteur')
    destinataire = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name='destinataire')
    date_facture = models.DateTimeField(auto_now_add=True)
    statut = models.IntegerField(default=1)#1: ok, 2: annule, 3: annule par erreur technique


    def __str__(self):
        return self.numero_facture
    class Meta:
        managed = True
        db_table = 'rapida_facture'

class Historique(models.Model):
    envoi = models.ForeignKey(Envoi, on_delete=models.CASCADE)
    statut = models.CharField(max_length=10)
    isactive = models.IntegerField(default=1)
    bureau = models.ForeignKey(Bureaux, on_delete=models.CASCADE)
    date_historique = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.statut
    class Meta:
        managed = True
        db_table = 'rapida_historique'

class Axe(models.Model):
    nom = models.CharField(max_length=50)
    isactive = models.IntegerField(default=1)
    bureau = models.ManyToManyField(Bureaux, related_name='axe_bureau')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nom
    def get_parents(self):
        return ','.join([str(p) for p in self.bureau.all()])
    class Meta:
        managed = True
        db_table = 'rapida_axe'
    
class Doc(models.Model):
    envoi = models.ManyToManyField(Envoi, related_name='envoi_doc')
    axe = models.ForeignKey(Axe, on_delete=models.CASCADE)
    convoyeur = models.CharField(max_length=50)
    voiture = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        managed = True
        db_table = 'rapida_docs'