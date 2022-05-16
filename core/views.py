

from calendar import c
from difflib import Match
import json
from multiprocessing import Condition, context
from re import A
from django.shortcuts import render
from numpy import empty
from pyparsing import java_style_comment
from core.forms import LoginForm

from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import DemandaPyme, MatchOfertaDemanda,OfertaPyme
from django.http import JsonResponse

from ast import keyword


from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'core/index.html', {})

def login_ingresar(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Te has identificado de modo correcto"
                    return render(request,'core/django_administrador.html', {'message': message, 'form':form})
                    #return render(request,'core/index.html', {'message': message, 'form':form})
                else:
                    message = "Tu usuario esta inactivo"
            else:
                message = "nombre de usuario y/o password incorrecto"
    else:
        form = LoginForm()
    return render(request,'core/login_ingresar.html', {'message': message, 'form':form})


class MatchListView(View):
    api = keyword
    def get(self, request):
        ulist = MatchOfertaDemanda.objects.all()
        return JsonResponse(list(ulist.values('idpymed','demandapyme','idpymeo','ofertapyme')),safe=False)
        
        
class OfertaPymeListView(View):
    api = keyword
    def get(self, request):
        ulist = OfertaPyme.objects.all()
        return JsonResponse(list(ulist.values()), safe=False)
'''
for i en OfertaPyme 
  for j en DemandaPyme
         ofertapyme[i[ == demandapyme [j]
        add    MatchOfertaDemanda 

for i in OfertaPyme.ofertapyme:
            for j in DemandaPyme.demandapyme:
                if j == i :
                    ulist = MatchOfertaDemanda.objects.exclude().select_related('ofertapyme','demandapyme')
                    return JsonResponse(list(ulist.values('idpymed','demandapyme','idpymeo','ofertapyme')),safe=False)
  
  
  
  
 ulist = MatchOfertaDemanda.objects.all()
        for i in MatchOfertaDemanda.demandapyme:
            for j in MatchOfertaDemanda.ofertapyme:
                if j == i:
                    ulist = MatchOfertaDemanda.objects.all()
                    return False
            else:
                ulist = MatchOfertaDemanda.objects.all()
                return JsonResponse(list(ulist.values('idpymed','demandapyme','idpymeo','ofertapyme')),safe=False)      

for i in MatchOfertaDemanda.demandapyme:
            for j in MatchOfertaDemanda.ofertapyme:
                loson = []
                iguales = '{} {}'.format(i,j)
                loson.append(iguales)
                if j == i:
                    return JsonResponse(list(ulist.values('idpymed','demandapyme','idpymeo','ofertapyme')),safe=False)






'''
















