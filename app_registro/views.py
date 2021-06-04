from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
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

        messages.add_message(request, messages.INFO, f'El participante {nombre} {apellido} ha sido registrado con éxito')

        # return JsonResponse({
        #     'nombre': nombre,
        #     'apellido': apellido,
        #     'correo': correo,
        #     'twitter': twitter,
        #     'OK': True,
        #     'msj': 'El participante ha sido registrado con éxito'
        # })

        # ctx = {
        #     'participantes': Participante.objects.all().order_by('nombre')
        # }

        # return HttpResponse('El participante ha sido registrado')
        # return render(request, 'registro/participantes.html', ctx)
    
    # Metodo GET, PUT, PATCH, DELETE

    # La primera consulta: select * from participantes order by nombre desc
    # Realizar un Queryset con el ORM de Django
    q = request.GET.get('q')

    if q:
        data = Participante.objects.filter(nombre__startswith=q).order_by('nombre')

        '''
            select * 
            from participantes
            where nombre like 'n%'
        '''
    else:
        data = Participante.objects.all().order_by('nombre')

    ctx = {
        'participantes': data,
        'q': q
    }

    return render(request, 'registro/participantes.html', ctx)




