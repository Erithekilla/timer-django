from django.db import models


# Create your models here.
class Tempozika(models.Model):
    tempoAtivo = models.IntegerField(default=0)

    def __str__(self):
        return f"Tempo: {self.tempoAtivo}"





