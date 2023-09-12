from rest_framework import serializers
from .models import Tarif, Zonify, Bureaux

class TarifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarif
        #fields = '__all__'
        exclude = ['id']

class ZonifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Zonify
        fields = ('ncodiquebur1', 'ncodiquebur2', 'zonemodifier')

class BureauxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bureaux
        exclude = ['id']