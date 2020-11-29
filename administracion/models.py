# -*- coding: utf-8 -*-
from django.db import models






class Proveedor(models.Model):
	nombre = models.CharField('Nombre', max_length=50, null=False)
	nit = models.CharField('NIT', max_length=15, null=False, unique=True)
	direccion = models.CharField('Dirección', max_length=50, null=False)
	numero= models.PositiveIntegerField('Número de Telefono', help_text='Solo Incluir Numeros')
	

	def __str__(self):
		return self.nombre

	class Meta:
		db_table = 'proveedor'
		verbose_name = 'Proveedor'
		verbose_name_plural = 'Proveedores'



class Escuela(models.Model):
	nombre = models.CharField('Nombre', max_length=50, null=False)
	nit = models.CharField('NIT', max_length=15, null=False, unique=True)
	direccion = models.CharField('Dirección', max_length=50, null=False)
	numero= models.PositiveIntegerField('Número de Telefono', help_text='Solo Incluir Numeros')
	

	def __str__(self):
		return self.nombre

	class Meta:
		db_table = 'escuela'
		verbose_name = 'Escuela'
		verbose_name_plural = 'Escuelas'

		


class Producto(models.Model):
	codigo_manual= models.PositiveIntegerField('Codigo Manual', help_text='Solo Incluir Números', null=False, unique=True)
	codigo_barra= models.PositiveIntegerField('Codigo Barra', help_text='Solo Incluir Números', null=False, unique=True)
	nombre = models.CharField('Nombre', max_length=50, null=False)
	proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=False)
	marca = models.CharField('Marca', max_length=50, null=False)
	precio_costo=models.DecimalField('Precio Costo', max_digits=7, 
		decimal_places=2, null=False)
	precio_venta=models.DecimalField('Precio Venta',max_digits=7,
		decimal_places=2,  null=False)
	descripcion = models.TextField('Descripción')
	existencia= models.PositiveIntegerField('Existencia', default=0)

	def __str__(self):
		return self.nombre

	class Meta:
		db_table = 'producto'
		verbose_name = 'Producto'
		verbose_name_plural = 'Productos'


