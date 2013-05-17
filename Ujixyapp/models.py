from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
from django.utils.encoding import smart_str
import os
from django.views.generic import ListView
from django.contrib.auth.admin import UserAdmin
from django.core.urlresolvers import reverse
from Ujixy.slughifi import slughifi
from autoslug.fields import AutoSlugField





class Usuario(models.Model):
	
	user = models.ForeignKey(User, unique=True)
	productos_comprados = models.ManyToManyField('Catalogoapp.Producto', null=True,blank=True)
	imagen = models.ImageField(null=True,blank=True, upload_to='media/foto_perfil')
	
	def __str__(self):
		return smart_str(self.user.username)

class GrupoDeMusica ( models.Model):
	usuario = models.ForeignKey(Usuario, unique=True, related_name='grupo')
	slug = AutoSlugField(populate_from='nombre_grupo', unique_with='usuario')
	nombre_grupo = models.CharField(max_length=150)
	estilo = models.ManyToManyField('Catalogoapp.Categoria')
	descripcion_grupo=models.TextField(null=True,blank=True)
	imagen = models.ImageField(null=True,blank=True, upload_to='media/grupos')
	
	
	def __str__(self):
		return smart_str(self.nombre_grupo)
		
#class Producto (models.Model):
	#nombre_producto = models.CharField(max_length=150)
	#tipo = models.CharField(max_length=155)
	#precio = models.FloatField ()
	#descripcion_producto=models.TextField(null=True,blank=True)
	#imagen = models.ImageField(null=True,blank=True, upload_to='media/productos')
	#stock = models.IntegerField ()
	#grupo = models.ForeignKey(GrupoDeMusica, null=True,blank=True, related_name='productos')
	#unidades_vendidas=models.IntegerField (blank=True, default=0)
	
	#paginate_by = 2
	
	#def __str__(self):
		#return smart_str(self.nombre_producto)
		
class Integrante (models.Model):
	nombre = models.CharField(max_length=150)
	slug = AutoSlugField(populate_from='nombre', unique_with='id')
	funcion = models.CharField(max_length=150)
	descripcion_integrante=models.TextField(null=True,blank=True)
	grupo = models.ForeignKey (GrupoDeMusica, null=True,blank=True, related_name='integrantes')
	
	def __str__(self):
		return smart_str(self.nombre)

class Noticia(models.Model):
	titulo = models.CharField(max_length=150)
	#my_field = tinymce_models.HTMLField() 
	slug = AutoSlugField(populate_from='titulo', unique_with='creado_a')
	cuerpo = models.TextField()
	creado_a = models.DateTimeField(auto_now=True)
	actualizado_a = models.DateTimeField(auto_now=True)
	imagen = models.ImageField(null=True,blank=True, upload_to='media/noticias')
	redactor=models.ForeignKey(Usuario, null=True,blank=True, related_name='noticias')
	
	def __str__(self):
		return smart_str(self.titulo)
	
	class Meta:
		ordering = ('-creado_a',)
		
		




admin.site.register(Usuario)
admin.site.register(GrupoDeMusica)
admin.site.register(Noticia)

