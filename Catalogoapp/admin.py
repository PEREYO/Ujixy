from django.contrib import admin
from Catalogoapp.models import Producto, Categoria
from Catalogoapp.forms import ProductAdminForm

class ProductAdmin(admin.ModelAdmin):
	form = ProductAdminForm
	# sets values for how the admin site lists your products
	list_display = ('nombre', 'precio', 'precio_antiguo', 'creado_a', 'actualizado_a',)
	list_display_links = ('nombre',)
	list_per_page = 50
	ordering = ['-creado_a']
	search_fields = ['nombre', 'descripcion', 'meta_keywords', 'meta_description']
	#exclude = ('creado_a', 'actualizado_a',)
	# sets up slug to be generated from product nombre
	prepopulated_fields = {'slug' : ('nombre',)}
# registers your product model with the admin site
admin.site.register(Producto, ProductAdmin)
class CategoryAdmin(admin.ModelAdmin):
	#sets up values for how admin site lists categories
	list_display = ('nombre', 'creado_a', 'actualizado_a',)
	list_display_links = ('nombre',)
	list_per_page = 20
	ordering = ['nombre']
	search_fields = ['nombre', 'descripcion', 'meta_keywords', 'meta_description']
	#exclude = ('creado_a', 'actualizado_a',)
# sets up slug to be generated from category nombre
prepopulated_fields = {'slug' : ('nombre',)}
admin.site.register(Categoria, CategoryAdmin)

