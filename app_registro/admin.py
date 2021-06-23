from django.contrib import admin
from .models import Conferencia, Conferencista, Participante, Asistencia

# ------------------------------------------------------------------------
class ConferenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha', 'hora', 'estado',)
    list_editable = ('nombre', 'fecha', 'estado',)

admin.site.register(Conferencia, ConferenciaAdmin)
# ------------------------------------------------------------------------
admin.site.register(Conferencista)
# ------------------------------------------------------------------------
admin.site.register(Asistencia)
# ------------------------------------------------------------------------
admin.site.register(Participante)
# ------------------------------------------------------------------------

