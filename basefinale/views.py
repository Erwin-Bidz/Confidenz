from django.shortcuts import render
from rest_framework import viewsets
from basefinale.models import Entreprise, Fichier
from basefinale.serializers import EntrepriseSerializer, FichierSerializer

# Create your views here.
class FichierViewset(viewsets.ModelViewSet):

    queryset = Fichier.objects.all()
    serializer_class = FichierSerializer
    
def home(request):
    liste_entreprises = Entreprise.objects.all()
    context = {"liste_entreprises": liste_entreprises}
    return render(request, "index.html", context)

def detail(request, entreprise_id):
    entreprise = Entreprise.objects.get(id = entreprise_id)
    liste_fichiers = Fichier.objects.filter(company_id = entreprise_id)
    context = {'liste_fichiers': liste_fichiers, 'entreprise': entreprise}
    return render(request, 'detail.html', context)

def search(request):
    query = request.GET["entreprise"]
    entreprises = Entreprise.objects.filter(name__contains=query)
    return render(request, 'search.html', {'entreprises': entreprises})













### Une autre méthode pour la vue détails ###
#def detail(request, entreprise_id):
#    entreprise = Entreprise.objects.get(id=entreprise_id)
#    fichiers = entreprise.fichier_set.all()
#    context = {'entreprise': entreprise, 'fichiers': fichiers}
#    return render(request, 'detail.html', context)