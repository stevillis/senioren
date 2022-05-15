from django import forms

from ..models import Medicine


class MedicineForm(forms.ModelForm):
    """Medicine form."""
    expiration_date = forms.DateField(
        label=Medicine._meta.get_field('expiration_date').verbose_name,
        localize=True,
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Medicine
        fields = [
            'name',
            'description',
            'batch',
            'expiration_date',
            'stock_qty',
        ]
