from django.contrib import admin

from .models import *

class DetVenta(admin.TabularInline):
	model = DetalleVenta	
	extra = 1
	readonly_fields = ['sub_total']
	raw_id_fields = ['producto']
	autocomplete_fields=['producto']

class VentaAdmin(admin.ModelAdmin):
	inlines = [DetVenta]
	list_display=['id','cliente', 'total','fecha', 'generar_comprovante']
	readonly_fields = ['total']
	list_per_page = 12


class DetVentaEscuela(admin.TabularInline):
	model = DetalleVentaEscuela	
	extra = 1
	readonly_fields = ['sub_total']
	raw_id_fields = ['producto']
	autocomplete_fields=['producto']

class VentaEscuelaAdmin(admin.ModelAdmin):
	inlines = [DetVentaEscuela]
	list_display=['id','escuela', 'total','fecha', 'generar_comprovante']
	readonly_fields = ['total']
	list_per_page = 12



admin.site.register(Venta, VentaAdmin)
admin.site.register(VentaEscuela, VentaEscuelaAdmin)
