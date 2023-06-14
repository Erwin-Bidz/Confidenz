from django.db import models


# Create your models here.

class Entreprise(models.Model):

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=200, null=True)


    def __str__(self):
        return self.name



class Fichier(models.Model):
    title = models.CharField(max_length=200)
    favourite = models.BooleanField()
    upload = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='fichier', null=True)

    company = models.ForeignKey(Entreprise, on_delete=models.CASCADE)

    def __str__(self):
            return self.title
        
