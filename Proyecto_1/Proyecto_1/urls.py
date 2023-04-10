"""Proyecto_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto_1.views import saludo, herencia1_Template, herencia2_Template, saludo_Shortcut, saludo_Template, saludo_Template_Variable, saludo_Loader, despedida, getFecha, calculateAge, calculateAge2, lista_Ejemplos, plantilla_Incrustada

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('hastaluego/', despedida),
    path('fecha/', getFecha),
    path('edades/<int:year>', calculateAge),
    path('edades/<int:age>/<int:year>', calculateAge2),
    path('saludo_template/', saludo_Template),
    path('saludo_template_variable/', saludo_Template_Variable),
    path('lista_ejemplos/', lista_Ejemplos),
    path('saludo_loader/', saludo_Loader),
    path('saludo_shortcut/', saludo_Shortcut),
    path('plantilla_incrustada/', plantilla_Incrustada),
    path('herencia1_template/', herencia1_Template),
    path('herencia2_template/', herencia2_Template),
]
