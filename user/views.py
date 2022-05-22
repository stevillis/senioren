from django.contrib.auth import authenticate
from django.contrib.auth import login as log_in
from django.contrib.auth import logout as log_out
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from user.forms import LoginForm


def login(request: WSGIRequest) -> HttpResponse:
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            session_minutes = 120
            request.session.set_expiry(session_minutes * 60)
            log_in(request, user)

            return redirect(reverse('index'))
    else:
        if request.user.is_authenticated:
            return redirect(reverse('index'))

    context = {
        'form': form
    }

    return render(
        request=request,
        template_name='login.html',
        context=context
    )


def logout(request: WSGIRequest) -> HttpResponse:
    log_out(request)

    return redirect(reverse('index'))
