from django.shortcuts import render
from django.http import HttpResponse

participantes = [
    {
        'nombre': 'Juan',
        'apellido': 'Lopez',
        'correo': 'juan@gmail.com',
        'twitter': 'juan.lopez'
    },
    {
        'nombre': 'Maria',
        'apellido': 'Gomez',
        'correo': 'maria@gmail.com',
        'twitter': 'maria.gomez'
    },
    {
        'nombre': 'Karla',
        'apellido': 'Herrea',
        'correo': 'karla.herrea@gmail.com',
        'twitter': 'karla.herrera'
    },
    {
        'nombre': 'Josue',
        'apellido': 'Alvarez',
        'correo': 'josue@gmail.com',
        'twitter': 'josuetec2003'
    },
]

def index(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        twitter = request.POST.get('twitter')

        participantes.append({
            'nombre': nombre,
            'apellido': apellido,
            'correo': correo,
            'twitter': twitter
        })

        ctx = {
            'participantes': participantes
        }

        # return HttpResponse('El participante ha sido registrado')
        return render(request, 'registro/index.html', ctx)
    else:
        # contexto que va para la plantilla
        ctx = {
            'participantes': participantes
        }

        return render(request, 'registro/index.html', ctx)




