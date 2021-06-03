from django.contrib import admin
from .models import Conferencia, Conferencista, Participante

# ------------------------------------------------------------------------
class ConferenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha', 'hora', 'conferencista')
    list_editable = ('nombre', 'conferencista')

admin.site.register(Conferencia, ConferenciaAdmin)
# ------------------------------------------------------------------------
admin.site.register(Conferencista)
# ------------------------------------------------------------------------
admin.site.register(Participante)
