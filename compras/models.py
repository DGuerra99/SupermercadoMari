# -*- coding: utf-8 -*-
from django.db import models

from administracion.models import *


class Compra(models.Model):
	proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=False)
	fecha=models.DateField('Fecha', auto_now_add=True)
	fecha_de_compra=models.DateField('Fecha de Compra')
	numero_factura= models.PositiveIntegerField('Número de Factura', help_text='Solo Incluir Numeros')
	total=models.DecimalField('Total', max_digits=7, decimal_places=2, default  =0.00)




	def __str__(self):
		return "%s %s" %(self.proveedor, self.fecha)



	class Meta():
		db_table = 'compra'
		verbose_name = 'Compra'
		verbose_name_plural = 'Compras'

class DetalleCompra(models.Model):
	compra=models.ForeignKey(Compra, on_delete=models.CASCADE, null=False)
	producto=models.ForeignKey(Producto, on_delete=models.CASCADE, null=False)
	cantidad= models.PositiveIntegerField('Cantidad')
	precio_compra=models.DecimalField('Precio Compra', max_digits=7, decimal_places=2)
	precio_venta=models.DecimalField('Precio Venta', max_digits=7, decimal_places=2)
	subtotal = models.DecimalField('Subtotal', max_digits=7, decimal_places=2, null=True, blank=True)



	def save (self, force_insert=False, force_update=False, using=None):

		# metodo para la operación del subtotal
		self.subtotal = (self.cantidad * self.precio_compra)

		# metodo para sumar las existencias del producto
		product = Producto.objects.filter(nombre = self.producto).first()
		product.existencia = (product.existencia + self.cantidad)
		product.precio_costo = self.precio_compra
		product.precio_venta = self.precio_venta
		print(product.existencia)
		product.save()

		# metodo para sumar el total de Comprobantecompra
		comprobante = Compra.objects.all().last()
		comprobante.total = (comprobante.total + self.subtotal)
		comprobante.save()

		super(DetalleCompra, self).save(force_insert, force_update, using)



	def delete (self, *args, **kwargs):

		# metodo para restar existencias cuando se le resta la cantidad
		product = Producto.objects.filter(nombre = self.producto).first()
		product.existencia = (product.existencia - self.cantidad)
		print(product.existencia)
		product.save()

		# metodo para restar total cuando se elimina existencias
		comprobante = Compra.objects.all().last()
		comprobante.total = (comprobante.total - self.subtotal)
		comprobante.save()


		super(DetalleCompra, self).delete(*args, **kwargs)

    
	class Meta():
		db_table = 'detalle_compra'
		verbose_name = 'Detalle de Compra'
		verbose_name_plural = 'Detalles de Compras'