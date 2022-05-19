from ..models import MedicalEvaluation
from .history.medical_evaluation_history_service import \
    create_medical_evaluation_history
from .util_service import get_object_by_id_or_404


def get_medical_evaluation_none():
    return MedicalEvaluation.objects.none()


def get_all_medical_evaluations():
    return MedicalEvaluation.active_manager.all().order_by('-schedule', '-created_at')


def list_medical_evaluations():
    return get_all_medical_evaluations()


def get_medical_evaluation_by_id(pk):
    return get_object_by_id_or_404(MedicalEvaluation, pk)


def create_medical_evaluation(medical_evaluation):
    created_medical_evaluation = MedicalEvaluation.objects.create(
        schedule=medical_evaluation.schedule,
        heart_pressure=medical_evaluation.heart_pressure,
        glucose=medical_evaluation.glucose,
        observation=medical_evaluation.observation,
        patient=medical_evaluation.patient,
        nursing_professional=medical_evaluation.nursing_professional,
        created_by=medical_evaluation.created_by,
        is_active=medical_evaluation.is_active,
    )
    create_medical_evaluation_history(created_medical_evaluation, insert=True)


def update_medical_evaluation(old_medical_evaluation, new_medical_evaluation):
    old_medical_evaluation.schedule = new_medical_evaluation.schedule
    old_medical_evaluation.heart_pressure = new_medical_evaluation.heart_pressure
    old_medical_evaluation.glucose = new_medical_evaluation.glucose
    old_medical_evaluation.observation = new_medical_evaluation.observation
    old_medical_evaluation.patient = new_medical_evaluation.patient
    old_medical_evaluation.nursing_professional = new_medical_evaluation.nursing_professional
    old_medical_evaluation.updated_by = new_medical_evaluation.updated_by
    old_medical_evaluation.save(force_update=True)
    create_medical_evaluation_history(old_medical_evaluation)


def deactivate_medical_evaluation(medical_evaluation, user):
    medical_evaluation.is_active = False
    medical_evaluation.deactivated_by = user
    medical_evaluation.save(force_update=True)
    create_medical_evaluation_history(medical_evaluation)
