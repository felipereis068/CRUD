from wsgiref.util import request_uri
from MySQLdb import DataError
from django.shortcuts import redirect, render
from app.forms import CarrosForm
from app.models import Carros


def home(request):
    data = {}
    data['crud'] = Carros.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['crud'] = Carros.objects.get(pk=pk)  
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['crud'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['crud'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['crud'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['crud'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    crud = Carros.objects.get(pk=pk)
    crud.delete()
    return redirect('home')
    



