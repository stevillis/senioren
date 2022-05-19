from typing import Tuple

from dal import autocomplete
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django_serverside_datatable.views import ServerSideDatatableView
from medicine.entities import nursing_professional
from medicine.forms.nursing_professional_forms import NursingProfessionalForm
from medicine.models import NursingProfessional
from medicine.services import nursing_professional_service


def get_cleaned_data(form: NursingProfessionalForm) -> Tuple:
    name = form.cleaned_data['name']
    coren = form.cleaned_data['coren']

    return (
        name,
        coren,
    )


def list_nursing_professionals(request: WSGIRequest) -> HttpResponse:
    nursing_professionals = nursing_professional_service.list_nursing_professionals()
    context = {
        'model': NursingProfessional,
        'nursing_professionals': nursing_professionals
    }
    return render(request, 'templates/nursing_professional/list_nursing_professionals.html', context)


def nursing_professional_detail(request: WSGIRequest, pk: int) -> HttpResponse:
    found_nursing_professional = nursing_professional_service.get_nursing_professional_by_id(
        pk)
    context = {
        'nursing_professional': found_nursing_professional,
    }
    return render(request, 'templates/nursing_professional/nursing_professional_detail.html', context)


def create_nursing_professional(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = NursingProfessionalForm(request.POST)
        if form.is_valid():
            name, coren = get_cleaned_data(form)
            new_nursing_professional = nursing_professional.NursingProfessional(
                name=name,
                coren=coren,
                created_at=None,
                updated_at=None,
                created_by=request.user,
                updated_by=None,
                is_active=True,
                deactivated_by=None,
            )
            nursing_professional_service.create_nursing_professional(
                new_nursing_professional)
            return redirect('medicine:nursing-professional-list')
    else:
        form = NursingProfessionalForm()
    context = {
        'form': form,
        'is_edit': False,
    }
    return render(request, 'templates/nursing_professional/form_nursing_professional.html', context)


def update_nursing_professional(request: WSGIRequest, pk: int) -> HttpResponse:
    old_nursing_professional = nursing_professional_service.get_nursing_professional_by_id(
        pk)
    form = NursingProfessionalForm(
        request.POST or None, instance=old_nursing_professional)
    if request.method == 'POST':
        if form.is_valid():
            name, coren = get_cleaned_data(form)
            new_nursing_professional = nursing_professional.NursingProfessional(
                name=name,
                coren=coren,
                created_at=old_nursing_professional.created_at,
                updated_at=None,
                created_by=old_nursing_professional.created_by,
                updated_by=request.user,
                is_active=old_nursing_professional.is_active,
                deactivated_by=old_nursing_professional.deactivated_by,
            )
            nursing_professional_service.update_nursing_professional(
                old_nursing_professional, new_nursing_professional)
            return redirect('medicine:nursing-professional-list')
    context = {
        'form': form,
        'is_edit': True,
    }
    return render(request, 'templates/nursing_professional/form_nursing_professional.html', context)


def deactivate_nursing_professional(request: WSGIRequest, pk: int) -> HttpResponse:
    found_nursing_professional = nursing_professional_service.get_nursing_professional_by_id(
        pk)
    if request.method == 'POST':
        user = request.user
        found_nursing_professional.updated_by = user
        nursing_professional_service.deactivate_nursing_professional(
            found_nursing_professional, user)
        return redirect('medicine:nursing-professional-list')
    context = {
        'nursing_professional': found_nursing_professional,
    }
    return render(request, "templates/nursing_professional/deactivate_nursing_professional.html", context)


class NursingProfessionalListView(ServerSideDatatableView):
    queryset = nursing_professional_service.get_all_nursing_professionals()
    model = NursingProfessional
    columns = [
        'id',
        'name',
        'coren',
    ]


class NursingProfessionalAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return nursing_professional_service.get_nursing_professional_none()

        qs = nursing_professional_service.get_all_nursing_professionals()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
