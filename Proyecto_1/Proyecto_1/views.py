from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Mundo!. Primera página con Django")

def despedida(request):
    return HttpResponse("Adios Mundo!. Fin de mi primera página con Django")

def getFecha(request):
    current_date = datetime.datetime.now()
    text = f"""
    <html>
        <body>
            <h1>
                Fecha y hora actuales: {current_date}
            </h1>
        </body>
    </html>
    """
    return HttpResponse(text)

def calculateAge(request, year):
    current_age = 24
    current_year = datetime.datetime.now().year
    timelapse = year - current_year
    future_age = current_age + timelapse
    documento = f"""
    <html>
        <body>
            <h2>
                En el año {year} tendrás {future_age} años
            </h2>
        </body>
    </html>
    """
    return HttpResponse(documento)

def calculateAge2(request,age, year):
    current_age = age
    current_year = datetime.datetime.now().year
    timelapse = year - current_year
    future_age = current_age + timelapse
    documento = f"""
    <html>
        <body>
            <h2>
                En el año {year} tendrás {future_age} años
            </h2>
        </body>
    </html>
    """
    return HttpResponse(documento)

def saludo2(request):
    doc_path = 'G:\My Drive\Sincronizacion\Programacion\Python\Djando_Course_Pildoras_Informaticas\Proyecto_1\Proyecto_1\Templates\saludoTemplate.html'
    with open(doc_path) as doc_externo:
        templ = Template(doc_externo.read())  
    ctx = Context()
    document = templ.render(ctx)
    return HttpResponse(document)