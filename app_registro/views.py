from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Participante

def index(request):
    return render(request, 'registro/index.html')


def participantes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        twitter = request.POST.get('twitter')

        p = Participante(nombre=nombre, apellido=apellido, correo=correo, twitter=twitter)
        p.save()

        ctx = {
            'participantes': Participante.objects.all().order_by('nombre')
        }

        # return HttpResponse('El participante ha sido registrado')
        return render(request, 'registro/participantes.html', ctx)
    
    # Metodo GET, PUT, PATCH, DELETE

    # La primera consulta: select * from participantes order by nombre desc
    # Realizar un Queryset con el ORM de Django
    data = Participante.objects.all().order_by('nombre')

    ctx = {
        'participantes': data
    }

    return render(request, 'registro/participantes.html', ctx)




