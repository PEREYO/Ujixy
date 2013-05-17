from django.template import loader, Context, RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Q
from Ujixyapp.models import *
import datetime
from forms import *
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.files.base import ContentFile 
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.shortcuts import get_object_or_404
#from django.views.generic.simple import direct_to_template
#from cart import Cart
#Sesiones y usuarios

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

			
	

# Create your views here.

@login_required(login_url='/Inicio')
def about_pages(request, page):
	try:
		return direct_to_template(request, template="about/%s.html" % page)
	except TemplateDoesNotExist:
		raise Http404()
		
	
############################### VISTA NOTICIAS ###############################

@login_required(login_url='/Inicio')
def BusquedaNoticias(request):
	query = request.GET.get('q', '')
	if query:
		qset = (Q(titulo__icontains=query))
		results = Noticia.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("noticias/buscar_noticias.html", {
			"tipoplantilla" : "bases/base_noticias.html",
			"results": results,
			"query": query,
			'usuario': request.user},
			context_instance=RequestContext(request))

@login_required(login_url='/Inicio')	
def ArchivoNoticias(request):
	noticias = Noticia.objects.all()
	return render_to_response("noticias/archivo_noticias.html",
		{'noticias': noticias, 'usuario': request.user},
		context_instance=RequestContext(request))

@login_required(login_url='/Inicio')
def NuevaNoticia(request):
	usuario = request.user
	if request.method == 'POST':
		form = NoticiaForm(request.POST)
		if form.is_valid():
			form.save()
			n=Noticia.objects.get(id=form.instance.pk)#Noticia recien creada con el formulario
			n.redactor=usuario.get_profile()#asignamos quien ha redactado la noticia
			n.save()
			return HttpResponseRedirect('/MostrarNoticia/'+str(n.id)+'/')
	else:
		form = NoticiaForm()
	return render_to_response('noticias/nueva_noticia.html', {'form': form, 'usuario': usuario},
								context_instance=RequestContext(request))

@login_required(login_url='/Inicio')	
def MostrarNoticia(request, slug):
	noticia = get_object_or_404(Noticia, slug=slug)
	return render_to_response("noticias/noticia.html",
		{'noticia': noticia, 'usuario': request.user},
		context_instance=RequestContext(request))
		


############################### VISTA MUSICOS ###############################

#@login_required(login_url='/Inicio')
#def ArchivoMusicos(request):
	#musicos = Usuario.objects.filter(musico=True)
	#return render_to_response("musicos/archivo_musicos.html",
		#{'musicos': musicos, 'usuario': request.user},
		#context_instance=RequestContext(request))
		
#@login_required(login_url='/Inicio')		
#def BusquedaMusicos(request):
	#query = request.GET.get('q', '')
	#if query:
		#qset = (Q(nombre_artistico__icontains=query))
		#results =Usuario.objects.filter(qset).distinct()
	#else:
		#results = []
	#return render_to_response("musicos/buscar_musicos.html", {
			#"tipoplantilla" : "bases/base_musicos.html",
			#"results": results,
			#"query": query,
			#'usuario': request.user},
			#context_instance=RequestContext(request))

#@login_required(login_url='/Inicio')		
#def MostrarMusico(request, offset):
	#offset = int(offset)
	#musico=Usuario.objects.get(id=offset)
	#return render_to_response("musicos/musico.html",
		#{'musico': musico, 'usuario': request.user},
		#context_instance=RequestContext(request))
		


			
############################### VISTA GRUPOS ############################### 

@login_required(login_url='/Inicio')
def ArchivoGrupos(request):
	grupos = GrupoDeMusica.objects.all()
	return render_to_response("grupos/archivo_grupos.html",
		{'grupos': grupos, 'usuario': request.user},
		context_instance=RequestContext(request))
		
@login_required(login_url='/Inicio')		
def MostrarGrupo(request,slug):
	grupo = get_object_or_404(GrupoDeMusica, slug=slug)
	return render_to_response("grupos/grupo.html",
		{'grupo': grupo, 'usuario': request.user},
		context_instance=RequestContext(request))
		
@login_required(login_url='/Inicio')		
def BusquedaGrupos(request):
	query = request.GET.get('q', '')
	if query:
		qset = (Q(nombre_grupo__icontains=query))
		results = GrupoDeMusica.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("grupos/buscar_grupos.html", {
			"tipoplantilla" : "bases/base_grupos.html",
			"results": results,
			"query": query,
			'usuario': request.user},
			context_instance=RequestContext(request))
			
