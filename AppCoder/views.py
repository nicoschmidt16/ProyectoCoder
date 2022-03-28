#from django.shortcuts import render
#nose si va esto de arriba, porlas no lo borro

from django.http import HttpResponse

from AppCoder.models import Curso

def curso(self):
    curso = Curso(nombre = "Desarrollo web", camada = "19881")
    curso.save()
    documentoDeTexto = f"--->Curso:{curso.nombre}, Camada:{curso.camada}"
    return HttpResponse(documentoDeTexto)

# Create your views here.
