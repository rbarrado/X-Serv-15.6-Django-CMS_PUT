from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request, peticion):

    if request.method == "POST":
        p = Pages(name=request.POST['nombre'])
        p.save()
    try:
        solicitud = Pages.objects.get(name=peticion)
        respuesta = 'Hola, soy ' + solicitud.name + ": " + str(solicitud.page)
        #en vez del id lo podemos hacer tambien con el nombre pero esta mejor asi
    except Pages.DoesNotExist:
        respuesta = "No existe esa página. Creala"
        respuesta += '<form action="" method="POST">'
        respuesta += 'Nombre: <input type="text" name="nombre">'
        respuesta += '<input type="submit" value="Enviar">'

    return HttpResponse(respuesta)

def give_page(request):
    lista_paginas = Pages.objects.all()
    respuesta = "<ol>" #Esto me crea una lista en la pagina
    for pag in lista_paginas:
        respuesta += '<li><a href="' + str(pag.id) + '">' + pag.name + '</a>'
    respuesta += "</ol>"
    return HttpResponse(respuesta)
