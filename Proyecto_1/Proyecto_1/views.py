from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Mundo!. Primera página con Django")

def despedida(request):
    return HttpResponse("Adios Mundo!. Fin de mi primera página con Django")