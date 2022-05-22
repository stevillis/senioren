import medicine.filters as filters

from ..models import Medicine
from .history.medicine_history_service import create_medicine_history
from .util_service import get_object_by_id_or_404


def get_medicine_none():
    return Medicine.objects.none()


def get_all_medicines():
    return Medicine.active_manager.all()


def list_medicines(request):
    medicines = get_all_medicines()
    filtered_medicines = filters.MedicineFilter(
        data=request.GET,
        queryset=medicines
    )
    return filtered_medicines


def get_medicine_by_id(pk):
    return get_object_by_id_or_404(Medicine, pk)


def create_medicine(medicine):
    created_medicine = Medicine.objects.create(
        name=medicine.name,
        description=medicine.description,
        batch=medicine.batch,
        expiration_date=medicine.expiration_date,
        stock_qty=medicine.stock_qty,
        created_by=medicine.created_by,
        is_active=medicine.is_active,
    )
    create_medicine_history(created_medicine, insert=True)


def update_medicine(old_medicine, new_medicine):
    old_medicine.name = new_medicine.name
    old_medicine.description = new_medicine.description
    old_medicine.batch = new_medicine.batch
    old_medicine.expiration_date = new_medicine.expiration_date
    old_medicine.stock_qty = new_medicine.stock_qty
    old_medicine.updated_by = new_medicine.updated_by
    old_medicine.save(force_update=True)
    create_medicine_history(old_medicine)


def deactivate_medicine(medicine, user):
    medicine.is_active = False
    medicine.deactivated_by = user
    medicine.save(force_update=True)
    create_medicine_history(medicine)
