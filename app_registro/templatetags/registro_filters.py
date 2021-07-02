from django import template
from app_registro.models import Asistencia

register = template.Library()

# filtros: filter()
# tags: simple_tag

@register.filter
def mayusculas(texto):
    return f'<strong>{texto.upper()}</strong>'


@register.simple_tag
def validar_asistencia(conf, part):
    return Asistencia.objects.filter(conferencia=conf, participante=part).exists()
