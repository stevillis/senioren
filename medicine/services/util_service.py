from typing import Tuple, Type

from django.core.exceptions import ObjectDoesNotExist
from django.core.signing import BadSignature
from django.db.models import Model
from django.http import Http404
from django.utils.translation import gettext_lazy as _


def get_object_by_id_or_404(
        obj: Type[Model],
        pk: str
) -> Tuple[Model, Http404]:
    not_found_message = _('not found')
    error_msg = Http404(f'{obj.__name__} {not_found_message}')
    try:
        return obj.objects.get(id=pk)
    except ObjectDoesNotExist:
        raise error_msg
    except BadSignature:
        raise error_msg
