from django.shortcuts import render, redirect
from . import models
# Create your views here.

def home(request):
    context = {
        'carros' : models.Carro.objects.all(),
        'fabricantes' : models.Fabricante.objects.all(),
    }
    return render(request,'index.html',context)

def carros(request):
    context = {
        'carros' : models.Carro.objects.all(),
        'fabricantes' : models.Fabricante.objects.all(),
    }
    if request.method == 'GET':
        if 'id' in request.GET:
            context['carro'] = models.Carro.objects.get(id=request.GET['id'])
    if request.method == 'POST':
        fabricante = models.Fabricante.objects.get(id=request.POST['fabricante'])
        novo_carro = models.Carro(placa=request.POST['placa'], modelo=request.POST['modelo'], fabricante=fabricante)
        novo_carro.save()
    return render(request,'newcar.html',context)
    
def deleteCarro(request):
    if request.method == 'GET':
        carro = models.Carro.objects.get(id=request.GET['id'])
        carro.delete()
    return redirect('../')

def fabricantes(request):
    context = {
        'carros' : models.Carro.objects.all(),
        'fabricantes' : models.Fabricante.objects.all(),
    }
    if request.method == 'POST':
        novo_fabricante = models.Fabricante(nome=request.POST['nome'])
        novo_fabricante.save()
    return render(request,'newfabricante.html',context)
    
def deleteFabricante(request):
    if request.method == 'GET':
        fabricante = models.Fabricante.objects.get(id=request.GET['id'])
        fabricante.delete()
    return redirect('../')
    