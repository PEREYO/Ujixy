from django.template import loader, Context, RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Q
from models import *
import datetime
from forms import *
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.files.base import ContentFile 
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required(login_url='/Inicio')	
def MostrarMensaje(request, slug):
	mensaje = get_object_or_404(Mensaje, slug=slug)
	if request.method == 'POST':
		m=request.POST['mensaje']
		print request.user.id
		data={'envia' : request.user.id , 'recibe' : mensaje.envia.id  , 'mensaje' : m } #Ahora recibe es quien envio el mensaje
		form = MensajeForm(data)
		if form.is_valid():
			form.save()
	else:
			form=MensajeForm()
	return render_to_response("mensaje.html",
		{'mensaje': mensaje, 'usuario': request.user, 'form': form },
		context_instance=RequestContext(request))
		
@login_required(login_url='/Inicio')
def ArchivoMensajes(request):
	mensajes = Mensaje.objects.filter(recibe=request.user.id)
	print "hola"
	print mensajes
	return render_to_response("recibidos.html",
		{'mensajes': mensajes, 'usuario': request.user},
		context_instance=RequestContext(request))
