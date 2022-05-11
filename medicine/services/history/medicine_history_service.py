from medicine.models import Medicine, MedicineHistory


def create_medicine_history(medicine: Medicine, insert: bool = False) -> None:
    user = medicine.created_by if insert else medicine.updated_by

    MedicineHistory.objects.create(
        name=medicine.name,
        description=medicine.description,
        batch=medicine.batch,
        expiration_date=medicine.expiration_date,
        stock_qty=medicine.stock_qty,
        created_at=medicine.created_at,
        created_by=user,
        updated_at=medicine.updated_at,
        updated_by=medicine.updated_by,
        is_active=medicine.is_active,
        medicine=medicine,
    )
