from django.forms import TextInput
from django_filters import CharFilter, FilterSet

from .models import Medicine


class MedicineFilter(FilterSet):
    name = CharFilter(
        lookup_expr='icontains',
        widget=TextInput(
            attrs={
                'placeholder': Medicine._meta.get_field('name').verbose_name,
            }
        ),
        max_length=Medicine._meta.get_field('name').max_length
    )
    description = CharFilter(
        lookup_expr='icontains',
        widget=TextInput(
            attrs={
                'placeholder': Medicine._meta.get_field('description').verbose_name,
            }
        ),
        max_length=Medicine._meta.get_field('description').max_length
    )
    batch = CharFilter(
        lookup_expr='icontains',
        widget=TextInput(
            attrs={
                'placeholder': Medicine._meta.get_field('batch').verbose_name,
            }
        ),
        max_length=Medicine._meta.get_field('batch').max_length
    )

    class Meta:
        model = Medicine
        fields = ['name', 'description', 'batch', ]
