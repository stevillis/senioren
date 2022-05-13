from typing import Tuple

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from medicine.entities import medicine
from medicine.forms.medicine_forms import MedicineForm
from medicine.models import Medicine
from medicine.services import medicine_service


def list_medicines(request: HttpRequest) -> HttpResponse:
    medicines = medicine_service.list_medicines(request)
    context = {
        'model': Medicine,
        'medicines': medicines
    }
    return render(request, "templates/medicine/list_medicines.html", context)


def get_cleaned_data(form: MedicineForm) -> Tuple:
    name = form.cleaned_data["name"]
    description = form.cleaned_data["description"]
    batch = form.cleaned_data["batch"]
    expiration_date = form.cleaned_data["expiration_date"]
    stock_qty = form.cleaned_data["stock_qty"]

    return name, description, batch, expiration_date, stock_qty


def medicine_detail(request: HttpRequest, pk: int) -> HttpResponse:
    found_medicine = medicine_service.get_medicine_by_id(pk)
    context = {
        'medicine': found_medicine,
    }
    return render(request, "templates/medicine/medicine_detail.html", context)


def create_medicine(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            name, description, batch, expiration_date, stock_qty = get_cleaned_data(
                form)
            new_medicine = medicine.Medicine(
                name=name,
                description=description,
                batch=batch,
                expiration_date=expiration_date,
                stock_qty=stock_qty,
                created_at=None,
                updated_at=None,
                created_by=request.user,
                updated_by=None,
                is_active=True,
                deactivated_by=None,
            )
            medicine_service.create_medicine(new_medicine)
            return redirect("medicine:list")
    else:
        form = MedicineForm()
    context = {
        'form': form,
        'is_edit': False,
    }
    return render(request, "templates/medicine/form_medicine.html", context)


def update_medicine(request):
    # TODO
    pass


def deactivate_medicine(request):
    # TODO
    pass
