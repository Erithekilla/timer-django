from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tempo-pomo/', views.definir_tempo, name="tempo-pomo")
]
