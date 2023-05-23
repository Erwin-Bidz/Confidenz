from django.shortcuts import render
from rest_framework import viewsets
from basefinale.models import Entreprise, Fichier
from basefinale.serializers import EntrepriseSerializer, FichierSerializer

# Create your views here.
class FichierViewset(viewsets.ModelsViewset):

    queryset = Fichier.objetcs.all()
    serializer_class = FichierSerializer