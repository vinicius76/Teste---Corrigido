from django.shortcuts import render
from django.views.generic import ListView
from .models import Agenda_Publica,Agenda_Institucional
	
class HomePageView(ListView):
	model = Agenda_Publica
	template_name = "app_agendas/1.html"

class SecondPageView(ListView):
    model = Agenda_Institucional
    template_name = "app_agendas/2.html"
