from rest_framework import serializers
from .models import Personne, Envoi, Facture, Historique, Axe, Doc

class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = '__all__'
        #exclude = ['id']

class EnvoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envoi
        fields = '__all__'

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = '__all__'
class HistoriqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historique
        fields = '__all__'
class AxeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Axe
        fields = '__all__'
class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = '__all__'