from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Tempozika
from .forms import tempoPomo

def index(request):
    tempo = Tempozika.objects.all()
    form = tempoPomo()

    tempo_salvo = Tempozika.objects.last()
    tempo_padrao = 25

    if tempo_salvo:
        tempo_padrao = tempo_salvo.tempoAtivo

    context = {'tempo':tempo,'form':form,'tempo_timer':tempo_padrao}
    return render(request, "timer/index.html", context)


def definir_tempo(request):
    if request.method=="POST":
        form = tempoPomo(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = tempoPomo()
    
    return render(request, "index.html", {"form": form})