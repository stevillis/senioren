from ..models import NursingProfessional
from .history.nursing_professional_history_service import \
    create_nursing_professional_history
from .util_service import get_object_by_id_or_404


def get_nursing_professional_none():
    return NursingProfessional.objects.none()


def get_all_nursing_professionals():
    return NursingProfessional.active_manager.all()


def list_nursing_professionals():
    return get_all_nursing_professionals()


def get_nursing_professional_by_id(pk):
    return get_object_by_id_or_404(NursingProfessional, pk)


def create_nursing_professional(nursing_professional):
    created_nursing_professional = NursingProfessional.objects.create(
        name=nursing_professional.name,
        coren=nursing_professional.coren,
        created_by=nursing_professional.created_by,
        is_active=nursing_professional.is_active,
    )
    create_nursing_professional_history(
        created_nursing_professional, insert=True
    )


def update_nursing_professional(old_nursing_professional, new_nursing_professional):
    old_nursing_professional.name = new_nursing_professional.name
    old_nursing_professional.coren = new_nursing_professional.coren
    old_nursing_professional.updated_by = new_nursing_professional.updated_by
    old_nursing_professional.save(force_update=True)
    create_nursing_professional_history(old_nursing_professional)


def deactivate_nursing_professional(nursing_professional, user):
    nursing_professional.is_active = False
    nursing_professional.deactivated_by = user
    nursing_professional.save(force_update=True)
    create_nursing_professional_history(nursing_professional)
