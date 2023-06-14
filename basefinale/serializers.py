from rest_framework import serializers
from basefinale.models import Entreprise,Fichier

class FichierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fichier
        fields = '__all__'

class EntrepriseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entreprise
        fields = '__all__'