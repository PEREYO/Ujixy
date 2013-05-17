from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView
#from django.views.generic.simple import direct_to_template


admin.autodiscover()

admin.autodiscover()

urlpatterns = patterns('Ujixyapp.views',
    # Example:
    # (r'^Ujixy/', include('Ujixy.foo.urls')),

    

    
    
    #(r'^invitado/$', 'PerfilInvitado'),
    #Enlaces noticias
    
    (r'^BusquedaNoticias/$', 'BusquedaNoticias'),
    (r'^ArchivoNoticias/$', 'ArchivoNoticias'),
    (r'^Contacto/$', 'Contacto'),
    (r'^MostrarNoticia/(\d+)/$', 'MostrarNoticia'),
    
    
    #(r'^ComprarCarrito/(\d+)/$', 'ComprarCarrito'),
    
    
     #Enlaces musicos
    #(r'^ArchivoMusicos/$', 'ArchivoMusicos'),
    #(r'^MostrarMusico/(\d+)/$', 'MostrarMusico'),
    #(r'^BusquedaMusicos/$', 'BusquedaMusicos'),
    #(r'^NuevoMusico/$', 'NuevoMusico'),
    
    #Enlaces grupos
    (r'^ArchivoGrupos/$', 'ArchivoGrupos'),
    (r'^MostrarGrupo/(?P<slug>[\w-]+)$', 'MostrarGrupo'),
    (r'^BusquedaGrupos/$', 'BusquedaGrupos'),
    (r'^NuevoGrupo/$', 'NuevoGrupo'),
    (r'^NuevoIntegrante/$', 'NuevoIntegrante'),
    (r'^MostrarIntegrante/(?P<slug>[\w-]+)$', 'MostrarIntegrante'),
    
    #Enlaces Usuarios
    (r'^Perfil/$', 'Perfil'),
    (r'^CerrarSesion/$', 'CerrarSesion'),
    
    #Enlaces varios
    
    (r'^Inicio/$', 'Inicio'),
    #(r'^ComprarCarrito/$', 'ComprarCarrito'),
    (r'^NuevaNoticia/$', 'NuevaNoticia'),
    #('^about/$', direct_to_template, {'template': 'about.html'}),
    ('^about/(w+)/$', 'about_pages'),
    (r'^accounts/login/$', 'login'),
	(r'^accounts/logout/$', 'logout'),

	




)
urlpatterns += patterns('Catalogoapp.views',

	#Enlaces productos
    
    (r'^ArchivoProductos/$', 'ArchivoProductos'),
    (r'^BusquedaProductos/$', 'BusquedaProductos'),
    (r'^Vender/$', 'NuevoProducto'),
    (r'^MostrarProducto/(?P<slug>[\w-]+)$', 'MostrarProducto'),
    
)

urlpatterns += patterns('Mensajeapp.views',

	#Enlaces mensajes
    (r'^ArchivoMensajes/$', 'ArchivoMensajes'),
    (r'^MostrarMensaje/(?P<slug>[\w-]+)$', 'MostrarMensaje'),
    
) 
urlpatterns += patterns('',
	# Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	# Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_DOC_ROOT}),
	(r'^tinymce/', include('tinymce.urls')),
	#(r'^messages/', include('postman.urls'))
#	url(r'^messages/', RedirectView.as_view(url='messages.urls'))
	
)



