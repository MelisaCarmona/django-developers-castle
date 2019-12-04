from django.contrib import admin

# Register your models here.
from .models import Usuarios, Experiencia, Educacion, Habilidades, Experiencia, Logros

class UsuariosModelAdmin(admin.ModelAdmin):
	#columnas que se quieren visualizar
	list_display = ("__str__", "IdUsuario", "ImagUsua", "EstaUsua",)
	#barra de busqueda
	search_fields = ('IdUsuario', 'GeneUsua', 'CeluUsua', 'TeleUsua',)
	#se agrega un filtro
	list_filter = ('RegiUsua',)

	#se indica desde donde se obtienen otros parametros

	class Meta:
		model = Usuarios

admin.site.register(Usuarios, UsuariosModelAdmin)

class ExperienciaModelAdmin(admin.ModelAdmin):
	#columnas que se quieren visualizar
	list_display = ("__str__", "CargExpe", "EmprExpe", "FechInicio", "FechaFin", "SopoExpe")
	#barra de busqueda
	search_fields = ('CargExpe', 'EmprExpe',)
	#se agrega un filtro
	list_filter = ('CargExpe', 'FechaFin',)
	#se muestran las fechas de creación de usuario
	readonly_fields = ('EstaExpt',)

	#se indica desde donde se obtienen otros parametros
 	
 	class Meta.
 	  model = Experiencia
admin.site.register(Experiencia,ExperienciaModelAdmin)

class EducacionModelAdmin(admin.ModelAdmin):
	#columnas que se quieren visualizar
	list_display = ("__str__", "TipoEstu", "TituloEst", "FechGrado", "Instituto", "SoporteEs")
	#barra de busqueda
	search_fields = ('TituloEst', 'TipoEstu',)
	#se agrega un filtro
	list_filter = ('TipoEstu', 'FechGrado',)
	#se muestran las fechas de creación de usuario
	readonly_fields = ('EstaEstu',)

	#se indica desde donde se obtienen otros parametros
 	
 	class Meta.
 	  model = Educacion
admin.site.register(Educacion,EducacionModelAdmin)


class LogrosModelAdmin(admin.ModelAdmin):
	#columnas que se quieren visualizar
	list_display = ("__str__", "NombLogr", "FechLogr", "NombTilo")
	#barra de busqueda
	search_fields = ('NombLogr', 'NombTilo', 'FechLogr',)
	#se agrega un filtro
	list_filter = ('NombLogr', 'NombTilo', 'FechLogr',)
	

	#se indica desde donde se obtienen otros parametros
 	
 	class Meta.
 	  model = Logros
admin.site.register(Logros,LogrosModelAdmin)

class HabilidadesModelAdmin(admin.ModelAdmin):
	#columnas que se quieren visualizar
	list_display = ("__str__", "NombHabil", "NiveHabil")
	#barra de busqueda
	search_fields = ('NombHabil', 'NiveHabil',)
	#se agrega un filtro
	list_filter = ('NiveHabil', 'NombHabil', )
	

	#se indica desde donde se obtienen otros parametros
 	
 	class Meta.
 	  model = Habilidades
admin.site.register(Habilidades,HabilidadesModelAdmin)


