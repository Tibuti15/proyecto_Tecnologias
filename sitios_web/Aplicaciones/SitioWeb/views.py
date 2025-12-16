from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SitioWeb, Tecnologias


# -------- SITIOS --------

def listado_sitios(request):
    sitios = SitioWeb.objects.all()
    return render(request, 'index.html', {'sitios': sitios})


def nuevo_sitio(request):
    tecnologias = Tecnologias.objects.all()
    return render(request, 'nuevoSitio.html', {'tecnologias': tecnologias})


def guardar_sitio(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        url = request.POST.get('url')
        creador = request.POST.get('creador') 
        tecnologia_id = request.POST.get('tecnologia')
        foto = request.FILES.get("foto")

        tecnologia = get_object_or_404(Tecnologias, id=tecnologia_id)

        SitioWeb.objects.create(
            nombre=nombre,
            url=url,
            creador=creador,
            tecnologias=tecnologia,
            foto=foto
        )
        messages.success(request, "Sitio web guardado correctamente!")
        return redirect('index')


def editar_sitio(request, id):
    sitio = get_object_or_404(SitioWeb, id=id)
    tecnologias = Tecnologias.objects.all()
    return render(request, 'editarSitio.html', {
        'sitio': sitio,
        'tecnologias': tecnologias
    })


def edicion_sitio(request):
    if request.method == "POST":
        id = request.POST['id']
        nombre = request.POST['nombre']
        url = request.POST['url']
        creador = request.POST['creador']
        tecnologia_id = request.POST['tecnologia']
        foto = request.FILES.get("foto")

        sitio = get_object_or_404(SitioWeb, id=id)

        sitio.nombre = nombre
        sitio.url = url
        sitio.creador = creador
        sitio.tecnologias = get_object_or_404(Tecnologias, id=tecnologia_id)

        if foto:
            sitio.foto = foto

        sitio.save()

        messages.success(request, "Sitio web actualizado correctamente!")
        return redirect('index')



def eliminar_sitio(request, id):
    sitio = get_object_or_404(SitioWeb, id=id)
    sitio.delete()
    messages.success(request, "Sitio web eliminado exitosamente!")
    return redirect('index')


# -------- TECNOLOGÍAS --------

def listado_tecnologias(request):
    tecnologias = Tecnologias.objects.all()
    return render(request, 'tecnologia.html', {'tecnologias': tecnologias})


def nueva_tecnologia(request):
    return render(request, 'nuevaTecnologia.html')


def guardar_tecnologia(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        foto = request.FILES.get('foto')

        Tecnologias.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            foto=foto
        )
        messages.success(request, "Tecnología guardada exitosamente!")
        return redirect('listado_tecnologias')


def editar_tecnologia(request, id):
    tecnologia = get_object_or_404(Tecnologias, id=id)
    return render(request, 'editarTecnologia.html', {'tecnologia': tecnologia})


def edicion_tecnologia(request):
    if request.method == "POST":
        id = request.POST['id']
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        foto = request.FILES.get('foto')

        tecnologia = get_object_or_404(Tecnologias, id=id)
        tecnologia.nombre = nombre
        tecnologia.descripcion = descripcion

        if foto:
            tecnologia.foto = foto

        tecnologia.save()
        messages.success(request, "Tecnología actualizada correctamente!")
        return redirect('listado_tecnologias')


 
def eliminar_tecnologia(request, id):
    tecnologia = get_object_or_404(Tecnologias, id=id)
    tecnologia.delete()
    messages.success(request, "Tecnología eliminada exitosamente!")
    return redirect('listado_tecnologias')
