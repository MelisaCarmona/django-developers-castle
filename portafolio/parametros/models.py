from django.db import models 
#from ckeditor.fields import RichTextField

# Create your models here.
#los modelos son una clase que devuelve un objeto
#clases:Etnias,TipoDocu,TipoEdus,TipoLogr
#clases con nombre de la entidad, definir atributos

#clase Etnia, se encarga:

class Etnia(models.Model):
    NombreEtni=models.CharField(max_length=50)

    # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Grupo Etnico"
        verbose_name_plural = "Grupos Etnicos"

    def __str__(self):
        return self.NombreEtni

        
class TipoDocu(models.Model):
    NombreTiDo=models.CharField(max_length=50)

     # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Tipo De Documento"
        verbose_name_plural = "Tipo De Documentos"

    def __str__(self):
        return self.NombreTiDo

        #clase estado civil

class EstaCivil(models.Model):
    NombEsCi=models.CharField(max_length=50)

     # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Estado Civil"
        verbose_name_plural = "Estados Civiles"

    def __str__(self):
        return self.NombEsCi


    
class TipoEstu(models.Model):
    NombreTiEs=models.CharField(max_length=50)

     # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Tipo De Estudiante"
        verbose_name_plural = "Tipo De Estudiantes"

    def __str__(self):
        return self.NombreTiEs

        
class TipoLogr(models.Model):
    NombreTiLo=models.CharField(max_length=50)

  # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Tipo De Logro"
        verbose_name_plural = "Tipo De Logros"

    def __str__(self):
        return self.NombreTiLo