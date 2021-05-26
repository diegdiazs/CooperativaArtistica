from django.shortcuts import render

def home(request):
    return render(request,'galeria/index.html')

def contacto(request):
    return render(request,'galeria/contacto.html')

def exposiciones(request):
    return render(request,'galeria/exposiciones.html')

def fotografia(request):
    return render(request,'galeria/fotografia.html')

def iniciosesion(request):
    return render(request,'galeria/iniciosesion.html')

def registro(request):
    return render(request,'galeria/registro.html')
