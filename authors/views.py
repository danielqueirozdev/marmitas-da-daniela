from .forms.login_form import LoginForm
from .forms.register_form import RegisterForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from marmitas.models import Marmita

# Create your views here.
def register_view(request):
    form_data = request.session.pop('form_data', None)
    form_errors = request.session.pop('form_errors', None)
    register_form_data = request.session.get('register_form_data', None)

    form = RegisterForm(register_form_data)

    if form_errors:
        form._errors = form_errors

    return render(request, 'authors/pages/register.html', context={
        'form': form,
    })

def register_create_view(request):
    if request.method != 'POST':
        raise Http404()

    form = RegisterForm(request.POST)

    if form.is_valid():
        data_user = form.save(commit=False)

        data_user.set_password(data_user.password)

        data_user.save()
        messages.success(request, 'Conta criada com sucesso. Faça o login.')

        del(form)
        return redirect(reverse('authors:login'))

    request.session['register_form_data'] = request.POST
    request.session['form_errors'] = form.errors

    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html', {
        'form': form,
        'form_action': reverse('authors:login_create')
    })

def login_create_view(request):
    if request.method != 'POST':
        raise Http404()
    
    form = LoginForm(request.POST)
    login_url = reverse('authors:login')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Login realizado com sucesso.')
            login(request, authenticated_user)
            return redirect('marmitas:home')
        
        messages.error(request, 'Usuário ou senha inválidos.')

        return redirect(login_url)
    
    messages.error(request, 'Usuário ou senha inválidos.')

    return redirect(login_url)

@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    if request.method != 'POST':
        return redirect('authors:login')

    logout(request)
    return redirect('authors:login')