from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
from django.utils.encoding import smart_str
import os
from django.utils.translation import gettext_lazy as _
from Ujixyapp.models import GrupoDeMusica
from Ujixy.slughifi import slughifi
from autoslug.fields import AutoSlugField

class Categoria(models.Model):
	nombre = models.CharField(max_length=50)
	slug = AutoSlugField(populate_from='nombre', unique_with='creado_a')
	descripcion = models.TextField()
	activo = models.BooleanField(default=True)
	meta_keywords = models.CharField("Meta Keywords",max_length=255,
	help_text='Comma-delimited set of SEO keywords for meta tag')
	meta_descripcion = models.CharField("Meta Description", max_length=255,
	help_text='Content for description meta tag')
	creado_a = models.DateTimeField(auto_now_add=True)
	actualizado_a = models.DateTimeField(auto_now=True)
	

	class Meta:
		db_table = 'categorias'
		ordering = ['-creado_a']
		verbose_name_plural = 'Categorias'
	def __unicode__(self):
		return self.nombre
	@models.permalink
	def get_absolute_url(self):
		return ('categoria_catalogo', (), { 'categoria_slug': self.slug })


class Producto(models.Model):
	nombre = models.CharField(max_length=255, unique=True, verbose_name='name')
	slug = AutoSlugField(populate_from='nombre', unique_with='creado_a')
	brand = models.CharField(max_length=50)
	sku = models.CharField(max_length=50)
	precio = models.DecimalField(max_digits=9,decimal_places=2)
	precio_antiguo = models.DecimalField(max_digits=9,decimal_places=2,
	blank=True,default=0.00)
	imagen = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	is_bestseller = models.BooleanField(default=False)
	is_featured = models.BooleanField(default=False)
	cantidad = models.IntegerField()
	descripcion = models.TextField()
	meta_keywords = models.CharField(max_length=255,
	help_text='Comma-delimited set of SEO keywords for meta tag')
	meta_description = models.CharField(max_length=255,
	help_text='Content for description meta tag')
	creado_a = models.DateTimeField(auto_now_add=True)
	actualizado_a = models.DateTimeField(auto_now=True)
	categorias = models.ManyToManyField(Categoria)
	grupo = models.ForeignKey(GrupoDeMusica, null=True,blank=True, related_name='productos')
	class Meta:
		db_table = 'productos'
		ordering = ['-creado_a']
		verbose_name = _('Product')
	def __unicode__(self):
		return self.nombre
	@models.permalink
	def get_absolute_url(self):
		return ('producto_catalogo', (), { 'producto_slug': self.slug })
	def precio_venta(self):
		if self.precio_antiguo > self.precio:
			return self.precio
		else:
			return None

#admin.site.register(Categoria)
#admin.site.register(Producto)
