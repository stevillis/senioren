from typing import Tuple

from dal import autocomplete
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django_serverside_datatable.views import ServerSideDatatableView
from medicine.entities import patient
from medicine.forms.patient_forms import PatientForm
from medicine.models import Patient
from medicine.services import patient_service
from medicine.views.utils import clean_masked_inputs_form


def get_cleaned_data(form: PatientForm) -> Tuple:
    name = form.cleaned_data['name']
    social_name = form.cleaned_data['social_name']
    cpf = form.cleaned_data['cpf']
    rg = form.cleaned_data['rg']
    birth_date = form.cleaned_data['birth_date']
    marital_status = form.cleaned_data['marital_status']
    place_of_birth = form.cleaned_data['place_of_birth']
    gender = form.cleaned_data['gender']
    phone = form.cleaned_data['phone']
    observation = form.cleaned_data['observation']

    return (
        name,
        social_name,
        cpf,
        rg,
        birth_date,
        marital_status,
        place_of_birth,
        gender,
        phone,
        observation
    )


def list_patients(request: WSGIRequest) -> HttpResponse:
    patients = patient_service.list_patients()
    context = {
        'model': Patient,
        'patients': patients
    }
    return render(request, 'templates/patient/list_patients.html', context)


def patient_detail(request: WSGIRequest, pk: int) -> HttpResponse:
    found_patient = patient_service.get_patient_by_id(pk)
    context = {
        'patient': found_patient,
    }
    return render(request, 'templates/patient/patient_detail.html', context)


def create_patient(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = PatientForm(clean_masked_inputs_form(request))
        if form.is_valid():
            (name,
             social_name,
             cpf,
             rg,
             birth_date,
             marital_status,
             place_of_birth,
             gender,
             phone,
             observation
             ) = get_cleaned_data(form)
            new_patient = patient.Patient(
                name=name,
                social_name=social_name,
                cpf=cpf,
                rg=rg,
                birth_date=birth_date,
                marital_status=marital_status,
                place_of_birth=place_of_birth,
                gender=gender,
                phone=phone,
                observation=observation,
                created_at=None,
                updated_at=None,
                created_by=request.user,
                updated_by=None,
                is_active=True,
                deactivated_by=None,
            )
            patient_service.create_patient(new_patient)
            return redirect('medicine:patient-list')
    else:
        form = PatientForm()
    context = {
        'form': form,
        'is_edit': False,
    }
    return render(request, 'templates/patient/form_patient.html', context)


def update_patient(request: WSGIRequest, pk: int) -> HttpResponse:
    old_patient = patient_service.get_patient_by_id(pk)
    old_patient.birth_date = old_patient.birth_date.strftime("%Y-%m-%d")
    form = PatientForm(
        clean_masked_inputs_form(request) or None,
        instance=old_patient
    )
    if request.method == 'POST':
        if form.is_valid():
            (name,
             social_name,
             cpf,
             rg,
             birth_date,
             marital_status,
             place_of_birth,
             gender,
             phone,
             observation
             ) = get_cleaned_data(form)
            new_patient = patient.Patient(
                name=name,
                social_name=social_name,
                cpf=cpf,
                rg=rg,
                birth_date=birth_date,
                marital_status=marital_status,
                place_of_birth=place_of_birth,
                gender=gender,
                phone=phone,
                observation=observation,
                created_at=old_patient.created_at,
                updated_at=None,
                created_by=old_patient.created_by,
                updated_by=request.user,
                is_active=old_patient.is_active,
                deactivated_by=old_patient.deactivated_by,
            )
            patient_service.update_patient(old_patient, new_patient)
            return redirect('medicine:patient-list')
    context = {
        'form': form,
        'is_edit': True,
    }
    return render(request, 'templates/patient/form_patient.html', context)


def deactivate_patient(request: WSGIRequest, pk: int) -> HttpResponse:
    found_patient = patient_service.get_patient_by_id(pk)
    if request.method == 'POST':
        user = request.user
        found_patient.updated_by = user
        patient_service.deactivate_patient(found_patient, user)
        return redirect('medicine:patient-list')
    context = {
        'patient': found_patient,
    }
    return render(request, "templates/patient/deactivate_patient.html", context)


class PatientListView(ServerSideDatatableView):
    queryset = patient_service.get_all_patients()
    model = Patient
    columns = [
        'id',
        'name',
        'cpf',
        'birth_date',
        'phone',
    ]


class PatientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return patient_service.get_patient_none()

        qs = patient_service.get_all_patients()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
