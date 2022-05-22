from typing import Tuple

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django_serverside_datatable.views import ServerSideDatatableView
from medicine.entities import medication
from medicine.forms.medication_forms import MedicationForm
from medicine.models import Medication
from medicine.services import medication_service


def get_cleaned_data(form: MedicationForm) -> Tuple:
    schedule = form.cleaned_data['schedule']
    observation = form.cleaned_data['observation']
    medicines = form.cleaned_data['medicines']
    patient = form.cleaned_data['patient']
    nursing_professional = form.cleaned_data['nursing_professional']

    return (
        schedule,
        observation,
        medicines,
        patient,
        nursing_professional,
    )


@login_required
def list_medications(request: WSGIRequest) -> HttpResponse:
    medications = medication_service.list_medications()
    context = {
        'model': Medication,
        'medications': medications
    }

    return render(
        request=request,
        template_name='templates/medication/list_medications.html',
        context=context
    )


@login_required
def medication_detail(request: WSGIRequest, pk: int) -> HttpResponse:
    found_medication = medication_service.get_medication_by_id(
        pk
    )
    context = {
        'medication': found_medication,
    }

    return render(
        request=request,
        template_name='templates/medication/medication_detail.html',
        context=context
    )


@login_required
def create_medication(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            (
                schedule,
                observation,
                medicines,
                patient,
                nursing_professional,
            ) = get_cleaned_data(form)

            new_medication = medication.Medication(
                schedule=schedule,
                observation=observation,
                medicines=medicines,
                patient=patient,
                nursing_professional=nursing_professional,
                created_at=None,
                updated_at=None,
                created_by=request.user,
                updated_by=None,
                is_active=True,
                deactivated_by=None,
            )
            medication_service.create_medication(new_medication)

            return redirect('medicine:medication-list')
    else:
        form = MedicationForm()

    context = {
        'form': form,
        'is_edit': False,
    }

    return render(
        request=request,
        template_name='templates/medication/form_medication.html',
        context=context
    )


@login_required
def update_medication(request: WSGIRequest, pk: int) -> HttpResponse:
    old_medication = medication_service.get_medication_by_id(
        pk
    )
    form = MedicationForm(
        request.POST or None,
        instance=old_medication
    )
    if request.method == 'POST':
        if form.is_valid():
            (
                schedule,
                observation,
                medicines,
                patient,
                nursing_professional,
            ) = get_cleaned_data(form)

            new_medication = medication.Medication(
                schedule=schedule,
                observation=observation,
                medicines=medicines,
                patient=patient,
                nursing_professional=nursing_professional,
                created_at=old_medication.created_at,
                updated_at=None,
                created_by=old_medication.created_by,
                updated_by=request.user,
                is_active=old_medication.is_active,
                deactivated_by=old_medication.deactivated_by,
            )
            medication_service.update_medication(
                old_medication, new_medication
            )

            return redirect('medicine:medication-list')

    context = {
        'form': form,
        'is_edit': True,
    }

    return render(
        request=request,
        template_name='templates/medication/form_medication.html',
        context=context
    )


@login_required
def deactivate_medication(request: WSGIRequest, pk: int) -> HttpResponse:
    found_medication = medication_service.get_medication_by_id(
        pk
    )
    if request.method == 'POST':
        user = request.user
        found_medication.updated_by = user
        medication_service.deactivate_medication(
            found_medication, user)

        return redirect('medicine:medication-list')

    context = {
        'medication': found_medication,
    }

    return render(
        request=request,
        template_name="templates/medication/deactivate_medication.html",
        context=context
    )


class MedicationListView(LoginRequiredMixin, ServerSideDatatableView):
    queryset = medication_service.get_all_medications()
    model = Medication
    columns = [
        'id',
        'schedule',
        'patient__name',
        'nursing_professional__name',
    ]
