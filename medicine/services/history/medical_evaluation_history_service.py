from medicine.models import MedicalEvaluation, MedicalEvaluationHistory


def create_medical_evaluation_history(medical_evaluation: MedicalEvaluation, insert: bool = False) -> None:
    user = medical_evaluation.created_by if insert else medical_evaluation.updated_by

    MedicalEvaluationHistory.objects.create(
        schedule=medical_evaluation.schedule,
        heart_pressure=medical_evaluation.heart_pressure,
        glucose=medical_evaluation.glucose,
        observation=medical_evaluation.observation,
        patient=medical_evaluation.patient,
        nursing_professional=medical_evaluation.nursing_professional,
        created_at=medical_evaluation.created_at,
        created_by=user,
        updated_at=medical_evaluation.updated_at,
        updated_by=medical_evaluation.updated_by,
        is_active=medical_evaluation.is_active,
        deactivated_by=medical_evaluation.deactivated_by,
        medical_evaluation=medical_evaluation,
    )
