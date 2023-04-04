# DJANGO FRAMEWORK 
## Índice

1. [Introducción](#introducción)
2. [Primer Proyecto](#primer-proyecto)
3. [Primera Página](#primera-página)
4. [Parámetros en URL](#páginas-dinámicas-y-parámetros-en-url)

***

## INTRODUCCIÓN
### ¿Qué es Django? 
Django es un **Framework** (un marco de trabajo formado por un conjunto de herramientas, librerías y buenas prácticas) web gratuito de código abierto escrito en Python.

Algunos Frameworks en un patron denominado **MVC** (Modelo Vista Controlador) que consiste dividir cualquier aplicacion web en tres grandes modulos:
- Modelo
- Vista
- Controlador

El *Modelo* es el que se encarga de obtener la información, normalmente de una base de datos.
La *Vista* es el encargado de mostrar la información al usuario (lo que el usuario ve y con lo que interactua).
El *Controlador* se encarga de gestionar todas las comunicaciones existentes entre la vista y el modelo.

El proceso en un modelo MVC sería:
Un usuario hace una peticion en una pagina web, la vista. El controlador recibe la petición y demanda datos al modelo, el modelo devuelve los datos pedidos al controlador, que se los da a la vista para que los enseñe al usuario.

Django no se basa exactamente en **MVC** si no en **MTV** (Model Template View), que lo que hace es sustituir las vistas por Templates, el controlador es el view y el Model sigue siendo el Model

***
## PRIMER PROYECTO

No es necesario que la carpeta la creemos en las raiz del servidor. Podemos crearla donde queramos.
Para empezar nuestro proyecto, abrimos una terminal CMD y nos dirigimos a la carpeta donde vayamos a guardar nuestro proyecto. En la terminal escribimos el comando

```
django-admin startproject NombreSubCarpeta
```    
    
Este comando crea una Subcarpeta con todo lo necesario para empezar el proyecto.
- Un archivo *Manage.py* que es una utilidad de lineas de comandos que nos permite interactuar con nuestros proyectos django. (Si en la terminal por ejemplo ejecutamos *python manage.py help* nos dara un listado de opciones y ayuda).

- Una subcarpeta con el mismo nombre del proyecto que contiene otros archivos muy importantes:
    - \_init\_.py: Permite que python trate al directorio como un paquete
    - settings.py: Contiene todas las configuraciones de nuestro proyecto de Django
    - urls.py: Donde se almacenan las urls que usaremos en nuestro proyecto
    - wsgi.py: Relativo al servidor web donde vamos a usar nuestro proyecto de Django
    
    
### Inicio de la base de datos
Para empezar nuestro proyecto, vamos a necesitar tener una base de datos a la que se conecten las apps que estan en el archivo settings.py. En este proyecto, vamos a empezar usando una base de datos SQLlite3, que viene instalada por defecto con Django y no hace falta configurar cosas adicionales.

¿Cómo creamos la base de datos para que estas aplicaciones hagan uso de esos datos? En el directorio de nuestro proyecto ejecutamos el siguiente comando:

```
python manage.py migrate
```

Esto creaara en nuestra carpeta un nuevo archivo llamado *db.sqlite3* que será nuestra base de datos. Con esto nuestro proyecto ya estaría en funcionamiento. Para comprobarlo, tenemos que ejecutar el servidor, y una vez que este listo, vamos en un navegador a la dirección correspondiente y deberiamos ver la pagina bienvenida de Django

    
A lo largo iremos usando diferentes servidores de prueba. Django viene ya con un servidor para poder hacer pruebas muy ligero que no es recomendable para proyectos serios porque es un servidor que no admite multiples peticiones simultaneas, no admite cargas de trabajo pesada... Solo sirve para hacer pequeños proyectos y ver si se ven.

Para ejecutar este servidor de testeo debemos ejecutar el siguienet comando
```
python manage.py runserver
```
    
Si todo va bien, en la terminal deberiamos ver una linea que ponga *Starting development server*, que nos indica que ya hemos arrancado el servidor de desarrollo en la direccion que nos indica. En mi caso, es _http://127.0.0.1:8000/_, y al abrir esa URL en un navegador debemos ver la pagina de Django diciendo que la instalación ha funcionado

***
## PRIMERA PÁGINA

Vamos a crear nuestra primera pagina. Para ello vamos a tener que crear nuestra primera vista y configurar la URL. Por ahora no nos vamos a conectar a ninguna base de datos, asi que del MTV vamos a olvidarnos del Model. Y tampoco vamos a elaborar ningún template con interfaces o formularios para el usuario. Solo vamos a crear una view para hacer peticiones al servidor. 

Para hacer la petición, Django va a trabajar con dos objetos fundamentales:
Para hacer la petición trabajaremos con objetos de la clase **HttpRequest**, y para manejar la respuesta vamos a trabajar con objetos de la clase **HttpResponse**.

Para empezar rearemos un archivo nuevo que correspondera a las vistas que vayamos almacenando. Por convenio, el nombre que suele tener este archivo es ``view.py``.

### Creación de la vista
El primer paso para trabajar con las peticiones es importar el modulo ***django.http*** donde se definen los objetos de **HttpResponse** y **HttpRequest**
```
from django.http import HttpResponse
```
Para crear una vista lo que tenemos que hacer es crear una función python. A cada función dentro del archivo View se le denomina **vista** Vamos a crear una función que nos enseñe una pagina básica que ponga "Hola Mundo!". La vista que vamos a crear es la siguiente.

```
def saludo(request):
    return HttpResponse("Hola Mundo!. Primera página con Django")
```

En una vista, lo importante es lo que va a recibir por parametro. Para hacer la petición, la vista recibe un *Request* como primer argumento. 
Después de crear la vista, debemos de decirle a Python la URL que tenemos que introducir en el navegador para poder ver esa vista.

Para enlazar esta vista con el URL para poder ver el texto, tenemos que hacerlo en el archivo ``urls.py``. Podemos observar que hay una lista *urlpatterns*, que es donde almacenamos las urls. Enotnces lo que haremos es, siguiendo la misma nomenclatura, usamos el path y la URL que queremos enlazar con la vista. La lista *urlpatterns* quedaria entonces de la siguiente forma:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
]
```

Creamos un path con la url que queremos entre comillas, y como segundo parametro la vista que queremos enlazarle. El nombre de la URL no tiene porque ser el mismo que el de la vista. Lo hacemos asi solo para facilitarnos el trabajo. Como en este caso, nuestra función *saludo* está en otro archivo, tendremos que importarla. Para ello simplemente añadimos ``from Proyecto_1.views import saludo
`` donde los demas importas.

 Ya simplemente debemos probar que todo funciona bien. Para ello primero arrancamos el servidor (desde el cmd, ejecutar el comando *runserver* desde el archivo ``manage.py``). Una vez arrancado el server, simplemente vamos al navegador y abrimos nuestra Url base con el nuevo path al final que creamos:  http://127.0.0.1:8000/saludo/

 Acabamos de crear nuestra primera página web con Django. Ahora podemos crear más vistas y URLs para 

 En el archivo ``view.py`` vamos a crear otra función para despedirnos.  

``` 
def despedida(request):
    return HttpResponse("Adios Mundo!. Fin de mi primera página con Django")
```

No olvidemos añadir una nueva URL con la que enlazar nuestra nueva vista. Añadimos a *urlpatterns* el siguiente path: ``path('hastaluego/', despedida)``

***

## PÁGINAS DINÁMICAS Y PARÁMETROS EN URL

En esta sección veremos como trabajar con contenido dinámico y pasar parámetros con Django a una URL. Hasta ahora solo hemos usado contenido estático (mostrar mensajes de texto), pero ahora veremos como trabajar de forma dinámica. Para ello vamos a crear un ejemplo que nos muestre la hora y fecha actuales. Dependiendo de cuando se ejecute, tomára la fecha y hora del servidor y la mostrará en pantalla.

Empezaremos creando una nueva vista con el siguiente codigo:
```
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
```

En esta vista hemos cogido la función ``now`` del modulo datetime que previamente hemos importado, y la hemos añadido en el texto que vamos a mostrar en la página. En este caso, hemos escrito un HTML como el texto para que veamos que sigue funcionando y asi podemos ponerle más customizaciones como el tamaño del párrafo. Ahora simplemente creamos un path con la URL que queramos y simplemente probamos. En mi caso, añadiré ``path('fecha/', getFecha)`` a mi *urlpatterns*


Ahora veremos cómo pasarle parámetros a la URL. Para ello vamos a construir una vista que nos diga qué edad tendremos en un año futuro. Crearemos la siguiente vista que nos calcule la edad futura:
```
def calculateAge(request, year):
    current_age = 24
    current_year = datetime.datetime.now().year
    time_period = year - current_year
    future_age = current_age + time_period
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
```

Esta vez, aparte del parámetro *request* de la vista, le hemos añadido un segundo parametro a la función, *year*, que será el año en el que queramos calcular nuestra edad.

Vamos a enlazar esta vista con una URL que nos permita añadir un parámetro. El path que añadiremos a *urlpatterns* es el siguiente: ``path('edades/<int:year>', calculateAge)``. Para pasar un parámetro a un URL tenemos que escribirlo entre los simbolos ``< >``- En este caso, como el URL toma todo lo que está entre comillas como texto, y nuestro year es un numero con el que queremos hacer operaciones maetmáticas, tenemos que indicarle a Django que el parámetro que le vamos a pasar es un numero. Para ello, antes del nombre de la variable de la función escribimos ``int:``. Ya solo queda comprobar que funciona navegando a la URL con el parámatro: http://127.0.0.1:8000/edades/2070

Ahora mismo, nuestra edad la tenemos de forma estática. Vamos a ver cómo podemos pasar más de un parámetro a una URL para poder poner nuestra edad actual y en que año queremos saberla. Para ello vamos a modificar la vista anterior (o crear otra distinta). La vista seria:

```
def calculateAge(request,age,  year):
    current_age = age
    current_year = datetime.datetime.now().year
    time_period = year - current_year
    future_age = current_age + time_period
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
```

En nuestra URL, simplemente tenemos que añadir el parámetro nuevo de la misma forma que si tuvieramos uno. El path quedaría de la forma ``path('edades/<int:age>/<int:year>', calculateAge)``.
La nueva URL sería de la forma http://127.0.0.1:8000/edades/24/2070
***

## Templates

### ¿Qúe son?
Las **Templates**, o plantillas, son básicamente cadenas de texto que pueden contener codigo HTML. Sirven para separar la parte lógica de la parte visual de un documento web. Hasta ahora habiamos incrustado nuestro código HTML en las vistas, pero esto no debería hacerse. Hay muchas formas de usar las templates. La más normal es guardar la cadena de texto (el documento HTML) en un documento o fichero independiente y despues simplemente cargar ese fichero en la vista.

### ¿Cómo se usan las plantillas?
El proceso básico para usar una plantilla consta de 3 pasos:
1. Crear un objeto de tipo Template que lea ese documento donde guardamos nuestra cadena de texto externa de HTML. La Template se crea de la siguiente forma: 
``plt = Template(doc_externo.read())`` 
2. Crear un **contexto**. El contexto son los datos adicionales que puede llegar a utilizar la template. Por ejemplo, si queremos añadir contenido dinámico al HTML (como los parámetros en el ejemplo anterior), estos iran almacenados dentro del contexto. El contexto siempre tendremos que crearlo, aunque esté vacío. El contexto se escribe de la forma 
``ctx = Context()``
3. Renderizar el objeto Template que hemos creado en el paso 1. Para ello solo usaremos la función render y le pasaremos el contexto como argumento, esté o no vacío. 
``documento = plt.render(ctx)``

### Ejemplo 1
Vamos a recrear la URL de saludo que creamos en la sección [Primera Página](#primera-página) con una Template. Para ello vamos a crear una plantilla con un código HTML, cargaremos la plantilla en la vista `saludo`, crearemos un contexto y renderizaremos la plantilla.

Como primer paso vamos a crear una carpeta *Templates* en nuestro directorio donde almacenar las plantillas, y dentro creamos un archivo HTML, donde copiaremos el código de nuestra función saludo. Dentro crearemos nuestro fichero HTML al que llamaremos ``saludoTemplate.html``

```
<html>
  <body>
    <h1>
      Hola Mundo! Primera pagina con una Template con Django
    </h1>
  </body>
</html>
```

Ahora tenemos que abrir este documento en nuestro vista y crear una template que lo lea. El código de la función queda de la siguiente forma: 

```
def saludo(request):
    doc_path = 'path of the html file'
    with open(doc_path) as doc_externo:
        templ = Template(doc_externo.read())  
    ctx = Context()
    document = templ.render(ctx)
    return HttpResponse(document)
```

En esta función hemos abierto nuestro documento HTML con el operador *with* y la función *open*, indicando el path del archivo en la variable *doc_path*. Hemos creado un archivo Template, un contexto vacío y renderizado la template con dicho contexto. Por último simplemente devolver el render de la template como Response de la vista.