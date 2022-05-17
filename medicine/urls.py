from django.urls import path

from .views.medicine_views import (MedicineListView, create_medicine,
                                   deactivate_medicine, list_medicines,
                                   medicine_detail, update_medicine)
from .views.nursing_professional_views import (NursingProfessionalListView,
                                               create_nursing_professional,
                                               deactivate_nursing_professional,
                                               list_nursing_professionals,
                                               nursing_professional_detail,
                                               update_nursing_professional)
from .views.patient_views import (PatientListView, create_patient,
                                  deactivate_patient, list_patients,
                                  patient_detail, update_patient)

app_name = 'medicine'

prefix_medicine_url = 'medicine'
prefix_patient_url = 'patient'
prefix_nursing_professional_url = 'nursing-professional'

urlpatterns = [
    # Medicine
    path(
        route=f'{prefix_medicine_url}/list/',
        view=list_medicines,
        name='medicine-list'
    ),
    path(
        route=f'{prefix_medicine_url}/detail/<int:pk>/',
        view=medicine_detail,
        name='medicine-detail'
    ),
    path(
        route=f'{prefix_medicine_url}/create/',
        view=create_medicine,
        name='medicine-create'
    ),
    path(
        route=f'{prefix_medicine_url}/update/<int:pk>/',
        view=update_medicine,
        name='medicine-update'
    ),
    path(
        route=f'{prefix_medicine_url}/deactivate/<int:pk>/',
        view=deactivate_medicine,
        name='medicine-deactivate'
    ),
    path(
        route=f'{prefix_medicine_url}/data/',
        view=MedicineListView.as_view(),
        name='medicine-data'
    ),

    # Patient
    path(
        route=f'{prefix_patient_url}/list/',
        view=list_patients,
        name='patient-list'),
    path(
        route=f'{prefix_patient_url}/detail/<int:pk>/',
        view=patient_detail,
        name='patient-detail'),
    path(
        route=f'{prefix_patient_url}/create/',
        view=create_patient,
        name='patient-create'),
    path(
        route=f'{prefix_patient_url}/update/<int:pk>/',
        view=update_patient,
        name='patient-update'),
    path(
        route=f'{prefix_patient_url}/deactivate/<int:pk>/',
        view=deactivate_patient,
        name='patient-deactivate'
    ),
    path(
        route=f'{prefix_patient_url}/data/',
        view=PatientListView.as_view(),
        name='patient-data'
    ),

    # Nursing Professional
    path(
        route=f'{prefix_nursing_professional_url}/list/',
        view=list_nursing_professionals,
        name='nursing-professional-list'),
    path(
        route=f'{prefix_nursing_professional_url}/detail/<int:pk>/',
        view=nursing_professional_detail,
        name='nursing-professional-detail'),
    path(
        route=f'{prefix_nursing_professional_url}/create/',
        view=create_nursing_professional,
        name='nursing-professional-create'),
    path(
        route=f'{prefix_nursing_professional_url}/update/<int:pk>/',
        view=update_nursing_professional,
        name='nursing-professional-update'),
    path(
        route=f'{prefix_nursing_professional_url}/deactivate/<int:pk>/',
        view=deactivate_nursing_professional,
        name='nursing-professional-deactivate'
    ),
    path(
        route=f'{prefix_nursing_professional_url}/data/',
        view=NursingProfessionalListView.as_view(),
        name='nursing-professional-data'
    ),
]
