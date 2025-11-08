from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Tempozika
from .forms import tempoPomo

def index(request):
    tempo = Tempozika.objects.all()
    form = tempoPomo()
    context = {'tempo':tempo,'form':form}
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