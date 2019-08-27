from django.shortcuts import render
from django.views.generic import (
	TemplateView,
	ListView,
	CreateView,	
)
from .models import Autor, Libros

class ListaAutores(ListView):
	template_name = "biblioteca/lista-autores.html"
	model = Autor
	context_object_name = 'autores'

class ListaLibrosAutores(ListView):
	""" Vista para listar libros autor"""
	template_name = "biblioteca/lista-libros.html"
	context_object_name = 'libros'

	def get_queryset(self):
		#Identificar el autor
		id = self.kwargs['pk']
		#Filtro de los libros
		lista = Libros.objects.filter(
			autor = id
		)
		#Devuelve el resultado o la lista resultado
		return lista

class AddAutor(CreateView):
	"""Vista para registrar un autor"""
	template_name = 'biblioteca/autor-add.html'
	model = Autor
	fields = ['nombre', 'nacionalidad']
	success_url = '/'