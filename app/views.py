from ensurepip import bootstrap
from django.shortcuts import redirect, render
from django.urls import is_valid_path
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
    



