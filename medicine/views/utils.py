import re

from django.core.handlers.wsgi import WSGIRequest
from django.http import QueryDict


def clean_mask_cpf(cpf: str) -> str:
    return re.sub(r'\D', '', cpf)


def mask_cpf(cpf: str) -> str:
    if len(cpf) == 11:
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    return cpf


def clean_masked_inputs_form(request: WSGIRequest) -> QueryDict:
    if request.method == 'POST':
        data = request.POST.copy()
    else:
        data = request.GET.copy()

    if 'cpf' in data:
        data['cpf'] = clean_mask_cpf(data.get('cpf'))

    return data
