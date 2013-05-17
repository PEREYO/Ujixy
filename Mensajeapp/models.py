from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.template import defaultfilters
from Ujixy.slughifi import slughifi
from autoslug.fields import AutoSlugField


# Create your models here.

class Mensaje(models.Model):
	asunto = models.CharField(max_length=155, null=True,blank=True, verbose_name='subject')
	mensaje = models.TextField()#message
	slug = AutoSlugField(populate_from='asunto', unique_with='creado_a')
	envia = models.ForeignKey(User, null=True,blank=True, related_name='mensajes_enviados')
	recibe = models.ForeignKey(User, null=True,blank=True, related_name='mensajes_recibidos')
	creado_a = models.DateTimeField(auto_now_add=True)
	inbox = models.BooleanField(default=True) # Esta el mensaje en recibidos, si no, ha sido leido
	is_active_sent = models.BooleanField(default=True) # Es visible para el usuario que envia, si no, el mensaje ha sido eliminado
	is_active_received = models.BooleanField(default=True) # Es visible para el usuario que recibe, si no, el mensaje ha sido eliminado
	
	def save(self, *args, **kwargs):
		self.slug = slughifi(self.asunto)
		super(Mensaje, self).save(*args, **kwargs)

admin.site.register(Mensaje)
