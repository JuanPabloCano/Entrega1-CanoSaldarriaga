from django.urls import path, include
from .views import *
import uuid

urlpatterns = [
    path('', index, name='index'),
    path('doctors/list/', DoctorsList.as_view(), name='doctors_list'),
    path('doctor/<pk>', DoctorDetail.as_view(), name='doctor_detail'),
    path('doctor/create/', DoctorCreate.as_view(), name='doctor_create'),
    path('doctor/update/<pk>', DoctorUpdate.as_view(), name='doctor_update'),
    path('doctor/delete/<pk>', DoctorDelete.as_view(), name='doctor_delete'),
    path('patients/list/', PatientList.as_view(), name='patients_list'),
    path('patient/<pk>', PatientDetail.as_view(), name='patient_detail'),
    path('patient/create/', PatientCreate.as_view(), name='patient_create'),
    path('patient/update/<pk>', PatientUpdate.as_view(), name='patient_update'),
    path('patient/delete/<pk>', PatientDelete.as_view(), name='patient_delete'),
    path('parents/list/', ParentList.as_view(), name='parents_list'),
    path('parent/<pk>', ParentDetail.as_view(), name='parent_detail'),
    path('parent/create/', ParentCreate.as_view(), name='parent_create'),
    path('parent/update/<pk>', ParentUpdate.as_view(), name='parent_update'),
    path('parent/delete/<pk>', ParentDelete.as_view(), name='parent_delete'),
    #path('doctor/search/', DoctorSearch.as_view(), name='doctor_search')
    path('search/', search, name='search'),
    path('doctorSearch/', doctorSearchResults, name='doctorSearch'),
    path('patient/search/', patientSearch, name='patient_search'),
    path('patientSearch/', patientSearchResults, name='patient_search_results'),
    path('parent/search/', parentSearch, name='parent_search'),
    path('parentSearch/', parentSearchResults, name='parent_search_results'),
]
