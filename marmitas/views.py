from django.shortcuts import render, redirect, get_object_or_404
from .models import Marmita
from .forms.form_marmita import MarmitaForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def marmitas_view(request):
    marmitas = Marmita.objects.all()

    return render(request, 'marmitas/pages/marmitas.html', {
        'marmitas': marmitas
    })

def staff_only(user):
    return user.is_authenticated and user.is_staff
@user_passes_test(staff_only, login_url='/sem-permissao/')
def marmitas_create_view(request):
    if request.method == 'POST':
        form = MarmitaForm(request.POST)
        if form.is_valid():
            marmita = form.save(commit=False)
            marmita.user = request.user
            marmita.save()
            return redirect('marmitas:home')
    else:
        form = MarmitaForm()
    
    return render(request, 'marmitas/pages/marmitas_create.html', {
        'form': form
    })

@user_passes_test(staff_only, login_url='/sem-permissao/')
def marmitas_edit_view(request, id):
    marmita = get_object_or_404(Marmita, pk=id)

    if request.method == 'POST':
        form = MarmitaForm(
            request.POST,
            instance=marmita
        )

        if form.is_valid():
            form.save()
            return redirect('marmitas:home')

    else:
        form = MarmitaForm(instance=marmita)

    return render(request, 'marmitas/pages/marmitas_create.html', {
        'form': form,
    })

@user_passes_test(staff_only, login_url='/sem-permissao/')
def marmitas_delete_view(request, id):
    marmita = get_object_or_404(Marmita, pk=id)

    if request.method == 'POST':
        marmita.delete()
        return redirect('marmitas:home')

    return render(request, 'marmitas/pages/marmitas_delete.html', {
        'marmita': marmita
    })

def marmita_detail_view(request, id):
    marmita = get_object_or_404(Marmita, pk=id)

    return render(request, 'marmitas/pages/detail.html', {
        'marmita': marmita
    })