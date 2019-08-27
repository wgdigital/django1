from django.shortcuts import render

from django.views.generic import (
	TemplateView,
	ListView,
)

class IndexView(TemplateView):
	#Una vista procesa los datos y renderiza el resultado en pantalla
	#Siempre nos pedira un template con el que trabajar
	#Un template es un archivo HTML
	
	template_name = "home/index.html"
	

class ListaLibros(ListView):
	template_name = "home/lista.html"
	queryset = ['El quijote de la mancha','codigo Limpio','La sombra del Viento','Djando 2.0']
	context_object_name = 'libros'