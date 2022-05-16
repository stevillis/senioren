from medicine.models import Patient, PatientHistory


def create_patient_history(patient: Patient, insert: bool = False) -> None:
    user = patient.created_by if insert else patient.updated_by

    PatientHistory.objects.create(
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
        created_at=patient.created_at,
        created_by=user,
        updated_at=patient.updated_at,
        updated_by=patient.updated_by,
        is_active=patient.is_active,
        deactivated_by=patient.deactivated_by,
        patient=patient,
    )
