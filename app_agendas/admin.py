from django.contrib import admin
from .models import Agenda_Publica,Agenda_Institucional

	
@admin.register(Agenda_Publica)
class Agenda_PublicaAdmin(admin.ModelAdmin):
    	pass
@admin.register(Agenda_Institucional)
class Agenda_Institucional(admin.ModelAdmin):
    	pass
