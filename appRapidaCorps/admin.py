from django.contrib import admin
from .models import * 

# Register your models here.
#admin.site.register([TypeEnvoi, Axe, Doc] )
#admin.site.register([TypeEnvoi, Doc] )
#admin.site.register([Doc] )

class EnvoiAdmin(admin.ModelAdmin):
    list_display = ('num_envoi', 'poids', 'bureau_exp', 'bureau_dest', 'type_envoi', 'dateEnvoi')
    search_fields = ('num_envoi', 'bureau_exp__nom', 'bureau_dest__nom', 'type_envoi__name')
    list_filter = ('type_envoi', 'bureau_exp', 'bureau_dest', 'dateEnvoi')
admin.site.register(Envoi, EnvoiAdmin)

class PersonneAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'prenom', 'tel', 'adresse', 'mail', 'numeroId', 'categorie')
admin.site.register(Personne, PersonneAdmin)

class FactureAdmin(admin.ModelAdmin):
    list_display = ('numero_facture', 'numero_bordereau', 'prix_rapida', 'type_paiement', 'bureau', 'envoi', 'expediteur', 'destinataire', 'date_facture', 'statut')
admin.site.register(Facture, FactureAdmin)

class HistoriqueAdmin(admin.ModelAdmin):
    list_display = ('id','envoi', 'statut', 'isactive', 'bureau', 'date_historique')
admin.site.register(Historique, HistoriqueAdmin)

class AxeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'isactive', 'get_parents', 'date')
admin.site.register(Axe, AxeAdmin)
class DocAdmin(admin.ModelAdmin):
    list_display = ('id', 'convoyeur', 'voiture', 'display_envoi', 'axe', 'date')
    def display_envoi(self, obj):
        return ", ".join([envoi.num_envoi for envoi in obj.envoi.all()])
    display_envoi.short_description = 'Envois'
admin.site.register(Doc, DocAdmin)