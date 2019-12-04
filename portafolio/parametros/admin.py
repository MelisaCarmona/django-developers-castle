from django.contrib import admin

#importacion de clases de models.py:
from.models import Etnia
from.models import TipoDocu
from.models import EstaCivil
from.models import TipoEstu
from.models import TipoLogr

#registrar modulos

admin.site.register(Etnia)
admin.site.register(TipoDocu)
admin.site.register(EstaCivil)
admin.site.register(TipoEstu)
admin.site.register(TipoLogr)


