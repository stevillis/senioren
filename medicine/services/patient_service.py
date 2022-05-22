from ..models import Patient
from .history.patient_history_service import create_patient_history
from .util_service import get_object_by_id_or_404


def get_patient_none():
    return Patient.objects.none()


def get_all_patients():
    return Patient.active_manager.all()


def list_patients():
    return get_all_patients()


def get_patient_by_id(pk):
    return get_object_by_id_or_404(Patient, pk)


def create_patient(patient):
    created_patient = Patient.objects.create(
        name=patient.name,
        social_name=patient.social_name,
        cpf=patient.cpf,
        rg=patient.rg,
        birth_date=patient.birth_date,
        marital_status=patient.marital_status,
        place_of_birth=patient.place_of_birth,
        gender=patient.gender,
        phone=patient.phone,
        observation=patient.observation,
        created_by=patient.created_by,
        is_active=patient.is_active,
    )
    create_patient_history(created_patient, insert=True)


def update_patient(old_patient, new_patient):
    old_patient.name = new_patient.name
    old_patient.social_name = new_patient.social_name
    old_patient.cpf = new_patient.cpf
    old_patient.rg = new_patient.rg
    old_patient.birth_date = new_patient.birth_date
    old_patient.marital_status = new_patient.marital_status
    old_patient.place_of_birth = new_patient.place_of_birth
    old_patient.gender = new_patient.gender
    old_patient.phone = new_patient.phone
    old_patient.observation = new_patient.observation
    old_patient.updated_by = new_patient.updated_by
    old_patient.save(force_update=True)
    create_patient_history(old_patient)


def deactivate_patient(patient, user):
    patient.is_active = False
    patient.deactivated_by = user
    patient.save(force_update=True)
    create_patient_history(patient)
