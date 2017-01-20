from django.shortcuts import render
from .models import Cadeira,Tema,Curso

def index(request):
    return render(request, 'home/home.html')

def Cursos(request):
    cursos_data= Curso.objects.all()
    return render(request,'home/cursos.html',{'cursos':cursos_data})

def CadeirasCurso(request,pk):
    cadeirasData = Cadeira.objects.all().filter(Curso=pk)
    return render(request, 'home/temas.html', {'cadeiras': cadeirasData})

def TemasCurso(request,pk):
    cadeirasData = Cadeira.objects.all().filter(Cadeira=pk)
    return render(request,'home/temas.html',{'temas':cadeirasData})
