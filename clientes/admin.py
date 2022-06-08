from django.contrib import admin
from .models import Clientes #IMPORTAMOS NUESTROS MODELOS AL PANEL DE ADMINISTRACIÓN

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('nombre','empresa',)
    ordering = ('-created_at',)
    search_fields = ('nombre', 'empresa') #VAMOS A PODER BUSCAR CON BASE EN EL TÍTULO Y CONTENIDO DE CADA PAGINA


admin.site.register(Clientes) #REGISTRAMOS EL MODELO Clientes


#CONFIGURAR TÍTULO DEL PANEL DE ADMINISTRACIÓN DE DJANGO   
admin.site.site_header = 'Panel de Admin de la API CRM'

#CAMBIAR NOMBRE DE LA PESTAÑA DEL PANEL DE ADMINISTRACIÓN DE DJANGO
admin.site.index_title = 'Panel de Admin de la API CRM'
