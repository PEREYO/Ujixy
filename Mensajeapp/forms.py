from django import forms
from django.http import HttpResponse
from django.forms import ModelForm
from django.contrib.auth.models import User
from models import Mensaje


class MensajeForm (ModelForm):
	class Meta:
		model=Mensaje
