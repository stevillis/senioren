from daterangefilter.filters import DateRangeFilter
from django.contrib import admin

from medicine.models import Medicine, MedicalEvaluation

BASE_FIELDS = ['is_active', ]
READ_ONLY_BASE_FIELDS = ['created_at', 'updated_at', ]


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
    fields = ['schedule', 'heart_pressure', 'glucose', 'observation', ] + BASE_FIELDS
    list_display = ('schedule', 'heart_pressure', 'glucose', 'observation',)
    list_filter = [
        ('schedule', DateRangeFilter)
    ]
    # search_fields = [] # TODO: define searchable fields
