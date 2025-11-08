from django import forms
from .models import Tempozika

class tempoPomo(forms.ModelForm):
    class Meta:
        model = Tempozika
        fields = ['tempoAtivo']