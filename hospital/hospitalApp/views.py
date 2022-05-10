from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render
import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    return render(request, 'hospitalApp/index.html')


class DoctorsList(ListView):
    model = Doctor
    template_name = 'hospitalApp/doctors_list.html'


class DoctorDetail(DetailView):
    model = Doctor
    template_name = 'hospitalApp/doctor_detail.html'


class DoctorCreate(CreateView):
    model = Doctor
    success_url = reverse_lazy('doctors_list')
    fields = ['name', 'last_name', 'email', 'age', 'specialty', 'entrance_time', 'exit_time']


class DoctorUpdate(UpdateView):
    model = Doctor
    success_url = reverse_lazy('doctors_list')
    fields = ['name', 'last_name', 'email', 'age', 'specialty', 'entrance_time', 'exit_time']


class DoctorDelete(DeleteView):
    model = Doctor
    success_url = reverse_lazy('doctors_list')
    fields = ['name', 'last_name', 'email', 'age', 'specialty', 'entrance_time', 'exit_time']


class PatientList(ListView):
    model = Patient
    template_name = 'hospitalApp/patients_list.html'


class PatientDetail(DetailView):
    model = Patient
    template_name = 'hospitalApp/patient_detail.html'


class PatientCreate(CreateView):
    model = Patient
    success_url = reverse_lazy('patients_list')
    fields = ['name', 'last_name', 'email', 'age', 'medical_history']


class PatientUpdate(UpdateView):
    model = Patient
    success_url = reverse_lazy('patients_list')
    fields = ['name', 'last_name', 'email', 'age', 'medical_history']


class PatientDelete(DeleteView):
    model = Patient
    success_url = reverse_lazy('patients_list')
    fields = ['name', 'last_name', 'email', 'age', 'medical_history']

class ParentList(ListView):
    model = Parent
    template_name = 'hospitalApp/parents_list.html'


class ParentDetail(DetailView):
    model = Parent
    template_name = 'hospitalApp/parent_detail.html'


class ParentCreate(CreateView):
    model = Parent
    success_url = reverse_lazy('parents_list')
    fields = ['name', 'last_name', 'email', 'age', 'medical_history', 'patient_relantionship']


class ParentUpdate(UpdateView):
    model = Parent
    success_url = reverse_lazy('parents_list')
    fields = ['name', 'last_name', 'email', 'age', 'medical_history', 'patient_relantionship']


class ParentDelete(DeleteView):
    model = Patient
    success_url = reverse_lazy('parents_list')
    fields = ['name', 'last_name', 'email', 'age', 'medical_history', 'patient_relantionship']

