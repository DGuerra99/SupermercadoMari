from django.shortcuts import render

#pdf
from django.http import HttpResponse
from django.views.generic import View
import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from datetime import datetime

from .models import *
from compras.models import *
from ventas.models import *
from informes.models import *


class ProductosGeneralPDF(View):#PDF para la constancia de Estudios

	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path


	def get(self, request, *args, **kwargs):
   
		try:
			template = get_template('principal/InventarioGeneral.html')#define la ruta del html a ser pdf
			context = {
				'productos': Producto.objects.all(),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
				#'mercadito': {'name': 'Instituto Nacional de Educacion Diversificada', 'dir': 'Concepción Las Minas, Chiquimula', 'cod': '20-08-0006-46/20-08-0020-46'},
				'icon': '{}{}'.format(settings.MEDIA_URL, 'logo.png'),
				'fecha': datetime.now().date()
			}#dixionario de datos
			html = template.render(context)#manda el dixionario de datos
			response = HttpResponse(content_type='application/pdf')
			#response['Content-Disposition'] = 'attachment; filename="cosntancia.pdf"'
			pisaStatus = pisa.CreatePDF(

				html, dest=response,#crea el html
				link_callback=self.link_callback)#llama la imagen

			return response
		except:
 			pass
		return HttpResponse(' Error 404  el PDF no se pudo generar  ')




class ComprasYVentasPDF(View):#PDF para la constancia de Estudios

	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path


	def get(self, request, *args, **kwargs):
   
	
		template = get_template('principal/InformeComprasVentas.html')#define la ruta del html a ser pdf
		context = {
			'compras': Compra.objects.all(),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'ventas': Venta.objects.all(),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'ventasescuelas': VentaEscuela.objects.all(),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'rango': InformePorRango.objects.get(pk=self.kwargs['pk']),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			#'mercadito': {'name': 'Instituto Nacional de Educacion Diversificada', 'dir': 'Concepción Las Minas, Chiquimula', 'cod': '20-08-0006-46/20-08-0020-46'},
			'icon': '{}{}'.format(settings.MEDIA_URL, 'logo.png'),
			'fecha': datetime.now().date()
		}#dixionario de datos
		html = template.render(context)#manda el dixionario de datos
		response = HttpResponse(content_type='application/pdf')
		#response['Content-Disposition'] = 'attachment; filename="cosntancia.pdf"'
		pisaStatus = pisa.CreatePDF(

			html, dest=response,#crea el html
			link_callback=self.link_callback)#llama la imagen

		return response
		




class ComprovantePDF(View):#PDF para la constancia de Estudios

	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path


	def get(self, request, *args, **kwargs):
   
		try:
			template = get_template('principal/ComprovanteVenta.html')#define la ruta del html a ser pdf
			context = {
				'venta': Venta.objects.get(pk=self.kwargs['pk']),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
				#'mercadito': {'name': 'Instituto Nacional de Educacion Diversificada', 'dir': 'Concepción Las Minas, Chiquimula', 'cod': '20-08-0006-46/20-08-0020-46'},
				'icon': '{}{}'.format(settings.MEDIA_URL, 'logo.png'),
				'fecha': datetime.now().date()
			}#dixionario de datos
			html = template.render(context)#manda el dixionario de datos
			response = HttpResponse(content_type='application/pdf')
			#response['Content-Disposition'] = 'attachment; filename="cosntancia.pdf"'
			pisaStatus = pisa.CreatePDF(

				html, dest=response,#crea el html
				link_callback=self.link_callback)#llama la imagen

			return response
		except:
 			pass
		return HttpResponse(' Error 404  el PDF no se pudo generar  ')




class ComprovanteEscuelaPDF(View):#PDF para la constancia de Estudios

	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path


	def get(self, request, *args, **kwargs):
   
		try:
			template = get_template('principal/ComprovanteVentaEscuela.html')#define la ruta del html a ser pdf
			context = {
				'venta': VentaEscuela.objects.get(pk=self.kwargs['pk']),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
				#'mercadito': {'name': 'Instituto Nacional de Educacion Diversificada', 'dir': 'Concepción Las Minas, Chiquimula', 'cod': '20-08-0006-46/20-08-0020-46'},
				'icon': '{}{}'.format(settings.MEDIA_URL, 'logo.png'),
				'fecha': datetime.now().date()
			}#dixionario de datos
			html = template.render(context)#manda el dixionario de datos
			response = HttpResponse(content_type='application/pdf')
			#response['Content-Disposition'] = 'attachment; filename="cosntancia.pdf"'
			pisaStatus = pisa.CreatePDF(

				html, dest=response,#crea el html
				link_callback=self.link_callback)#llama la imagen

			return response
		except:
 			pass
		return HttpResponse(' Error 404  el PDF no se pudo generar  ')