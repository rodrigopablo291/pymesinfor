from multiprocessing.managers import BaseManager, ValueProxy

from django.views import View
from ast import keyword
from django.db import models
from importlib_metadata import pass_none
from zmq import proxy
from django.http import JsonResponse


# Create your models here.

#Tipo Usuario
class TipoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombretipousuario = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return '{} '.format(self.nombretipousuario)
    
    class Meta:
        verbose_name = "Tipo Usuario"
        verbose_name_plural = "Tipo Usuario"
        
#Usuario
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    idtipousuario = models.ForeignKey(TipoUsuario,to_field='id',on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return '{} '.format(self.idtipousuario)
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuario"

#Industria Pyme      
class IndustriaPyme(models.Model):
    id = models.AutoField(primary_key=True)
    nombreindustria = models.CharField(max_length=50)
    descripcionindustria = models.CharField(max_length=100)
    
    def __str__(self):
        return '{} '.format(self.nombreindustria)
    
    class Meta:
        verbose_name = "Industria Pyme"
        verbose_name_plural = "Industria Pyme"
#Pyme
class Pyme(models.Model):
    id = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey(Usuario,to_field='id',on_delete=models.CASCADE)
    idindustriapyme = models.ForeignKey(IndustriaPyme,to_field='id',on_delete=models.CASCADE)
    nombrepyme = models.CharField(max_length=50,null=True,unique=True)
    rutpyme = models.CharField(max_length=30) # LO DEJE CHAR POR SI QUIERE PONER PUNTO Y GUION
    descripcion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=30)
    email =  models.EmailField()
    telefono = models.IntegerField()
    whatsapp = models.CharField(max_length=15) #TAMBIEN CHAR POR SI QUIERE COLOCAR EL +
    telegram = models.CharField(max_length=20)
    
    def __str__(self):
        return '{} '.format(self.nombrepyme)
    
    class Meta:
        verbose_name = "Pyme"
        verbose_name_plural = "Pyme"

        
#Categoria Demanda Oferta
class CategoriaDemandaOferta(models.Model):
    id = models.AutoField(primary_key=True)
    nombrecategoria = models.CharField(max_length=30,null=True,unique=True) # de esta manera al migrar no me pedira ingresar un dato obligatoriamente, pero el unique me lo pide obligatoriamente cuando no es una clave foreanea
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
            return '{} {}'.format(self.id,self.nombrecategoria)
    
    class Meta:
        verbose_name = "Categoria Demanda Oferta"
        verbose_name_plural = "Categoria Demanda Oferta"
        
# ===================================================================

#Demanda Pyme
class DemandaPyme(models.Model):
    id_dp = models.AutoField(primary_key=True)
    idpymed = models.ForeignKey(Pyme,to_field='nombrepyme',on_delete=models.CASCADE,related_name='nombrespyme')
    idcategoriademaandaoferta = models.ForeignKey(CategoriaDemandaOferta,to_field='id',on_delete=models.CASCADE)
    demandapyme = models.ForeignKey(CategoriaDemandaOferta,to_field='nombrecategoria',on_delete=models.CASCADE,related_name='demandaspyme')
    descripcion_dp = models.CharField(max_length=100)
    
    def __str__(self):
            return '{} '.format(self.id_dp)
    
    class Meta:
        verbose_name = "Demanda Pyme"
        verbose_name_plural = "Demanda Pyme"

#Oferta Pyme

class OfertaPyme(models.Model):
    id_op = models.AutoField(primary_key=True)
    idpymeo = models.ForeignKey(Pyme,to_field='nombrepyme',on_delete=models.CASCADE,related_name='nombrespymee')
    idcategoriademandaoferta = models.ForeignKey(CategoriaDemandaOferta,to_field='id',on_delete=models.CASCADE)
    ofertapyme = models.ForeignKey(CategoriaDemandaOferta,to_field='nombrecategoria',on_delete=models.CASCADE,related_name='ofertaspyme')
    descripcion_op = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Oferta Pyme"
        verbose_name_plural = "Oferta Pyme"
      

#MatchOfertaDemanda      

class MatchOfertaDemanda(DemandaPyme, OfertaPyme):
    class Meta:
        verbose_name = "Match Oferta Demanda"
        verbose_name_plural = "Match Oferta Demanda"
    pass

'''
  k = DemandaPyme.demandapyme
    o = OfertaPyme.ofertapyme
    if k == o:
        object = BaseManager
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''