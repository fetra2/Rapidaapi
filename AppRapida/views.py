from django.http import HttpResponse
from django.shortcuts import render

from AppRapida.models import Tarif, Zonify, Bureaux
from django.core import serializers
from django.http import JsonResponse, HttpResponseRedirect
from AppRapida.forms import TarifForm
from django.urls import reverse
import requests
import json

#api imports
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .serializers import TarifSerializer, ZonifySerializer, BureauxSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class RegisterUser(APIView):
    permission_classes = [permissions.AllowAny]
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                description="User registered successfully"
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Bad request"
            ),
        },
    )
    def post(self, request, format=None):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(username=username, password=password)
        if user:
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)



class ProtectedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]#do not allow anonymous
    def get(self, request):
        return Response({'message': 'Authenticated user', 'user': str(request.user)})

def index(request):
	return HttpResponse("kaiz")


class Bureau(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]#do not allow anonymous

    def get(self, request):  
        try:
            bureaux = Bureaux.objects.all()
            serializer = BureauxSerializer(bureaux, many=True) 
            return Response(serializer.data)
        except Bureaux.DoesNotExist:
            return Response({"error": " Bureaux not found"}, status=404)

class ZoneByCodique(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]#do not allow anonymous

    def get(self, request, codique1, codique2):
        if codique1 is None or codique2 is None:
            return Response({"error": "'two codiques ' are required."}, status=400)   
        try:
            zone = Zonify.objects.filter(ncodiquebur1=codique1, ncodiquebur2=codique2)
            serializer = ZonifySerializer(zone, many=False) 
            return Response(serializer.data)
        except Zonify.DoesNotExist:
            return Response({"error": "Zone not found for the given parameters."}, status=404)

class TarifZone(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]#do not allow anonymous

    def get(self, request, zone):
        if zone is None:
            return Response({"error": "'zone' is required."}, status=400)
        
        try:
            tarifs = Tarif.objects.filter(zone=zone)
            serializer = TarifSerializer(tarifs, many=True) 
            return Response(serializer.data)
        except Tarif.DoesNotExist:
            return Response({"error": "Tarif not found for the given parameters."}, status=404)

class TarifZonePoids(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]#do not allow anonymous

    def get(self, request, zone, poids):
        if zone is None or poids is None:
            return Response({"error": "Both 'zone' and 'poids' parameters are required."}, status=400)
        
        try:
            tarifs = Tarif.objects.filter(zone=zone)
            poidsmax = 0
            for tarif in tarifs:
                if float(poids)>=tarif.poidsmax:
                        print(f"poids = {poids} poidsmax={tarif.poidsmax}")
                        poidsmax = tarif.poidsmax
            queryset = tarifs.filter(poidsmin=poidsmax)
            serializer = TarifSerializer(queryset, many=True) 
            return Response(serializer.data)
        except Tarif.DoesNotExist:
            return Response({"error": "Tarif not found for the given parameters."}, status=404)


def formTarif(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TarifForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            zone = request.POST.get('zone')
            poids = float(request.POST.get('poids'))
            print(f"zone:{zone}, poids:{poids}")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #print(request.build_absolute_uri(reverse('tarif', args=(zone, poids))))
            tarif = requests.get(request.build_absolute_uri(reverse('tarif', args=(zone, poids))))
            data = json.loads(tarif.json())
            print(data[0]['fields']['zone'])
            print(data[0]['fields']['price'])
            return HttpResponse(f"<h1>zone: {data[0]['fields']['zone']}, prix: {data[0]['fields']['price']}</h1>")
            #return HttpResponseRedirect(reverse('showtarif'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TarifForm()

    return render(request, 'tarif_form.html', {'form': form})

class TarifList(generics.ListCreateAPIView):
    queryset = Tarif.objects.all()
    serializer_class = TarifSerializer

class TarifDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarif.objects.all()
    serializer_class = TarifSerializer
