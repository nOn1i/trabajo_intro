from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')  # Redirige a una página de registro exitoso
    else:
        form = RegistroForm()

    return render(request, 'registro/registro.html', {'form': form})
