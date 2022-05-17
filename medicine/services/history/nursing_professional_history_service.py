from medicine.models import NursingProfessional, NursingProfessionalHistory


def create_nursing_professional_history(nursing_professional: NursingProfessional, insert: bool = False) -> None:
    user = nursing_professional.created_by if insert else nursing_professional.updated_by

    NursingProfessionalHistory.objects.create(
        name=nursing_professional.name,
        coren=nursing_professional.coren,
        created_at=nursing_professional.created_at,
        created_by=user,
        updated_at=nursing_professional.updated_at,
        updated_by=nursing_professional.updated_by,
        is_active=nursing_professional.is_active,
        deactivated_by=nursing_professional.deactivated_by,
        nursing_professional=nursing_professional,
    )
