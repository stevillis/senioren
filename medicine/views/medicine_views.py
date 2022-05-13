from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from medicine.models import Medicine
from medicine.services import medicine_service


def list_medicines(request: HttpRequest) -> HttpResponse:
    medicines = medicine_service.list_medicines(request)
    context = {
        'model': Medicine,
        'medicines': medicines
    }
    return render(request, "list_medicines.html", context)


"""
@login_required(login_url='/login')
def cadastrar_campus(request: HttpRequest) -> HttpResponse:
    can_insert = has_permission(request.user, INSERIR_CADASTRO_CAMPUS)
    if request.method == "POST" and can_insert:
        form = CampusForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            campus_novo = campus.Campus(
                nome=nome,
                created=None,
                updated=None,
                createdby=request.user,
                updatedby=None,
                isactive=ESTA_ATIVO,
                inativado_em=None,
            )
            campus_service.cadastrar_campus(campus_novo)
            return redirect("registro:listar_campi")
    else:
        form = CampusForm()
    context = {
        'form': form,
        'isEdit': False,
        'erro': None if can_insert else 'Usuário sem permissão para Inserir Campus',
    }
    return render(request, "campi/form_campus.html", context)


@login_required(login_url='/login')
def get_campus_by_id(request: HttpRequest, pk: str) -> HttpResponse:
    can_view = has_permission(request.user, VISUALIZAR_CADASTRO_CAMPUS)
    campus_encontrado = campus_service.get_campus_by_id(pk)
    context = {
        'campus': campus_encontrado,
        'erro': None if can_view else 'Usuário sem permissão para Visualizar Campus',
    }
    return render(request, "campi/visualizar_campus.html", context)


@login_required(login_url='/login')
def editar_campus(request: HttpRequest, pk: str) -> HttpResponse:
    can_change = has_permission(request.user, EDITAR_CADASTRO_CAMPUS)
    campus_antigo = campus_service.get_campus_by_id(pk)
    form = CampusForm(request.POST or None, instance=campus_antigo)
    if request.method == "POST" and can_change:
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            campus_novo = campus.Campus(
                nome=nome,
                created=campus_antigo.created,
                updated=None,
                createdby=campus_antigo.createdby,
                updatedby=request.user,
                isactive=campus_antigo.isactive,
                inativado_em=campus_antigo.inativado_em,
            )
            campus_service.editar_campus(campus_antigo, campus_novo)
            return redirect("registro:listar_campi")
    context = {
        'form': form,
        'isEdit': True,
        'erro': None if can_change else 'Usuário sem permissão para Editar Campus',
    }
    return render(request, "campi/form_campus.html", context)


@login_required(login_url='/login')
def inativar_campus(request: HttpRequest, pk: str) -> HttpResponse:
    can_deactivate = has_permission(request.user, INATIVAR_CADASTRO_CAMPUS)
    campus_encontrado = campus_service.get_campus_by_id(pk)
    if request.method == "POST" and can_deactivate:
        campus_encontrado.updatedby = request.user
        campus_service.inativar_campus(campus_encontrado)
        return redirect("registro:listar_campi")
    context = {
        'campus': campus_encontrado,
        'erro': None if can_deactivate else 'Usuário sem permissão para Inativar Campus',
    }
    return render(request, "campi/inativar_campus.html", context)

"""


def medicine_detail(request):
    # TODO
    pass


def create_medicine(request):
    # TODO
    pass


def update_medicine(request):
    # TODO
    pass


def deactivate_medicine(request):
    # TODO
    pass
