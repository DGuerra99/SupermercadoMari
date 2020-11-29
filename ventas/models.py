# -*- coding: utf-8 -*-
from django.db import models

from administracion.models import *
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

class Venta(models.Model): 
	cliente=models.CharField('Cliente', max_length=150, null=False)
	nit = models.CharField('NIT', max_length=15, null=False)
	fecha=models.DateField('Fecha', auto_now_add=True)
	total=models.DecimalField('Total', max_digits=7, decimal_places=2, default  =0.00)

	def __str__(self):
		return "%s %s %s %s" %(self.cliente, self.id, self.total, self.fecha)

	def generar_comprovante(self):
			return mark_safe('<a target="_blank" href="/comprovante/'+str(self.id)+'"class="informe">Imprimir</a>')


	class Meta():
		db_table = 'venta'
		verbose_name = 'Venta'
		verbose_name_plural = 'Ventas'


class DetalleVenta(models.Model,):
	venta=models.ForeignKey(Venta, on_delete=models.CASCADE, null=False)
	producto=models.ForeignKey(Producto, on_delete=models.CASCADE, null=False)
	cantidad= models.PositiveIntegerField('Cantidad')
	sub_total=models.DecimalField('Sub Total', max_digits=7, decimal_places=2, default  =0.00)

	def clean(self):
		super(DetalleVenta, self).clean()

		if (self.producto.existencia<self.cantidad ):
			raise ValidationError('No posee suficiente Exitencia para completar la Venta')



	def save (self, force_insert=False, force_update=False, using=None):

		# metodo para la operación del subtotal
		self.sub_total = (self.cantidad * self.producto.precio_venta)

		# metodo para sumar las existencias del producto
		product = Producto.objects.filter(nombre = self.producto).first()
		product.existencia = (product.existencia - self.cantidad)
		print(product.existencia)
		product.save()

		# metodo para sumar el total de Comprobantecompra
		comprobante = Venta.objects.all().last()
		comprobante.total = (comprobante.total + self.sub_total)
		comprobante.save()

		super(DetalleVenta, self).save(force_insert, force_update, using)



	def delete (self, *args, **kwargs):

		# metodo para restar existencias cuando se le resta la cantidad
		product = Producto.objects.filter(nombre = self.producto).first()
		product.existencia = (product.existencia + self.cantidad)
		print(product.existencia)
		product.save()

		# metodo para restar total cuando se elimina existencias
		comprobante = Venta.objects.all().last()
		comprobante.total = (comprobante.total - self.sub_total)
		comprobante.save()


		super(DetalleVenta, self).delete(*args, **kwargs)



	class Meta():
		db_table = 'detalle_venta'
		verbose_name = 'Detalle de Venta'
		verbose_name_plural = 'Detalles de Ventas'




class VentaEscuela(models.Model): 
	escuela=models.ForeignKey(Escuela, on_delete=models.CASCADE, null=False)
	fecha=models.DateField('Fecha', auto_now_add=True)
	total=models.DecimalField('Total', max_digits=7, decimal_places=2, default  =0.00)

	def __str__(self):
		return "%s %s %s %s" %(self.escuela.nombre, self.id, self.total, self.fecha)

	def generar_comprovante(self):
			return mark_safe('<a target="_blank" href="/comprovanteescuela/'+str(self.id)+'"class="informe">Imprimir</a>')


	class Meta():
		db_table = 'venta_escuela'
		verbose_name = 'Venta a Escuela'
		verbose_name_plural = 'Ventas a Escuelas'


class DetalleVentaEscuela(models.Model,):
	venta_escuela=models.ForeignKey(VentaEscuela, on_delete=models.CASCADE, null=False)
	producto=models.ForeignKey(Producto, on_delete=models.CASCADE, null=False)
	cantidad= models.PositiveIntegerField('Cantidad')
	sub_total=models.DecimalField('Sub Total', max_digits=7, decimal_places=2, default  =0.00)

	def clean(self):
		super(DetalleVentaEscuela, self).clean()

		if (self.producto.existencia<self.cantidad ):
			raise ValidationError('No posee suficiente Exitencia para completar la Venta')


	def save (self, force_insert=False, force_update=False, using=None):

		# metodo para la operación del subtotal
		self.sub_total = (self.cantidad * self.producto.precio_venta)

		# metodo para sumar las existencias del producto
		product = Producto.objects.filter(nombre = self.producto).first()
		product.existencia = (product.existencia - self.cantidad)
		print(product.existencia)
		product.save()

		# metodo para sumar el total de Comprobantecompra
		comprobante = VentaEscuela.objects.all().last()
		comprobante.total = (comprobante.total + self.sub_total)
		comprobante.save()

		super(DetalleVentaEscuela, self).save(force_insert, force_update, using)



	def delete (self, *args, **kwargs):

		# metodo para restar existencias cuando se le resta la cantidad
		product = Producto.objects.filter(nombre = self.producto).first()
		product.existencia = (product.existencia + self.cantidad)
		print(product.existencia)
		product.save()

		# metodo para restar total cuando se elimina existencias
		comprobante = VentaEscuela.objects.all().last()
		comprobante.total = (comprobante.total - self.sub_total)
		comprobante.save()


		super(DetalleVentaEscuela, self).delete(*args, **kwargs)



	class Meta():
		db_table = 'detalle_venta_escuela'
		verbose_name = 'Detalle de Venta a Escuelas'
		verbose_name_plural = 'Detalles de Ventas a Escuelas'



