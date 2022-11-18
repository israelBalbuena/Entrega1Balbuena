from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "appfinancial/base.html")

def crypto(request):
    return render(request, "appfinancial/cripto.html")

def raices(request):
    return render(request, "appfinancial/raices.html")

def activos(request):
    return render(request, "appfinancial/activos.html")
