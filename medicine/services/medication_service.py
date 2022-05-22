from ..models import Medication
from .history.medication_history_service import create_medication_history
from .util_service import get_object_by_id_or_404


def get_medication_none():
    return Medication.objects.none()


def get_all_medications():
    return Medication.active_manager.all()


def list_medications():
    return get_all_medications()


def get_medication_by_id(pk):
    return get_object_by_id_or_404(Medication, pk)


def create_medication(medication):
    created_medication = Medication.objects.create(
        schedule=medication.schedule,
        observation=medication.observation,
        patient=medication.patient,
        nursing_professional=medication.nursing_professional,
        created_by=medication.created_by,
        is_active=medication.is_active,
    )

    for medicine in medication.medicines.all():
        created_medication.medicines.add(medicine)
    created_medication.save()

    create_medication_history(created_medication, insert=True)


def update_medication(old_medication, new_medication):
    old_medication.schedule = new_medication.schedule
    old_medication.observation = new_medication.observation
    old_medication.patient = new_medication.patient
    old_medication.nursing_professional = new_medication.nursing_professional
    old_medication.updated_by = new_medication.updated_by

    old_medication.medicines.clear()
    for medicine in new_medication.medicines:
        old_medication.medicines.add(medicine)

    old_medication.save(force_update=True)
    create_medication_history(old_medication)


def deactivate_medication(medication, user):
    medication.is_active = False
    medication.deactivated_by = user
    medication.save(force_update=True)
    create_medication_history(medication)
