from daterangefilter.filters import DateRangeFilter
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from medicine.models import (MedicalEvaluation, Medication, Medicine,
                             NursingProfessional, Patient)

BASE_FIELDS = ['is_active', ]
READ_ONLY_BASE_FIELDS = ['created_at', 'updated_at', ]


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance

    return Wrapper


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'batch', 'expiration_date', 'stock_qty', ] + BASE_FIELDS
    list_display = ('name', 'description', 'batch', 'expiration_date', 'stock_qty',)
    list_filter = [
        'batch',
        ('expiration_date', DateRangeFilter)
    ]
    search_fields = ('name', 'description',)


@admin.register(MedicalEvaluation)
class MedicalEvaluationAdmin(admin.ModelAdmin):
    fields = ['nursing_professional', 'patient', 'schedule', 'heart_pressure', 'glucose', 'observation', ] + BASE_FIELDS
    list_display = ('get_patient_name', 'schedule', 'heart_pressure', 'glucose', 'observation',)
    list_filter = [
        ('nursing_professional__name', custom_titled_filter(_('Nursing Professional'))),
        ('schedule', DateRangeFilter)
    ]
    search_fields = ('nursing_professional__name', 'patient__name', 'patient__cpf',)

    @admin.display(description=_('Patient'), ordering='patient__name')
    def get_patient_name(self, obj):
        return obj.patient.name

    @admin.display(description=_('CPF'), ordering='patient__cpf')
    def get_patient_cpf(self, obj):
        return obj.patient.cpf

    @admin.display(description=_('Nursing Professional'), ordering='nursing_professional__name')
    def get_nursing_professional_name(self, obj):
        return obj.nursing_professional.name


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    fields = ['name', 'social_name', 'cpf', 'rg', 'birth_date', 'marital_status', 'place_of_birth', 'gender', 'phone',
              'observation'] + BASE_FIELDS
    list_display = ('name', 'cpf', 'gender', 'marital_status', 'birth_date', 'phone',)
    list_filter = [
        'gender',
        'marital_status',
        ('birth_date', DateRangeFilter)
    ]
    search_fields = ('name', 'cpf', 'rg')

    def save_model(self, request, obj, form, change):
        if obj.gender == '':  # set default value for unselected gender
            obj.gender = -1
        super().save_model(request, obj, form, change)


@admin.register(NursingProfessional)
class NursingProfessionalAdmin(admin.ModelAdmin):
    fields = ['name', 'coren', ] + BASE_FIELDS
    list_display = ('name', 'coren',)
    # list_filter = [] # TODO: decide wich fields can be used here, if necessary
    search_fields = ('name', 'coren',)


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    fields = ['nursing_professional', 'patient', 'medicine', 'schedule', 'observation', ] + BASE_FIELDS
    list_display = ('get_patient_name', 'get_nursing_professional_name', 'schedule', 'observation',)
    list_filter = [
        ('nursing_professional__name', custom_titled_filter(_('Nursing Professional'))),
        ('schedule', DateRangeFilter)
    ]
    search_fields = ('nursing_professional__name', 'patient__name', 'medicine__name', 'observation',)

    @admin.display(description=_('Patient'), ordering='patient__name')
    def get_patient_name(self, obj):
        return obj.patient.name

    @admin.display(description=_('Nursing Professional'), ordering='nursing_professional__name')
    def get_nursing_professional_name(self, obj):
        return obj.nursing_professional.name
