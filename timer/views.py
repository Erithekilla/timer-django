from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Tempozika
from .forms import tempoPomo

def index(request):
    tempo = Tempozika.objects.all()
    form = tempoPomo()

    tempo_salvo_atv = Tempozika.objects.last()
    tempo_padrao_atv = 25

    if tempo_salvo_atv:
        tempo_padrao_atv = tempo_salvo_atv.tempoAtivo

    tempo_salvo_desc = Tempozika.objects.last()
    tempo_padrao_desc = 5

    if tempo_salvo_desc:
        tempo_padrao_desc = tempo_salvo_desc.tempoDesc

    context = {'tempo':tempo,'form':form,'tempo_timer':tempo_padrao_atv, 'tempo_desc': tempo_padrao_desc}
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