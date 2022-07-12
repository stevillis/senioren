from daterangefilter.filters import DateRangeFilter
from django.contrib import admin

from medicine.models import (MedicalEvaluation, MedicalEvaluationHistory,
                             Medication, MedicationHistory, Medicine,
                             MedicineHistory, NursingProfessional,
                             NursingProfessionalHistory, Patient,
                             PatientHistory)
from medicine.services.history.medical_evaluation_history_service import \
    create_medical_evaluation_history
from medicine.services.history.medication_history_service import \
    create_medication_history
from medicine.services.history.medicine_history_service import \
    create_medicine_history
from medicine.services.history.nursing_professional_history_service import \
    create_nursing_professional_history
from medicine.services.history.patient_history_service import \
    create_patient_history

BASE_FIELDS = ['is_active', ]
READ_ONLY_BASE_FIELDS = ['created_at', 'updated_at', ]


def custom_titled_filter(title):
    """Custom title for Django Admin filter"""

    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance

    return Wrapper


def set_created_by(request, obj):
    """Set request user to created_by field"""
    obj.created_by = request.user
    return obj


def set_updated_by(request, obj):
    """Set request user to updated_by field"""
    obj.updated_by = request.user
    return obj


def remove_delete_actions(actions):
    if actions.get('delete_selected'):
        del actions['delete_selected']
    if actions.get('delete_confirmation'):
        del actions['delete_confirmation']
    return actions


"""
----- Models -----
"""


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    """Medicine Model for Django Admin"""

    fields = [
        'name',
        'description',
        'batch',
        'expiration_date',
        'stock_qty',
    ] + BASE_FIELDS

    list_display = (
        'name',
        'description',
        'batch',
        'expiration_date',
        'stock_qty',
        'is_active',
    )

    list_filter = [
        'is_active',
        ('expiration_date', DateRangeFilter),
    ]

    search_fields = ('name', 'description',)

    def save_model(self, request, obj, form, change):
        obj = set_created_by(request, obj)
        if change:
            obj = set_updated_by(request, obj)
        super().save_model(request, obj, form, change)

        if change:
            create_medicine_history(obj)
        else:
            create_medicine_history(obj, insert=True)

    def _delete_model(self, request, obj):
        obj.is_active = False
        obj.deactivated_by = request.user
        obj.save()
        create_medicine_history(obj)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            self._delete_model(request, obj)

    def delete_model(self, request, obj):
        self._delete_model(request, obj)


