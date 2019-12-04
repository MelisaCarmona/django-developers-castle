from django.shortcuts import render, get_object_or_404
#se agregan las librerias necesarias para trabajar con vistas basadas en clases (CVB)
from django.views.generic.base import TemplateView
#Agregamos la libreria para importar listviews
from django.views.generic.list import listviews
#se importa los modelos hechos
from .models import Usuarios, Experiencia, Logros, Habilidades, Educacion 
# Create your views here.
