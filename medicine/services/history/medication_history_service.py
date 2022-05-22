from medicine.models import Medication, MedicationHistory


def create_medication_history(medication: Medication, insert: bool = False) -> None:
    user = medication.created_by if insert else medication.updated_by

    created_history = MedicationHistory.objects.create(
        schedule=medication.schedule,
        observation=medication.observation,
        patient=medication.patient,
        nursing_professional=medication.nursing_professional,
        created_at=medication.created_at,
        created_by=user,
        updated_at=medication.updated_at,
        updated_by=medication.updated_by,
        is_active=medication.is_active,
        deactivated_by=medication.deactivated_by,
        medication=medication,
    )

    for medicine in medication.medicines.all():
        created_history.medicines.add(medicine)
    created_history.save()
