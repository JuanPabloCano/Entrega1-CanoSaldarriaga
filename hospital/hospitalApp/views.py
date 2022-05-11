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
    model = Parent
    success_url = reverse_lazy('parents_list')
    fields = ['name', 'last_name', 'email', 'age', 'medical_history', 'patient_relantionship']

# class DoctorSearch(ListView):
#     template_name = 'hospitalApp/doctor_search.html'
#     model = Doctor
#
#     def get_queryset(self):
#         name = self.request.GET.get['name']
#         object_list = self.model.objects.all()
#         if name:
#             object_list = self.model.objects.filter(name__icontains=name)
#         else:
#             object_list = self.model.objects.none()
#         return object_list

def doctorSearchResults(request):
    return render(request, 'hospitalApp/doctor_search.html')

def search(request):
    if request.GET['name']:
        name = request.GET['name']
        doctors = Doctor.objects.filter(name=name)
        return render(request, 'hospitalApp/results.html', {'doctors': doctors, 'name': name})
    else:
        response = "No existe ese nombre"
        return render(request, 'hospitalApp/results.html', {'response': response})
    return render(request, 'hospitalApp/doctors_list.html')

def patientSearchResults(request):
    return render(request, 'hospitalApp/patient_search.html')

def patientSearch(request):
    if request.GET['name']:
        name = request.GET['name']
        patients = Patient.objects.filter(name=name)
        return render(request, 'hospitalApp/patient_results.html', {'patients': patients, 'name': name})
    else:
        response = "No existe ese nombre"
        return render(request, 'hospitalApp/patient_results.html', {'response': response})
    return render(request, 'hospitalApp/patients_list.html')


def parentSearchResults(request):
    return render(request, 'hospitalApp/parent_search.html')

def parentSearch(request):
    if request.GET['name']:
        name = request.GET['name']
        parents = Parent.objects.filter(name=name)
        return render(request, 'hospitalApp/parent_results.html', {'parents': parents, 'name': name})
    else:
        response = "No existe ese nombre"
        return render(request, 'hospitalApp/parent_results.html', {'response': response})
    return render(request, 'hospitalApp/parent_list.html')
