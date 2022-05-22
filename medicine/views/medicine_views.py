from typing import Tuple

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django_serverside_datatable.views import ServerSideDatatableView
from medicine.entities import medicine
from medicine.forms.medicine_forms import MedicineForm
from medicine.models import Medicine
from medicine.services import medicine_service


def get_cleaned_data(form: MedicineForm) -> Tuple:
    name = form.cleaned_data['name']
    description = form.cleaned_data['description']
    batch = form.cleaned_data['batch']
    expiration_date = form.cleaned_data['expiration_date']
    stock_qty = form.cleaned_data['stock_qty']

    return (
        name,
        description,
        batch,
        expiration_date,
        stock_qty
    )


@login_required
def list_medicines(request: WSGIRequest) -> HttpResponse:
    medicines = medicine_service.list_medicines(request)
    context = {
        'model': Medicine,
        'medicines': medicines
    }

    return render(
        request=request,
        template_name='templates/medicine/list_medicines.html',
        context=context
    )


@login_required
def medicine_detail(request: WSGIRequest, pk: int) -> HttpResponse:
    found_medicine = medicine_service.get_medicine_by_id(pk)
    context = {
        'medicine': found_medicine,
    }

    return render(
        request=request,
        template_name='templates/medicine/medicine_detail.html',
        context=context
    )


@login_required
def create_medicine(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            (
                name,
                description,
                batch,
                expiration_date,
                stock_qty
            ) = get_cleaned_data(form)
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

            return redirect('medicine:medicine-list')
    else:
        form = MedicineForm()
    context = {
        'form': form,
        'is_edit': False,
    }

    return render(
        request=request,
        template_name='templates/medicine/form_medicine.html',
        context=context
    )


@login_required
def update_medicine(request: WSGIRequest, pk: int) -> HttpResponse:
    old_medicine = medicine_service.get_medicine_by_id(pk)
    old_medicine.expiration_date = old_medicine.expiration_date.strftime(
        "%Y-%m-%d"
    )
    form = MedicineForm(request.POST or None, instance=old_medicine)
    if request.method == 'POST':
        if form.is_valid():
            (
                name,
                description,
                batch,
                expiration_date,
                stock_qty
            ) = get_cleaned_data(form)
            new_medicine = medicine.Medicine(
                name=name,
                description=description,
                batch=batch,
                expiration_date=expiration_date,
                stock_qty=stock_qty,
                created_at=old_medicine.created_at,
                updated_at=None,
                created_by=old_medicine.created_by,
                updated_by=request.user,
                is_active=old_medicine.is_active,
                deactivated_by=old_medicine.deactivated_by,
            )
            medicine_service.update_medicine(old_medicine, new_medicine)

            return redirect('medicine:medicine-list')

    context = {
        'form': form,
        'is_edit': True,
    }

    return render(
        request=request,
        template_name='templates/medicine/form_medicine.html',
        context=context
    )


@login_required
def deactivate_medicine(request: WSGIRequest, pk: int) -> HttpResponse:
    found_medicine = medicine_service.get_medicine_by_id(pk)
    if request.method == 'POST':
        user = request.user
        found_medicine.updated_by = user
        medicine_service.deactivate_medicine(found_medicine, user)

        return redirect('medicine:medicine-list')

    context = {
        'medicine': found_medicine,
    }

    return render(
        request=request,
        template_name="templates/medicine/deactivate_medicine.html",
        context=context
    )


class MedicineListView(LoginRequiredMixin, ServerSideDatatableView):
    queryset = medicine_service.get_all_medicines()
    model = Medicine
    columns = [
        'id',
        'name',
        'description',
        'batch',
        'expiration_date',
        'stock_qty',
    ]
