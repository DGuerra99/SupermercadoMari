# -*- coding: utf-8 -*-
from django.db import models

from administracion.models import *
from django.core.exceptions import ValidationError

TIPO_DEV  =(
    ('Compra', 'Compra'),
    ('Venta', 'Venta'),
)#Choice para seleccionar tipo de devolucion

class Devolucion(models.Model): 
	tipo_dev=models.CharField(
		'Tipo Devolución',
		max_length=6,
		choices=TIPO_DEV, default= 'Venta')
	motivo = models.TextField('Motivo')
	fecha=models.DateField('Fecha', auto_now_add=True)
	total=models.DecimalField('Total de Devolución', max_digits=7, decimal_places=2, default  =0.00)

	def __str__(self):
		return "%s %s %s %s" %(self.tipo_dev, self.id, self.total, self.fecha)

	class Meta():
		db_table = 'devolucion'
		verbose_name = 'Devolución'
		verbose_name_plural = 'Devoluciones'


class DetalleDev(models.Model,):
	devolucion=models.ForeignKey(Devolucion, on_delete=models.CASCADE, null=False)
	producto=models.ForeignKey(Producto, on_delete=models.CASCADE, null=False)
	cantidad= models.PositiveIntegerField('Cantidad')
	sub_total = models.DecimalField('Subtotal', max_digits=7, decimal_places=2, null=True, blank=True)


	def clean(self):
		super(DetalleDev, self).clean()

		if (self.devolucion.tipo_dev=='Compra' and self.producto.existencia<self.cantidad):
			raise ValidationError('No posee suficiente Exitencia para completar la Devolucion de la Compra')


	def save (self, force_insert=False, force_update=False, using=None):

		if self.devolucion.tipo_dev=='Compra':

			# metodo para la operación del subtotal
			self.sub_total = (self.cantidad * self.producto.precio_costo)

			# metodo para sumar las existencias del producto
			product = Producto.objects.filter(nombre = self.producto).first()
			product.existencia = (product.existencia - self.cantidad)
			print(product.existencia)
			product.save()

			# metodo para sumar el total de Comprobantecompra
			comprobante = Devolucion.objects.all().last()
			comprobante.total = (comprobante.total + self.sub_total)
			comprobante.save()
		else:
			# metodo para la operación del subtotal
			self.sub_total = (self.cantidad * self.producto.precio_venta)

			# metodo para sumar las existencias del producto
			product = Producto.objects.filter(nombre = self.producto).first()
			product.existencia = (product.existencia + self.cantidad)
			print(product.existencia)
			product.save()

			# metodo para sumar el total de Comprobantecompra
			comprobante = Devolucion.objects.all().last()
			comprobante.total = (comprobante.total + self.sub_total)
			comprobante.save()


		super(DetalleDev, self).save(force_insert, force_update, using)


	def delete (self, *args, **kwargs):
		if self.devolucion.tipo_dev=='Compra':

			# metodo para restar existencias cuando se le resta la cantidad
			product = Producto.objects.filter(nombre = self.producto).first()
			product.existencia = (product.existencia + self.cantidad)
			print(product.existencia)
			product.save()

			# metodo para restar total cuando se elimina existencias
			comprobante = Devolucion.objects.all().last()
			comprobante.total = (comprobante.total - self.sub_total)
			comprobante.save()
		else:
			# metodo para restar existencias cuando se le resta la cantidad
			product = Producto.objects.filter(nombre = self.producto).first()
			product.existencia = (product.existencia - self.cantidad)
			print(product.existencia)
			product.save()

			# metodo para restar total cuando se elimina existencias
			comprobante = Devolucion.objects.all().last()
			comprobante.total = (comprobante.total - self.sub_total)
			comprobante.save()


		super(DetalleDev, self).delete(*args, **kwargs)



	class Meta():
		db_table = 'detalle_devolucion'
		verbose_name = 'Detalle de Devolución'
		verbose_name_plural = 'Detalles de Devoluciones'
