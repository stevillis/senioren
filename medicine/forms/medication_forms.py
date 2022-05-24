from dal import autocomplete
from django import forms
from django.utils.translation import gettext_lazy as _
from tempus_dominus.widgets import DateTimePicker

from ..models import Medication
from ..services.medicine_service import get_medicines_with_stock
from ..services.nursing_professional_service import \
    get_all_nursing_professionals
from ..services.patient_service import get_all_patients


class CustomMMCF(forms.ModelMultipleChoiceField):
    """
    Defines custom label for Many to Many fields.
    """

    def label_from_instance(self, medicine):
        """Returns custom label for a given medicine."""
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
        queryset=get_medicines_with_stock(),
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

    def clean_medicines(self):
        """Check if all selected medicines have stock_qty greater than 0."""
        medicines = self.cleaned_data.get('medicines')

        if medicines:
            for medicine in medicines:
                if not medicine.stock_qty > 0:
                    msg = _('Stock for medicine is empty')
                    error_msg = f'{msg} - id: {medicine.id}'

                    self.add_error('medicines', error_msg)
        return medicines

    class Meta:
        """Meta data definitions."""
        model = Medication
        fields = [
            'schedule',
            'observation',
            'medicines',
            'patient',
            'nursing_professional',
        ]
