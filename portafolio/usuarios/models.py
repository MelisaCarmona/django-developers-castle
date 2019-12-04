from django.db import models
from django.conf import settings
from ckeditor.fields import Richtextfield
from parametros.models import TipoDocu, Empleos, EstaCivil, Etnia, TipoLogr, TipoEstu


# Create your models here.

class Usuario (models.Model):
	IdUsuario = models.CharField(max_length= 50,verbose_name = "No. Identificación", default="")
	idTipoDocu = models.ForeignKey(TipoDocu, default="", on_delete = models.CASCADE, verbose_name = "Tipo de Documento")
	idEstaCivil = models.ForeignKey(EstaCivil, default="", on_delete = models.CASCADE, verbose_name="Estado Civil")
	idEtnias = models.ForeignKey(Etnia, default="", on_delete = models.CASCADE, verbose_name="Etnias")
	ImagUsua = models.ImageField(verbose_name = "Foto de Perfil", upload_to = "perfiles/img")
	PerfiPro = Richtextfield(default="Candidato...", verbose_name = "Perfil profesional")
	GeneUsua = models.CharField(max_length=1, default="0", verbose_name = "Género")
	TeleUsua = models.CharField(max_length=20, default="0", verbose_name = "Teléfono")
	CeluUsua = models.CharField(max_length=20, default="0", verbose_name = "Celular")
	DireUsua = models.TextField(default = "0", verbose_name="Direccion Postal")
	RegiUsua = models.DateTimeField(default = 0, auto_now_add = False, verbose_name="Registrado el:")
	EstaUsua = models.CharField(max_length=50, default="Activo", verbose_name = "Estado")

    class Meta:
		verbose_name = "Candidato"
		verbose_name_plural= "Candidatos"

	#despues de crear la clase, retornamos el objeto NombEtni
	def __str__(self):
		return self.idUsuario

class Experiencia(models.Model):
	#atributos
	CargExpe = models.ForeignKey(Empleos, on_delete=models.CASCADE, limit_choices_to={'EsCargo':'SI'}, verbose_name="Cargo Ocupado")
	EmprExpe = models.CharField(max_length=150,verbose_name="Empresa")
	TeleEmpr = models.CharField(max_length=30,verbose_name="Teléfono de contácto de la Empresa")
	JefeExpe = models.CharField(max_length=30,verbose_name="Persona de contácto de la Empresa")
	FechInic = models.DateTimeField(auto_now_add = False, default=0, verbose_name="Fecha de Inicio")
	FechaFin = models.DateTimeField(auto_now_add = False, default=0, verbose_name="Fecha de Terminación")
	FuncionE = Richtextfield(verbose_name="Funciones Desempeñadas")
	LogrExpe = Richtextfield(verbose_name="Logros Alcanzados")
	SopoExpe = models.FileField(upload_to="soportes/laboral", default="", verbose_name="Certificación Laboral")
	EstaExpt = models..CharField(max_length=30,default="Activo", verbose_name="Estado de Experiencia")

	class Meta:
		verbose_name = "Experiencia"
		verbose_name_plural = "Experiencia Laboral"

	def __str__(self):
	   return self.CargExpe	

class Educacion(models.Model):
	TipoEstu = models.ForeignKey(TipoEstu, on_delete=models.CASCADE, default="", verbose_name="Tipo de Educación")
	Instituto = models.CharField(max_length=30, default="Activo", verbose_name="Institución o Academia")
	TituloEst = models.CharField(max_length=250, verbose_name="Titulo Obtenido")
	FechGrado = models.DateTimeField(auto_now_add = False, default=0, verbose_name="Fecha de Graduación")
	SoporteEs = models.FileField(upload_to="soportes/educacion", default="", verbose_name="Soporte Educación")
	EstaEstu = models.CharField(max_length=30, default="Activo", verbose_name="Estado de Educación")

	class Meta:
		verbose_name = "Educación"
		verbose_name_plural = "Estudios Registrados"

    def __str__(self):
       return self.TituloEst

#Clase de logros

class Logros(models.Model):
	NombTilo = models.ForeignKey(TippoLogr, on_delete=models.CASCADE, verbose_name="Tipo de Logro")
	FechLogr = models.DateTimeField(auto_now_add = False, default=0, verbose_name="Fecha de culminación de Logro")
	NombLogr = models.CharField(max_length= 100, default="Activo", verbose_name="Logro o Distición")
	DescLogr = Richtextfield(verbose_name="Descripción o características del logro")
    
    class Meta:
    	verbose_name = "Logros"
    	verbose_name_plural = "Logros Obtenidos"

    def __str__(self):
    	return self.NombLogr

 #Clase habilidades

 class Habilidades(models.Model):
 	NombHabil = models.CharField(max_length=100, default="Activo", verbose_name="Habilidad")
    NiveHabil = models.CharField(max_length=20, default="Activo", verbose_name="Nivel de Habilidades")

    class Meta:
    	 return self.NombHabil



