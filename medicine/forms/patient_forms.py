from django import forms

from ..models import Patient


class PatientForm(forms.ModelForm):
    """Patient form."""
    cpf = forms.CharField(
        label='CPF',
        widget=forms.TextInput(
            attrs={
                'data-mask': '000.000.000-00'
            }
        ),
        max_length=Patient._meta.get_field('cpf').max_length
    )

    birth_date = forms.DateField(
        label=Patient._meta.get_field('birth_date').verbose_name,
        localize=True,
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'type': 'date'
            }
        )
    )

    phone = forms.CharField(
        label=Patient._meta.get_field('phone').verbose_name,
        widget=forms.TextInput(
            attrs={
                'data-mask': '(00) 00000-0000'
            }
        ),
        max_length=Patient._meta.get_field('phone').max_length
    )

    class Meta:
        model = Patient
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
        ]
