from django.shortcuts import render
from django.http import HttpResponse
from appRapidaCorps.models import Personne, Envoi, Facture, Historique, Axe, Doc
from appRapidaCorps.serializers import PersonneSerializer, EnvoiSerializer, FactureSerializer, HistoriqueSerializer, AxeSerializer, DocSerializer


#api
from rest_framework.views import APIView
from rest_framework import status, generics, permissions, viewsets

from django.db.models import Subquery, OuterRef


# Create your views here.
def index(request):
	return HttpResponse("hombre si!")

class PersonneList(generics.ListCreateAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
class PersonneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer

class PersonneByDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonneSerializer

    def get_queryset(self):#tsy maintsy io no method ampiasana
        tel = self.request.query_params.get('tel', None)
        numero_id = self.request.query_params.get('numeroId', None)

        if tel:
            return Personne.objects.filter(tel=tel)
        elif numero_id:
            return Personne.objects.filter(numeroId=numero_id)
        else:
            return Personne.objects.none()

class EnvoiList(generics.ListCreateAPIView):
    queryset = Envoi.objects.all()
    serializer_class = EnvoiSerializer
class EnvoiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Envoi.objects.all()
    serializer_class = EnvoiSerializer
class EnvoiByDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EnvoiSerializer

    def get_queryset(self):
        bureau = self.request.query_params.get('bureau', None)
        factureIsNull = self.request.query_params.get('factureIsNull', None)

        if bureau and factureIsNull:
            envois_by_bureau_without_facture = Envoi.objects.filter(facture__isnull=True, bureau_exp__codique=bureau)
            return envois_by_bureau_without_facture
        elif bureau:
            envois_by_bureau_without_facture = Envoi.objects.filter(bureau_exp__codique=bureau)
            return envois_by_bureau_without_facture
        else:
            return Envoi.objects.none()
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
class FactureByDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FactureSerializer

    def get_queryset(self):
        bureau = self.request.query_params.get('bureau', None)
        type_paiement = self.request.query_params.get('type_paiement', None)
        limit = self.request.query_params.get('limit', None)
        if bureau and type_paiement and limit:
            two_facture_by_bureau_and_type_paiement = Facture.objects.filter(bureau__codique=bureau, type_paiement=type_paiement).order_by('-date_facture')[:int(limit)]
            return two_facture_by_bureau_and_type_paiement
        elif bureau and type_paiement:
            facture_by_bureau_and_type_paiement = Facture.objects.filter(bureau__codique=bureau, type_paiement=type_paiement)
            return facture_by_bureau_and_type_paiement
        elif bureau:
            facture_by_bureau = Facture.objects.filter(bureau__codique=bureau)
            return facture_by_bureau
        elif type_paiement:
            facture_by_type_paiement = Facture.objects.filter(type_paiement=type_paiement)
            return facture_by_type_paiement
        elif limit:
            return Facture.objects.all().order_by('-date_facture')[:int(limit)]
        else:
            return Facture.objects.all()
class HistoriqueList(generics.ListCreateAPIView):
    queryset = Historique.objects.all()
    serializer_class = HistoriqueSerializer
class HistoriqueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Historique.objects.all()
    serializer_class = HistoriqueSerializer

class HistoriqueByDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HistoriqueSerializer
    def get_queryset(self):
        bureau = self.request.query_params.get('bureau', None)
        statut = self.request.query_params.get('statut', None)
        isactive = self.request.query_params.get('isactive', None)
        if bureau and statut and isactive:
            return Historique.objects.filter(bureau=bureau, statut=statut, isactive=int(isactive))
        else:
            return Historique.objects.all() 
class AxeList(generics.ListCreateAPIView):
    queryset = Axe.objects.all()
    serializer_class = AxeSerializer
class AxeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Axe.objects.all()
    serializer_class = AxeSerializer
class AxeByDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AxeSerializer
    def get_queryset(self):
        bureau = self.request.query_params.get('bureau', None)
        if bureau:
            return Axe.objects.filter(bureau=bureau)
        else:
            return Axe.objects.all() 
class DocList(generics.ListCreateAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer
class DocDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer

class DocByDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DocSerializer
    def get_queryset(self):
        bureau = self.request.query_params.get('bureau', None)
        if bureau:
            return Doc.objects.filter(axe__bureau=bureau)
        else:
            return Doc.objects.all() 