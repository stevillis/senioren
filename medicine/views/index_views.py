import datetime
from typing import Tuple

from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render
from medicine.models import MedicalEvaluation, Medication
from medicine.services import medication_service


def _get_amount_created_today(model: Tuple[Medication, MedicalEvaluation]) -> int:
    return model.active_manager.filter(
        created_at__startswith=datetime.date.today()

    ).count()


def _get_amount_created_week(model: Tuple[Medication, MedicalEvaluation]) -> int:
    return model.active_manager.filter(
        created_at__lte=datetime.datetime.now(),
        created_at__gte=F('created_at') - datetime.timedelta(7),
    ).count()


@login_required()
def index(request: WSGIRequest) -> HttpResponse:
    """
    Dashboard Page.

    Shows some abstracts about Medication and Medical Evaluation.
    """
    medications_today = _get_amount_created_today(Medication)
    medications_this_week = _get_amount_created_week(Medication)

    medical_evaluations_today = _get_amount_created_today(MedicalEvaluation)
    medical_evaluations_this_week = _get_amount_created_week(MedicalEvaluation)

    medications = medication_service.get_all_medications()

    context = {
        'medications_today': medications_today,
        'medications_this_week': medications_this_week,
        'medical_evaluations_today': medical_evaluations_today,
        'medical_evaluations_this_week': medical_evaluations_this_week,

        'model': Medication,
        'medications': medications
    }

    return render(
        request=request,
        template_name='index.html',
        context=context
    )
