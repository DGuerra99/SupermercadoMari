from django.contrib import admin

from .models import *

class DetDevolucion(admin.TabularInline):
	model = DetalleDev	
	extra = 1

class DevolucionAdmin(admin.ModelAdmin):
	inlines = [DetDevolucion]
	list_display=['id','tipo_dev', 'total','fecha']

admin.site.register(Devolucion, DevolucionAdmin)
