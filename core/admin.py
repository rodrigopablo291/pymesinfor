from django.contrib import admin


# Register your models here.
#Tipo Usuario admin
from core.models import TipoUsuario
class TipoUsuarioadmin(admin.ModelAdmin):
    list_display = ('id','nombretipousuario','descripcion')  
admin.site.register(TipoUsuario,TipoUsuarioadmin)

#Usuario admin
from core.models import Usuario
class Usuarioadmin(admin.ModelAdmin):
    list_display = ('id','idtipousuario','username','password')
admin.site.register(Usuario,Usuarioadmin)

#Industria Pyme
from core.models import IndustriaPyme
class IndustriaPymeadmin(admin.ModelAdmin):
    list_display = ('id','nombreindustria','descripcionindustria')
admin.site.register(IndustriaPyme,IndustriaPymeadmin)

#Pyme
from core.models import Pyme
class Pymeadmin(admin.ModelAdmin):
    list_display = ('id','nombrepyme','rutpyme','descripcion','comuna','email','telefono','whatsapp','telegram')
admin.site.register(Pyme,Pymeadmin)

#Categoria Demanda Oferta
from core.models import CategoriaDemandaOferta
class CategoriaDemandaOfertaadmin(admin.ModelAdmin):
    list_display = ('id','nombrecategoria','descripcion')
admin.site.register(CategoriaDemandaOferta,CategoriaDemandaOfertaadmin)

#Demanda Pyme
from core.models import DemandaPyme
class DemandaPymeadmin(admin.ModelAdmin):
    list_display = ('id_dp','idpymed','idcategoriademaandaoferta','demandapyme','descripcion_dp')
admin.site.register(DemandaPyme,DemandaPymeadmin)

#Oferta Pyme
from core.models import OfertaPyme
class OfertaPymeadmin(admin.ModelAdmin):
    list_display = ('id_op','idpymeo','idcategoriademandaoferta','ofertapyme','descripcion_op')
admin.site.register(OfertaPyme,OfertaPymeadmin)

from core.models import MatchOfertaDemanda
class MatchOfertaDemandaadmin(admin.ModelAdmin):
    list_display = ('idpymed','idcategoriademandaoferta','demandapyme','descripcion_dp','idpymeo','idcategoriademandaoferta','ofertapyme','descripcion_op')
admin.site.register(MatchOfertaDemanda,MatchOfertaDemandaadmin)