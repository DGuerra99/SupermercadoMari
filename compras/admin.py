from django.contrib import admin

from .models import *

class DetCompra(admin.TabularInline):
	model = DetalleCompra	
	extra = 1
	raw_id_fields = ['producto']
	autocomplete_fields=['producto']
	readonly_fields = ['subtotal']

class CompraAdmin(admin.ModelAdmin):
	inlines = [DetCompra]
	list_display=['id','proveedor', 'total','fecha']
	readonly_fields = ['total']
	list_per_page = 12




admin.site.register(Compra, CompraAdmin)
