from django.template import loader, Context, RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Q
from Catalogoapp.models import Producto
from Ujixyapp.models import GrupoDeMusica
import datetime
from forms import *
from Mensajeapp.forms import MensajeForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.files.base import ContentFile 
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.contrib.auth.decorators import login_required
import pdb;

############################### VISTA PRODUCTOS ###############################

@login_required(login_url='/Inicio')
def ArchivoProductos(request):
	productos = Producto.objects.all()
	return render_to_response("productos/archivo_productos.html",
		{'productos': productos, 'usuario': request.user},
		context_instance=RequestContext(request))

@login_required(login_url='/Inicio')
def BusquedaProductos(request):
	query = request.GET.get('q', '')
	if query:
		qset = (Q(nombre_producto__icontains=query))
		results = Producto.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("productos/buscar_productos.html", {
			"tipoplantilla" : "bases/base_productos.html",
			"results": results,
			"query": query,
			'usuario': request.user},
			context_instance=RequestContext(request))
			
@login_required(login_url='/Inicio')			
def NuevoProducto(request):
	usuario=request.user
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
			#print m
			g=GrupoDeMusica.objects.get(usuario=usuario.get_profile().id)#GrupodeMusica asociado al usuario actual 
			p=Producto.objects.get(id=form.instance.pk)#producto recien creado con el formulario
			#print p
			#ps=Producto.objects.all()
			#for producto in ps:
			#	if producto==p:				
			p.grupo=g#asignamos quien ha creado el producto
			p.save()
			
			return HttpResponseRedirect('/MostrarProducto/'+str(p.id)+'/')
	else:
		form = ProductoForm()		
	return render_to_response('productos/vender.html', {'form': form, 'usuario': usuario},
								context_instance=RequestContext(request))

@login_required(login_url='/Inicio')	
def MostrarProducto(request, offset):
	pdb.set_trace()
	offset = int(offset)#id del producto
	producto=Producto.objects.get(id=offset)
	if request.method == 'POST':
		m=request.POST['mensaje']
		print request.user.id
		print request.user.id
		print producto.grupo.usuario.id
		print producto.grupo.usuario
		data={'envia' : request.user.id , 'recibe' : producto.grupo.usuario.id  , 'mensaje' : m }
		form = MensajeForm(data)
		if form.is_valid():
			form.save()
		else:
			pdb.set_trace()
			print "falso"
	else:
			form=MensajeForm()
	#if request.method=='POST':
		#unidades=request.POST['unidades']#unidades a agregar del producto actual
		#AgregarAlCarrito(request, producto, unidades)
	return render_to_response("productos/producto.html",
		{ 'producto': producto, 'usuario': request.user, 'form': form },
		context_instance=RequestContext(request))
		
#@login_required(login_url='/Inicio')	
#def ComprarCarrito(request):
	#usuario=request.user
	#u=usuario.get_profile()#perfil del usuario propio
	##cart=Cart(request)#instancia del carrito actual
	#if request.method == 'POST':
		#form=ComprarForm(request.POST)
		#if form.is_valid():
			#for item in cart:
				#producto=Producto.objects.get(id=item.product.id)
				#producto.unidades_vendidas+=item.quantity #sumamos a las unidades totales que se van a comprar
				#u.productos_comprados.add(producto)
				#producto.save()
			#BorrarCarrito(request)
			#return HttpResponseRedirect("/Perfil/")
			
	#else:
		#form=ComprarForm()
	#return render_to_response("productos/comprar.html",
		#{'cart' : Cart(request), 'usuario': usuario, 'form' : form},
		#context_instance=RequestContext(request))
