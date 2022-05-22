from dal import autocomplete
from django import forms
from tempus_dominus.widgets import DateTimePicker

from ..models import Medication
from ..services.medicine_service import get_all_medicines
from ..services.nursing_professional_service import \
    get_all_nursing_professionals
from ..services.patient_service import get_all_patients


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, medicine):
        return f'{medicine.name}'


class MedicationForm(forms.ModelForm):
    """Medication form."""

    schedule = forms.DateTimeField(
        input_formats=['%d-%m-%Y %H:%M:%S'],
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        )
    )

    medicines = CustomMMCF(
        queryset=get_all_medicines(),
        widget=forms.CheckboxSelectMultiple
    )

    patient = forms.ModelChoiceField(
        queryset=get_all_patients(),
        widget=autocomplete.ModelSelect2(url='medicine:patient-autocomplete')
    )

    nursing_professional = forms.ModelChoiceField(
        queryset=get_all_nursing_professionals(),
        widget=autocomplete.ModelSelect2(
            url='medicine:nursing-professional-autocomplete')
    )

    class Meta:
        model = Medication
        fields = [
            'schedule',
            'observation',
            'medicines',
            'patient',
            'nursing_professional',
        ]
