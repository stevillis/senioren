"""Util module for common services functions."""

from typing import Tuple, Type

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model
from django.http import Http404


def get_object_by_id_or_404(obj: Type[Model], pk: str) -> Tuple[Model, Http404]:
    """
    Get Model object by id.

    Returns: an instance of obj if exists, Http404 otherwise.
    """
    try:
        return obj.objects.get(id=pk)
    except ObjectDoesNotExist as object_does_not_exist:
        raise Http404(f'{obj.__name__} not found') from object_does_not_exist
