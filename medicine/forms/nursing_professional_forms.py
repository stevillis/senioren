from django import forms

from ..models import NursingProfessional


class NursingProfessionalForm(forms.ModelForm):
    """NursingProfessional form."""

    class Meta:
        model = NursingProfessional
        fields = [
            'name',
            'coren',
        ]
