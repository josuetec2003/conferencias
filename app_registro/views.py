from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Participante, Conferencia, Asistencia
from datetime import datetime
from time import sleep
from telegram import Bot # pip install python-telegram-bot

TOKEN = '1689491589:AAFQs3K6z_CGP7Lw0i2SRZfU-CQXlRHTzWs'
GROUP_ID = -549716729

bot = Bot(token=TOKEN)

@login_required()
def index(request):
    return render(request, 'registro/index.html')


@login_required()
def participantes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        twitter = request.POST.get('twitter')

        p = Participante(nombre=nombre, apellido=apellido, correo=correo, twitter=twitter)
        p.save()

        msj = f'El participante {nombre} {apellido} ha sido registrado con éxito.'

        # Codigo para enviar un mensaje a un grupo de telegram

        try:
            bot.send_message(chat_id=GROUP_ID, text=msj)
        except Exception as e:
            msj += f'<br/><strong>{e}</strong>'
        
        messages.add_message(request, messages.INFO, msj)

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
    activo = 'participantes'
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
        'activo': activo,
        'participantes': data,
        'q': q
    }

    return render(request, 'registro/participantes.html', ctx)


@login_required()
def eliminar_participante(request, id):
    Participante.objects.get(pk=id).delete()
    return redirect(reverse('participantes'))


@login_required()
def editar_participante(request, id):
    par = get_object_or_404(Participante, pk=id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        twitter = request.POST.get('twitter')

        par.nombre = nombre
        par.apellido = apellido
        par.correo = correo
        par.twitter = twitter
        par.save()

    #par = Participante.objects.get(pk=id)    
    data = Participante.objects.all().order_by('nombre')

    ctx = {
        'activo': 'participantes',
        'participantes': data,
        'p': par
    }

    return render(request, 'registro/participantes.html', ctx)


@login_required()
def conferencias(request):
    hoy = datetime.now().date()

    confs = Conferencia.objects.filter(fecha__gt=hoy).order_by('fecha')

    return render(request, 'registro/conferencias.html', {'confs': confs})

@login_required()
def asistir(request, id, accion): 
    if accion == 'asistir':
        # Obteniendo el objeto Conferencia utilizando el id de la URL
        conf = get_object_or_404(Conferencia, pk=id)

        # Verificar si el participante ya forma parte de la asistencia
        obj, created = Asistencia.objects.get_or_create(conferencia=conf, participante=request.user.participante)

        if created:
            msj = f'Ya formas parte de la conferencia {conf.nombre}'
        else:
            msj = f'Tu asistencia ya habia sido reservada'
        
        messages.add_message(request, messages.ERROR, msj)

        return redirect(reverse('registro:conferencias'))

    elif accion == 'salirme':
        conf = get_object_or_404(Conferencia, pk=id)
        Asistencia.objects.filter(conferencia=conf, participante=request.user.participante).delete()

        messages.add_message(request, messages.ERROR, 'Te has salido de la conferencia')
        return redirect(reverse('registro:conferencias'))
        

    else:
        raise Http404("No encontramos lo que buscas")


def ajax_view(request):
    if request.is_ajax():
        ctx = {'respuesta': 'Esto es AJAX'}

        sleep(20)

        return JsonResponse(ctx)
    else:
        return HttpResponse('No tienes permiso para visualizar el contenido de esta pagina')