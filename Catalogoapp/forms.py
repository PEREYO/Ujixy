from django import forms
from models import Producto
from django.http import HttpResponse
from django.forms import ModelForm
from Catalogoapp.models import Producto



class ProductoForm ( ModelForm):
	class Meta:
		model=Producto
		exclude = ( 'unidades_vendidas', 'grupo')
		
class ProductAdminForm(forms.ModelForm):
	class Meta:
		model = Producto
	def clean_price(self):
		if self.cleaned_data['precio'] <= 0:
			raise forms.ValidationError('Price must be greater than zero.')
		return self.cleaned_data['precio']

