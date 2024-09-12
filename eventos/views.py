from django.shortcuts import render
from .models import Evento
from .forms import EventoForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Organizador
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .forms import OrganizadorForm

def lista_eventos(request):
    eventos = Evento.objects.select_related('organizador').all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})



def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')  
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)  
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')  
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/editar_evento.html', {'form': form})

def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')  
    return render(request, 'eventos/eliminar_evento.html', {'evento': evento})





class OrganizadorListView(ListView):
    model = Organizador
    template_name = 'eventos/lista_organizadores.html'
    context_object_name = 'organizadores'  


class OrganizadorCreateView(CreateView):
    model = Organizador
    template_name = 'eventos/crear_organizador.html'
    fields = ['nombre', 'email']
    success_url = reverse_lazy('lista_organizadores')  

def editar_organizador(request, pk):
    organizador = get_object_or_404(Organizador, pk=pk)
    if request.method == 'POST':
        form = OrganizadorForm(request.POST, instance=organizador)
        if form.is_valid():
            form.save()
            return redirect('lista_organizadores')  
    else:
        form = OrganizadorForm(instance=organizador)
    return render(request, 'eventos/editar_organizador.html', {'form': form})

def eliminar_organizador(request, pk):
    organizador = get_object_or_404(Organizador, pk=pk)
    if request.method == 'POST':
        organizador.delete()
        return redirect('lista_organizadores')  
    return render(request, 'eventos/eliminar_organizador.html', {'organizador': organizador})





@login_required  
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_eventos'))
    else:
        form = EventoForm(instance=evento)
    
    return render(request, 'eventos/editar_evento.html', {'form': form, 'evento': evento})



@login_required
def dashboard(request):
    return render(request, 'eventos/dashboard.html')