@admin.register(MedicalEvaluation)
class MedicalEvaluationAdmin(admin.ModelAdmin):
    """MedicalEvaluation Model for Django Admin"""

    fields = [
        'nursing_professional',
        'patient',
        'schedule',
        'heart_pressure',
        'glucose',
        'observation',
    ] + BASE_FIELDS

    list_display = (
        'get_patient_name',
        'schedule',
        'heart_pressure',
        'glucose',
        'observation',
    )

    list_filter = [
        (
            'nursing_professional__name',
            custom_titled_filter('Profissional de Enfermagem')
        ),
        ('schedule', DateRangeFilter),
    ]

    search_fields = (
        'nursing_professional__name',
        'patient__name',
        'patient__cpf',
    )

    @admin.display(description='Paciente', ordering='patient__name')
    def get_patient_name(self, obj):
        """Get Patient name for list_display"""
        return obj.patient.name

    @admin.display(description='CPF', ordering='patient__cpf')
    def get_patient_cpf(self, obj):
        """Get Patient cpf for list_display"""
        return obj.patient.cpf

    @admin.display(description='Profissional de Enfermagem',
                   ordering='nursing_professional__name')
    def get_nursing_professional_name(self, obj):
        """Get Nursing Professional name for list_display"""
        return obj.nursing_professional.name

    def save_model(self, request, obj, form, change):
        obj = set_created_by(request, obj)
        if change:
            obj = set_updated_by(request, obj)
        super().save_model(request, obj, form, change)

        if change:
            create_medical_evaluation_history(obj)
        else:
            create_medical_evaluation_history(obj, insert=True)

    def _delete_model(self, request, obj):
        obj.is_active = False
        obj.deactivated_by = request.user
        obj.save()
        create_medical_evaluation_history(obj)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            self._delete_model(request, obj)

    def delete_model(self, request, obj):
        self._delete_model(request, obj)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Patient Model for Django Admin"""

    fields = [
        'name',
        'social_name',
        'cpf',
        'rg',
        'birth_date',
        'marital_status',
        'place_of_birth',
        'gender',
        'phone',
        'observation'
    ] + BASE_FIELDS

    list_display = (
        'name',
        'cpf',
        'gender',
        'marital_status',
        'birth_date',
        'phone',
        'is_active',
    )

    list_filter = [
        'gender',
        'marital_status',
        ('birth_date', DateRangeFilter),
    ]

    search_fields = ('name', 'cpf', 'rg')

    def save_model(self, request, obj, form, change):
        if obj.gender == '':  # set default value for unselected gender
            obj.gender = -1
        obj = set_created_by(request, obj)
        if change:
            obj = set_updated_by(request, obj)
        super().save_model(request, obj, form, change)

        if change:
            create_patient_history(obj)
        else:
            create_patient_history(obj, insert=True)

    def _delete_model(self, request, obj):
        obj.is_active = False
        obj.deactivated_by = request.user
        obj.save()
        create_patient_history(obj)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            self._delete_model(request, obj)

    def delete_model(self, request, obj):
        self._delete_model(request, obj)


@admin.register(NursingProfessional)
class NursingProfessionalAdmin(admin.ModelAdmin):
    """Nursing Professional Model for Django Admin"""
    fields = ['name', 'coren', ] + BASE_FIELDS

    list_display = ('name', 'coren',)

    # list_filter = [] # TODO: decide wich fields can be used here, if necessary

    search_fields = ('name', 'coren',)

    def save_model(self, request, obj, form, change):
        obj = set_created_by(request, obj)
        if change:
            obj = set_updated_by(request, obj)
        super().save_model(request, obj, form, change)

        if change:
            create_nursing_professional_history(obj)
        else:
            create_nursing_professional_history(obj, insert=True)

    def _delete_model(self, request, obj):
        obj.is_active = False
        obj.deactivated_by = request.user
        obj.save()
        create_nursing_professional_history(obj)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            self._delete_model(request, obj)

    def delete_model(self, request, obj):
        self._delete_model(request, obj)


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    """Medication Model for Django Admin"""

    fields = [
        'nursing_professional',
        'patient',
        'medicines',
        'schedule',
        'observation',
    ] + BASE_FIELDS

    list_display = (
        'get_patient_name',
        'get_nursing_professional_name',
        'schedule',
        'observation',
        'is_active',
    )

    list_filter = [
        (
            'nursing_professional__name',
            custom_titled_filter('Profissional de Enfermagem')
        ),
        ('schedule', DateRangeFilter)
    ]

    search_fields = (
        'nursing_professional__name',
        'patient__name',
        'medicine__name',
        'observation',
    )

    @admin.display(description='Paciente', ordering='patient__name')
    def get_patient_name(self, obj):
        """Get Patient name for list_display"""
        return obj.patient.name

    @admin.display(description='Profissional de Enfermagem',
                   ordering='nursing_professional__name')
    def get_nursing_professional_name(self, obj):
        """Get Nursing Professional name for list_display"""
        return obj.nursing_professional.name

    def save_model(self, request, obj, form, change):
        obj = set_created_by(request, obj)
        if change:
            obj = set_updated_by(request, obj)
        super().save_model(request, obj, form, change)

        if change:
            create_medication_history(obj)
        else:
            create_medication_history(obj, insert=True)

    def _delete_model(self, request, obj):
        obj.is_active = False
        obj.deactivated_by = request.user
        obj.save()
        create_medication_history(obj)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            self._delete_model(request, obj)

    def delete_model(self, request, obj):
        self._delete_model(request, obj)


"""
----- History Models -----
"""


@admin.register(MedicineHistory)
class MedicineHistoryAdmin(admin.ModelAdmin):
    """Medicine History Model for Django Admin"""

    fields = [
        'name',
        'description',
        'batch',
        'expiration_date',
        'stock_qty',
        'created_at',
        'created_by',
        'updated_at',
        'updated_by',
    ] + BASE_FIELDS

    list_display = (
        'name',
        'description',
        'batch',
        'expiration_date',
        'stock_qty',
    )

    list_filter = [
        ('expiration_date', DateRangeFilter),
    ]

    search_fields = ('name', 'description',)

    def save_model(self, request, obj, form, change):
        obj = set_created_by(request, obj)
        if change:
            obj = set_updated_by(request, obj)
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_actions(self, request):
        actions = super(MedicineHistoryAdmin, self).get_actions(request)
        return remove_delete_actions(actions)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        return super().change_view(request, object_id, form_url, extra_context=dict(show_delete=False))


@admin.register(PatientHistory)
class PatientHistoryAdmin(admin.ModelAdmin):
    """Patient History Model for Django Admin"""

    fields = [
        'name',
        'social_name',
        'cpf',
        'rg',
        'birth_date',
        'marital_status',
        'place_of_birth',
        'gender',
        'phone',
        'observation',
        'created_at',
        'created_by',
        'updated_at',
        'updated_by',
    ] + BASE_FIELDS

    list_display = (
        'name',
        'cpf',
        'birth_date',
        'phone',
    )

    list_filter = [
        'gender',
        'marital_status',
        ('birth_date', DateRangeFilter),
    ]

    search_fields = ('name', 'cpf', 'phone',)

    def save_model(self, request, obj, form, change):
        obj = set_created_by(request, obj)
        if change:
            obj = set_updated_by(request, obj)
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_actions(self, request):
        actions = super(PatientHistoryAdmin, self).get_actions(request)
        return remove_delete_actions(actions)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        return super().change_view(request, object_id, form_url, extra_context=dict(show_delete=False))


@admin.register(NursingProfessionalHistory)
class NursingProfessionalHistoryAdmin(admin.ModelAdmin):
    """Nursing Professional History Model for Django Admin"""

    fields = [
        'name',
        'coren',
        'created_at',
        'created_by',
        'updated_at',
        'updated_by',
    ] + BASE_FIELDS

    list_display = (
        'name',
        'coren',
    )

    list_filter = []

    search_fields = ('name', 'coren',)

    def save_model(self, request, obj, form, change):
        obj = set_created_by(request, obj)
        if change:
            obj = set_updated_by(request, obj)
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_actions(self, request):
        actions = super(NursingProfessionalHistoryAdmin,
                        self).get_actions(request)
        return remove_delete_actions(actions)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        return super().change_view(request, object_id, form_url, extra_context=dict(show_delete=False))


@admin.register(MedicalEvaluationHistory)
class MedicalEvaluationHistoryAdmin(admin.ModelAdmin):
    """Medical Evaluation History Model for Django Admin"""

    fields = [
        'nursing_professional',
        'patient',
        'medicine',
        'schedule',
        'observation',
    ] + BASE_FIELDS

    list_display = (
        'get_patient_name',
        'get_nursing_professional_name',
        'schedule',
        'observation',
    )

    list_filter = [
        (
            'nursing_professional__name',
            custom_titled_filter('Profissional de Enfermagem')
        ),
        ('schedule', DateRangeFilter)
    ]

    search_fields = (
        'nursing_professional__name',
        'patient__name',
        'medicine__name',
        'observation',
    )

    @admin.display(description='Paciente', ordering='patient__name')
    def get_patient_name(self, obj):
        """Get Patient name for list_display"""
        return obj.patient.name

    @admin.display(description='Profissional de Enfermagem',
                   ordering='nursing_professional__name')
    def get_nursing_professional_name(self, obj):
        """Get Nursing Professional name for list_display"""
        return obj.nursing_professional.name

    def save_model(self, request, obj, form, change):
        obj = set_created_by(request, obj)
        if change:
            obj = set_updated_by(request, obj)
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_actions(self, request):
        actions = super(MedicalEvaluationHistoryAdmin,
                        self).get_actions(request)
        return remove_delete_actions(actions)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        return super().change_view(request, object_id, form_url, extra_context=dict(show_delete=False))


@admin.register(MedicationHistory)
class MedicationHistoryAdmin(admin.ModelAdmin):
    """Medication History Model for Django Admin"""

    fields = [
        'schedule',
        'observation',
        'nursing_professional',
        'patient',
        'medicine',
    ] + BASE_FIELDS

    list_display = (
        'schedule',
        'observation',
        'get_patient_name',
        'get_nursing_professional_name',
        'get_medicine_name',
    )

    list_filter = [
        (
            'nursing_professional__name',
            custom_titled_filter('Profissional de Enfermagem')
        ),
        ('schedule', DateRangeFilter)
    ]

    search_fields = (
        'nursing_professional__name',
        'patient__name',
        'medicine__name',
        'observation',
    )

    @admin.display(description='Paciente', ordering='patient__name')
    def get_patient_name(self, obj):
        """Get Patient name for list_display"""
        return obj.patient.name

    @admin.display(description='Profissional de Enfermagem',
                   ordering='nursing_professional__name')
    def get_nursing_professional_name(self, obj):
        """Get Nursing Professional name for list_display"""
        return obj.nursing_professional.name

    @admin.display(description='Medicamento', ordering='medicine__name')
    def get_medicine_name(self, obj):
        """Get Medicine name for list_display"""
        return obj.medicine.name

    def save_model(self, request, obj, form, change):
        obj = set_created_by(request, obj)
        if change:
            obj = set_updated_by(request, obj)
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_actions(self, request):
        actions = super(MedicationHistoryAdmin,
                        self).get_actions(request)
        return remove_delete_actions(actions)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        return super().change_view(request, object_id, form_url, extra_context=dict(show_delete=False))
