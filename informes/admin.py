from django.contrib import admin

from .models import *

class InformeAdmin(admin.ModelAdmin):
	list_display=['fecha_inicio', 'fecha_limite','generar_informe']
	fields=['fecha_inicio','fecha_limite','tipo_dev']

class InventarioAdmin(admin.ModelAdmin):
	list_display=['generar_inventario']


admin.site.register(InformePorRango, InformeAdmin)
admin.site.register(Inventario, InventarioAdmin)
