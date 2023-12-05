from django.shortcuts import render
from django.http import HttpResponse
from appRapidaCorps.models import Personne, Envoi, Facture, Historique, Axe, Doc
from appRapidaCorps.serializers import PersonneSerializer, EnvoiSerializer, FactureSerializer, HistoriqueSerializer, AxeSerializer, DocSerializer


#api
from rest_framework.views import APIView
from rest_framework import status, generics, permissions, viewsets


# Create your views here.
def index(request):
	return HttpResponse("hombre si!")

class PersonneList(generics.ListCreateAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
class PersonneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer

class EnvoiList(generics.ListCreateAPIView):
    queryset = Envoi.objects.all()
    serializer_class = EnvoiSerializer
class EnvoiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Envoi.objects.all()
    serializer_class = EnvoiSerializer

class FactureList(generics.ListCreateAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer
class FactureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

class FactureByBureau(viewsets.ReadOnlyModelViewSet):
    serializer_class = FactureSerializer

    def get_queryset(self):
        codique = self.kwargs['codique']
        return Facture.objects.filter(bureau__codique=codique)

class HistoriqueList(generics.ListCreateAPIView):
    queryset = Historique.objects.all()
    serializer_class = HistoriqueSerializer
class HistoriqueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Historique.objects.all()
    serializer_class = HistoriqueSerializer

class AxeList(generics.ListCreateAPIView):
    queryset = Axe.objects.all()
    serializer_class = AxeSerializer
class AxeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Axe.objects.all()
    serializer_class = AxeSerializer

class DocList(generics.ListCreateAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer
class DocDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer