from django.contrib import admin

from .models import *

class ProductoAdmin(admin.ModelAdmin):
	search_fields = [ 'nombre', 'codigo_manual', 'codigo_barra']
	readonly_fields = ['existencia']
	list_per_page = 12
	list_display=[ 'nombre', 'marca','codigo_manual', 'codigo_barra']
	

admin.site.register(Proveedor)
admin.site.register(Escuela)
admin.site.register(Producto, ProductoAdmin)