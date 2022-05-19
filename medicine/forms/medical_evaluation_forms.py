from dal import autocomplete
from django import forms
from tempus_dominus.widgets import DateTimePicker

from ..models import MedicalEvaluation
from ..services.nursing_professional_service import \
    get_all_nursing_professionals
from ..services.patient_service import get_all_patients


class MedicalEvaluationForm(forms.ModelForm):
    """MedicalEvaluation form."""

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
        model = MedicalEvaluation
        fields = [
            'schedule',
            'heart_pressure',
            'glucose',
            'observation',
            'patient',
            'nursing_professional',
        ]
