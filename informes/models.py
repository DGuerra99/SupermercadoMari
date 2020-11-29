from django.db import models

from compras.models import *
from ventas.models import *
from django.utils.safestring import mark_safe


TIPO_INFORME  =(
	('General', 'General'),
    ('Compra', 'Compra'),
    ('Venta', 'Venta'),
)#Choice para seleccionar tipo de de informe


#Informe -----------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
class InformePorRango(models.Model):
	tipo_dev=models.CharField(
		'Tipo de Informe',
		max_length=7,
		choices=TIPO_INFORME, default= 'General')
	fecha_inicio = models.DateField('Fecha De Inicio')
	fecha_limite = models.DateField('Fecha De Limite')
	total_compras = models.DecimalField('Total de Compras',max_digits=7,
		decimal_places=2,  null=False, default=0.00)
	total_ventas = models.DecimalField('Total Ventas',max_digits=7,
		decimal_places=2,  null=False, default=0.00)
	diferencia = models.DecimalField('Total Ventas',max_digits=7,
		decimal_places=2,  null=False, default=0.00)

	def generar_informe(self):
			return mark_safe('<a target="_blank" href="/informe/'+str(self.id)+'"class="informe">Imprimir</a>')



	def save (self, force_insert=False, force_update=False, using=None):
		self.total_compras=self.total_compras-self.total_compras
		self.total_ventas=self.total_ventas-self.total_ventas


		for e in Compra.objects.all():
			if (e.fecha >= self.fecha_inicio and e.fecha <= self.fecha_limite):
				self.total_compras+=e.total
						

		for i in Venta.objects.all():
			if (i.fecha >= self.fecha_inicio and i.fecha <= self.fecha_limite):
				self.total_ventas+=i.total

		for j in VentaEscuela.objects.all():
			if (j.fecha >= self.fecha_inicio and j.fecha <= self.fecha_limite):
				self.total_ventas+=j.total

		self.diferencia=self.total_ventas-self.total_compras

		super(InformePorRango, self).save(force_insert, force_update, using)





	class Meta():
		db_table = 'informe_por_rango'
		verbose_name = 'Informe Por Rango de Fecha'
		verbose_name_plural = 'Informes Por Rango de Fecha'


class Inventario(models.Model):

	def generar_inventario(self):
			return mark_safe('<a target="_blank" href="/inventario"class="inventario">Imprimir</a>')



	class Meta():
		db_table = 'inventario'
		verbose_name = 'Inventario de Productos'
		verbose_name_plural = 'Inventario de Productos'

