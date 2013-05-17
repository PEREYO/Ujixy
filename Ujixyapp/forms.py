from django import forms
from models import Noticia, Usuario, GrupoDeMusica, Integrante
from django.http import HttpResponse
from django.forms import ModelForm
from django.contrib.auth.models import User
#from tinymce.widgets import TinyMCE
#from widgets import AdvancedEditor

TOPIC_CHOICES = (
	('general', 'Encuesta general'),
	('bug', 'Informe de error'),
	('sugerencia', 'Sugerencia'),
)
class ContactoForm(forms.Form):
	asunto = forms.ChoiceField(choices=TOPIC_CHOICES)
	mensaje = forms.CharField(widget=forms.Textarea())
	correo = forms.EmailField(required=False)
	#funcion para no admitir mensajes con menos de 4 palabras
	def min_palabras(self):
		mensaje = self.cleaned_data.get('mensaje', '')
		palabras = len(mensaje.split())
		if palabras < 4:
			raise forms.ValidationError("Mensaje demasiado corto! por favor escriba algo mas")

		return mensaje
		
class ComprarForm ( forms.Form):
	nombre=forms.CharField(max_length=155)
	apellidos=forms.CharField(max_length=155)
	correo=forms.EmailField()
	direccion=forms.CharField(max_length=155)
	Numero_de_tarjeta_de_credito=forms.CharField(max_length=155)
	telefono=forms.CharField(max_length=155)
	

class NoticiaForm (ModelForm):
	class Meta:
		model=Noticia
		exclude = ( 'redactor')

class RegistroForm ( ModelForm):
	 class Meta:
		 model=User
		 
class Imagen (ModelForm):
	class Meta:
		model=Usuario
		fields = ('user', 'imagen')
		
class GrupoForm (ModelForm):
	class Meta:
		model=GrupoDeMusica
		
class IntegranteForm (ModelForm):
	class Meta:
		model=Integrante
		exclude = ( 'grupo')
