from typing import Tuple

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django_serverside_datatable.views import ServerSideDatatableView
from medicine.entities import medical_evaluation
from medicine.forms.medical_evaluation_forms import MedicalEvaluationForm
from medicine.models import MedicalEvaluation
from medicine.services import medical_evaluation_service


def get_cleaned_data(form: MedicalEvaluationForm) -> Tuple:
    schedule = form.cleaned_data['schedule']
    heart_pressure = form.cleaned_data['heart_pressure']
    glucose = form.cleaned_data['glucose']
    observation = form.cleaned_data['observation']
    patient = form.cleaned_data['patient']
    nursing_professional = form.cleaned_data['nursing_professional']

    return (
        schedule,
        heart_pressure,
        glucose,
        observation,
        patient,
        nursing_professional,
    )


@login_required()
def list_medical_evaluations(request: WSGIRequest) -> HttpResponse:
    medical_evaluations = medical_evaluation_service.list_medical_evaluations()
    context = {
        'model': MedicalEvaluation,
        'medical_evaluations': medical_evaluations
    }

    return render(
        request=request,
        template_name='templates/medical_evaluation/list_medical_evaluations.html',
        context=context
    )


@login_required()
def medical_evaluation_detail(request: WSGIRequest, pk: int) -> HttpResponse:
    found_medical_evaluation = medical_evaluation_service.get_medical_evaluation_by_id(
        pk)
    context = {
        'medical_evaluation': found_medical_evaluation,
    }

    return render(
        request=request,
        template_name='templates/medical_evaluation/medical_evaluation_detail.html',
        context=context
    )


@login_required()
def create_medical_evaluation(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = MedicalEvaluationForm(request.POST)
        if form.is_valid():
            (
                schedule,
                heart_pressure,
                glucose,
                observation,
                patient,
                nursing_professional,
            ) = get_cleaned_data(form)

            new_medical_evaluation = medical_evaluation.MedicalEvaluation(
                schedule=schedule,
                heart_pressure=heart_pressure,
                glucose=glucose,
                observation=observation,
                patient=patient,
                nursing_professional=nursing_professional,
                created_at=None,
                updated_at=None,
                created_by=request.user,
                updated_by=None,
                is_active=True,
                deactivated_by=None,
            )
            medical_evaluation_service.create_medical_evaluation(
                new_medical_evaluation
            )

            return redirect('medicine:medical-evaluation-list')
    else:
        form = MedicalEvaluationForm()
    context = {
        'form': form,
        'is_edit': False,
    }

    return render(
        request=request,
        template_name='templates/medical_evaluation/form_medical_evaluation.html',
        context=context
    )


@login_required()
def update_medical_evaluation(request: WSGIRequest, pk: int) -> HttpResponse:
    old_medical_evaluation = medical_evaluation_service.get_medical_evaluation_by_id(
        pk
    )
    form = MedicalEvaluationForm(
        request.POST or None, instance=old_medical_evaluation
    )
    if request.method == 'POST':
        if form.is_valid():
            (
                schedule,
                heart_pressure,
                glucose,
                observation,
                patient,
                nursing_professional,
            ) = get_cleaned_data(form)

            new_medical_evaluation = medical_evaluation.MedicalEvaluation(
                schedule=schedule,
                heart_pressure=heart_pressure,
                glucose=glucose,
                observation=observation,
                patient=patient,
                nursing_professional=nursing_professional,
                created_at=old_medical_evaluation.created_at,
                updated_at=None,
                created_by=old_medical_evaluation.created_by,
                updated_by=request.user,
                is_active=old_medical_evaluation.is_active,
                deactivated_by=old_medical_evaluation.deactivated_by,
            )
            medical_evaluation_service.update_medical_evaluation(
                old_medical_evaluation, new_medical_evaluation)

            return redirect('medicine:medical-evaluation-list')

    context = {
        'form': form,
        'is_edit': True,
    }

    return render(
        request=request,
        template_name='templates/medical_evaluation/form_medical_evaluation.html',
        context=context
    )


@login_required()
def deactivate_medical_evaluation(request: WSGIRequest, pk: int) -> HttpResponse:
    found_medical_evaluation = medical_evaluation_service.get_medical_evaluation_by_id(
        pk
    )
    if request.method == 'POST':
        user = request.user
        found_medical_evaluation.updated_by = user
        medical_evaluation_service.deactivate_medical_evaluation(
            found_medical_evaluation, user)

        return redirect('medicine:medical-evaluation-list')

    context = {
        'medical_evaluation': found_medical_evaluation,
    }

    return render(
        request=request,
        template_name="templates/medical_evaluation/deactivate_medical_evaluation.html",
        context=context
    )


class MedicalEvaluationListView(LoginRequiredMixin, ServerSideDatatableView):
    queryset = medical_evaluation_service.get_all_medical_evaluations()
    model = MedicalEvaluation
    columns = [
        'id',
        'schedule',
        'heart_pressure',
        'glucose',
        'observation',
        'patient__name',
        'nursing_professional__name',
    ]
