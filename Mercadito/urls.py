"""Mercadito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from administracion.views import *

from django.contrib.auth.decorators import login_required #para que sea login


urlpatterns = [
    path('', admin.site.urls),
    path('inventario', login_required(ProductosGeneralPDF.as_view()), name='inventario'),
    path('informe/<int:pk>', login_required(ComprasYVentasPDF.as_view()), name='informe'),  
    path('comprovante/<int:pk>', login_required(ComprovantePDF.as_view()), name='comprovante'),  
    path('comprovanteescuela/<int:pk>', login_required(ComprovanteEscuelaPDF.as_view()), name='comprovanteescuela'),  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
