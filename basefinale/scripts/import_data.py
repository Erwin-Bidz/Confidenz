from basefinale.models import Entreprise

def run():
    for i in range(3, 9):
        entreprise = Entreprise()
        entreprise.name = "Entreprise N°%d" % i
        entreprise.description = "Description entreprise N°%d" % i
        entreprise.save()

print("Opération réussie !")