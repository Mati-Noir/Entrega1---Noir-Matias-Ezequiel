from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Curso, Estudiante, Profesor
from mi_app.forms import CursoFormulario, CursoBusquedaFormulario, ProfesorFormulario, EstudianteFormulario

# --------- Sector de la pagina web. --------- #


def mostrar_index(request):
    return render(request, "mi_app/index.html", {"mi_titulo": "Bienvenido, suscribase para recibir notificaciones sobre la actualidad antes que nadie."})


# --------- Sector de las listas de las diferentes clases de los models. --------- #


def listar_cursos(request): # vista
    context = {}
    context["cursos"] = Curso.objects.all() # modelo
    return render(request, "mi_app/lista_cursos.html", context) # template


def listar_estudiantes(request):
    context = {}
    context["estudiantes"] = Estudiante.objects.all()
    return render(request, "mi_app/lista_estudiantes.html", context)

def listar_profesores(request):
    context = {}
    context["profesores"] = Profesor.objects.all()
    return render(request, "mi_app/lista_profesores.html", context)


# --------- Sector de las formularios. --------- #


def formulario_curso(request):

    if request.method == "POST":
        
        mi_formulario = CursoFormulario(request.POST)

        print(mi_formulario)

        if  mi_formulario.is_valid():

            datos = mi_formulario.cleaned_data 

            curso = Curso(nombre=datos["curso"], camada=datos["camada"])

            curso.save()

            return render(request, "mi_app/gracias.html", {"mensaje":"agregado con exito!"})
   
    else:

        mi_formulario = CursoFormulario()
    
    return render(request, "mi_app/curso_formulario.html", {"mi_formulario":mi_formulario})


def profesor_formulario(request):

    if request.method == "POST":
        
        mi_formulario_profesor = ProfesorFormulario(request.POST)

        print(mi_formulario_profesor)

        if  mi_formulario_profesor.is_valid():

            data = mi_formulario_profesor.cleaned_data 

            profe = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"],)

            profe.save()

            return render(request, "mi_app/gracias.html")
   
    else:

        mi_formulario_profesor = ProfesorFormulario()
    
    return render(request, "mi_app/Profesor_Formulario.html", {"mi_formulario_profesor":mi_formulario_profesor})




def estudiante_formulario(request):

    if request.method == "POST":
        
        mi_formulario_estudiante = EstudianteFormulario(request.POST)

        print(mi_formulario_estudiante)

        if  mi_formulario_estudiante.is_valid():

            dato = mi_formulario_estudiante.cleaned_data 

            alumno = Estudiante(Nombre=dato["Nombre"], Apellido=dato["Apellido"], Email=dato["Email"],)

            alumno.save()

            return render(request, "mi_app/gracias.html")
   
    else:

        mi_formulario_estudiante = EstudianteFormulario()
    
    return render(request, "mi_app/Estudiante_formulario.html", {"mi_formulario_estudiante":mi_formulario_estudiante})



# --------- Sector de las busquedas de formularios. --------- #

def formulario_busqueda(request):

    busqueda_formulario = CursoBusquedaFormulario()

    if request.GET:    
        busqueda_formulario = CursoBusquedaFormulario(request.GET)
        if busqueda_formulario.is_valid():
            cursos = Curso.objects.filter(nombre=busqueda_formulario.cleaned_data.get("criterio")).all()
            return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario, "cursos": cursos})


    return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario})



def contacto(request):

    if request.method == "POST":
        
        return render(request, "mi_app/gracias.html")

    return render(request,"mi_app/contacto.html")


def busqueda_productos(request):

    return render(request, "mi_app/busqueda_productos.html")