@login_required(login_url='/Inicio')
def NuevoGrupo(request):
	usuario=request.user
	print usuario.username
	if request.method == 'POST':
		n=request.POST['nombre_grupo']
		des=request.POST['descripcion_grupo']
		data={'usuario' : usuario.get_profile().id , 'nombre_grupo' : n  , 'descripcion_grupo' : des  }
		form = GrupoForm(data)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/NuevoIntegrante/')
			print "save"
			#g=GrupoDeMusica.objects.get(id=form.instance.pk)#Grupo recien creado con el formulario
			#g.usuario=usuario.get_profile().id#Asignamos al grupo el usuario
	else:
			form=GrupoForm()
	return render_to_response('grupos/crear_grupo.html', { 'usuario':usuario, 'form' : form},
			context_instance=RequestContext(request))
			
@login_required(login_url='/Inicio')			
def NuevoIntegrante(request):
	usuario=request.user
	if request.method == 'POST':
		form = IntegranteForm(request.POST)
		if form.is_valid():
			form.save()
			i=Integrante.objects.get(id=form.instance.pk)#Integrante recien creado con el formulario
			g=GrupoDeMusica.objects.get(usuario=usuario.get_profile().id)#Grupo asociado al usuario
			i.grupo=g
			i.save()
	else:
			form=IntegranteForm()
	return render_to_response('grupos/crear_integrante.html', { 'usuario':usuario, 'form' : form},
			context_instance=RequestContext(request))
		
@login_required(login_url='/Inicio')			
def MostrarIntegrante(request, slug):
	integrante = get_object_or_404(Integrante, slug=slug)
	return render_to_response("grupos/integrante.html",
		{'integrante': integrante, 'usuario': request.user},
		context_instance=RequestContext(request))		

			
############################### VISTAS USUARIOS ###############################
								
								
@login_required(login_url='/Inicio')
def Perfil(request):
	usuario = request.user
	return render_to_response('usuarios/perfil.html',{'usuario' : usuario},
								context_instance=RequestContext(request))
								
@login_required(login_url='/Inicio')
def CerrarSesion(request):
	logout(request)
	#BorrarCarrito(request)
	return HttpResponseRedirect("/Inicio")

############################### VISTAS ADICIONALES ###############################

@login_required(login_url='/Inicio')
def Contacto(request):
	if request.method == 'POST':
		form = ContactoForm(request.POST)
		
		mensaje =ContactoForm.min_palabras(form)
		if form.is_valid():
			asunto= form.cleaned_data['asunto']
			mensaje =form.cleaned_data['mensaje']
			correo = form.cleaned_data.get('correo', 'noreply@ejemplo.com')
			
			send_mail(
				'Feedback from your site, topic: %s' % asunto,
				mensaje, correo,
				['jesus.pereirarivas@gmail.com']
			)
			return HttpResponseRedirect('/Contacto/')
	else:
		form = ContactoForm()
		
	return render_to_response('contacto.html', {'form': form, 'usuario': request.user},context_instance=RequestContext(request))
	
	
def Inicio(request):	
	if request.method == 'POST':
		if 'ingresar' in request.POST:
			ingresarform = AuthenticationForm(request.POST)
			if ingresarform.is_valid:
				nombre=request.POST['username']
				contrasena=request.POST['password']
				usuario = authenticate(username=nombre, password=contrasena)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect("/Perfil/")
				else:
					return HttpResponseRedirect("/account/invalid/")
		elif 'registrar' in request.POST:
			registrarform = UserCreationForm(request.POST)	
			if registrarform.is_valid():
				registrarform.save()
				print "save"
				nombre=request.POST['username']
				contrasena=request.POST['password1']
				usuario = authenticate(username=nombre, password=contrasena)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					u=Usuario(user=request.user)
					u.save()
					return HttpResponseRedirect("/Perfil/")
				else:
					return HttpResponseRedirect("/account/invalid/")
			else:
				return HttpResponseRedirect("/ERROR/")
	else:
		ingresarform = AuthenticationForm()
		registrarform = UserCreationForm()
	return render_to_response('inicio.html', {'ingresarform':ingresarform,
								'registrarform' : registrarform},context_instance=RequestContext(request))
								
								

############################### VISTAS CARRITO ###############################


#def AgregarAlCarrito(request, producto, cantidad):
	#cart = Cart(request)
	#cart.add(producto, producto.precio, cantidad)

#def EliminarDelCarrito(request, p_id):
	#producto = Producto.objects.get(id=p_id)
	#cart = Cart(request)
	#cart.remove(producto)
	
#def BorrarCarrito(request):
	#cart = Cart(request)
	#cart.clear()

	


