from django.shortcuts import render, redirect
from django import forms
from rest_framework import viewsets
from basefinale.serializers import EntrepriseSerializer, FichierSerializer, EmployeSerializer

from django.contrib.auth.models import User
from basefinale.models import Entreprise, Fichier, Employe

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from django.contrib.auth import login

from django.http import HttpResponse
import openpyxl


# Create your views here.

class PageLogin(LoginView):
    template_name = 'basefinale/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('files')

class RegisterPage(View):
    #template_name = 'basefinale/register.html'
    #form_class = UserCreationForm
    #model = User
    #fields = ['username', 'password', 'email']
    redirect_authenticated_user = True
    #success_url = reverse_lazy('files')

    def get(self, request):
        form = UserForm()
        return render(request, 'basefinale/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('files')
        return render(request, 'basefinale/register.html', {'form': form})


    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

class FichierViewSet(viewsets.ModelViewSet):

    queryset = Fichier.objects.all()
    serializer_class = FichierSerializer
    filterset_fields = ['favourite', 'company']
    search_fields = ['title']


class EntrepriseViewSet(viewsets.ModelViewSet):

    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
    search_fields = ['name']

class EmployeViewSet(viewsets.ModelViewSet):

    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    search_fields = ['identifier']


class FileList(LoginRequiredMixin, ListView):
    model = Fichier
    context_object_name = 'files'
    template_name = 'basefinale/fichier_list.html'


class FileDetail(LoginRequiredMixin, DetailView):
    model = Fichier
    context_object_name = 'file'

class FileAdd(LoginRequiredMixin, CreateView):
    model = Fichier
    fields = ['title', 'favourite', 'content', 'company']
    success_url = reverse_lazy('files') #renvoie à la liste des fichiers après l'upload d'un fichier
    template_name = 'basefinale/upload_fichier.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FileAdd, self).form_valid(form)

    #def upload_file(request):
    #    if request.method == 'POST':
    #        file = request.FILES['file']
    #        wb = openpyxl.load_workbook(file)
    #        ws = wb.active
    #        data = []
    #        for row in ws.iter_rows():
    #            row_data = []
    #            for cell in row:
    #                row_data.append(str(cell.value))
    #            data.append('\t'.join(data))
    #        file_data = '\n'.join(data)
    #        response = HttpResponse(content_type='text/plain')
    #        response['Content-Disposition'] = 'attachment; filename="data.txt"'
    #        response.write(file_data)
    #        return response
    #    return render(request, 'upload_fichier.html')

class FileDelete(LoginRequiredMixin, DeleteView):
    model = Fichier
    context_object_name = 'fichier'
    success_url = reverse_lazy('files')
    template_name = "basefinale/supprimer_fichier.html"

class FileUpdate(LoginRequiredMixin, UpdateView):
    model = Fichier
    fields = ['title', 'favourite', 'content', 'company']
    success_url = reverse_lazy('files')
    template_name = 'basefinale/modifier_fichier.html'

class CompanyAdd(LoginRequiredMixin, CreateView):
    model = Entreprise
    fields = '__all__'
    success_url = reverse_lazy('files')
    template_name = 'basefinale/ajout_entreprise.html'

class EmployeAdd(LoginRequiredMixin, CreateView):
    model = Employe
    fields = ['company', 'identifier']
    success_url = reverse_lazy('files')
    template_name = 'basefinale/ajout_employe.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EmployeAdd, self).form_valid(form)

