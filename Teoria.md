# DJANGO FRAMEWORK 
## Índice

1. [Introducción](#introducción)
2. [Primer Proyecto](#primer-proyecto)
3. [Primera Página](#primera-página)
4. [Parámetros en URL](#páginas-dinámicas-y-parámetros-en-url)
5. [Templates](#templates)
5. [Bases de Datps](#bases-de-datos)

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
<br>

    
Este comando crea una Subcarpeta con todo lo necesario para empezar el proyecto.
- Un archivo *Manage.py* que es una utilidad de lineas de comandos que nos permite interactuar con nuestros proyectos django. (Si en la terminal por ejemplo ejecutamos *python manage.py help* nos dara un listado de opciones y ayuda).

- Una subcarpeta con el mismo nombre del proyecto que contiene otros archivos muy importantes:
    - \_init\_.py: Permite que python trate al directorio como un paquete
    - settings.py: Contiene todas las configuraciones de nuestro proyecto de Django
    - urls.py: Donde se almacenan las urls que usaremos en nuestro proyecto
    - wsgi.py: Relativo al servidor web donde vamos a usar nuestro proyecto de Django
<br>

    
### Inicio de la base de datos
Para empezar nuestro proyecto, vamos a necesitar tener una base de datos a la que se conecten las apps que estan en el archivo settings.py. En este proyecto, vamos a empezar usando una base de datos SQLlite3, que viene instalada por defecto con Django y no hace falta configurar cosas adicionales.

¿Cómo creamos la base de datos para que estas aplicaciones hagan uso de esos datos? En el directorio de nuestro proyecto ejecutamos el siguiente comando:

```
python manage.py migrate
```
<br>

Esto creaara en nuestra carpeta un nuevo archivo llamado *db.sqlite3* que será nuestra base de datos. Con esto nuestro proyecto ya estaría en funcionamiento. Para comprobarlo, tenemos que ejecutar el servidor, y una vez que este listo, vamos en un navegador a la dirección correspondiente y deberiamos ver la pagina bienvenida de Django

    
A lo largo iremos usando diferentes servidores de prueba. Django viene ya con un servidor para poder hacer pruebas muy ligero que no es recomendable para proyectos serios porque es un servidor que no admite multiples peticiones simultaneas, no admite cargas de trabajo pesada... Solo sirve para hacer pequeños proyectos y ver si se ven.

Para ejecutar este servidor de testeo debemos ejecutar el siguienet comando
```
python manage.py runserver
```
<br>

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
<br>

Para crear una vista lo que tenemos que hacer es crear una función python. A cada función dentro del archivo View se le denomina **vista** Vamos a crear una función que nos enseñe una pagina básica que ponga "Hola Mundo!". La vista que vamos a crear es la siguiente.

```
def saludo(request):
    return HttpResponse("Hola Mundo!. Primera página con Django")
```
<br>

En una vista, lo importante es lo que va a recibir por parametro. Para hacer la petición, la vista recibe un *Request* como primer argumento. 
Después de crear la vista, debemos de decirle a Python la URL que tenemos que introducir en el navegador para poder ver esa vista.

Para enlazar esta vista con el URL para poder ver el texto, tenemos que hacerlo en el archivo ``urls.py``. Podemos observar que hay una lista *urlpatterns*, que es donde almacenamos las urls. Enotnces lo que haremos es, siguiendo la misma nomenclatura, usamos el path y la URL que queremos enlazar con la vista. La lista *urlpatterns* quedaria entonces de la siguiente forma:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
]
```
<br>

Creamos un path con la url que queremos entre comillas, y como segundo parametro la vista que queremos enlazarle. El nombre de la URL no tiene porque ser el mismo que el de la vista. Lo hacemos asi solo para facilitarnos el trabajo. Como en este caso, nuestra función *saludo* está en otro archivo, tendremos que importarla. Para ello simplemente añadimos ``from Proyecto_1.views import saludo
`` donde los demas importas.

 Ya simplemente debemos probar que todo funciona bien. Para ello primero arrancamos el servidor (desde el cmd, ejecutar el comando *runserver* desde el archivo ``manage.py``). Una vez arrancado el server, simplemente vamos al navegador y abrimos nuestra Url base con el nuevo path al final que creamos:  http://127.0.0.1:8000/saludo/

 Acabamos de crear nuestra primera página web con Django. Ahora podemos crear más vistas y URLs para 

 En el archivo ``view.py`` vamos a crear otra función para despedirnos.  

``` 
def despedida(request):
    return HttpResponse("Adios Mundo!. Fin de mi primera página con Django")
```
<br>

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
<br>

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
<br>

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
<br>

En nuestra URL, simplemente tenemos que añadir el parámetro nuevo de la misma forma que si tuvieramos uno. El path quedaría de la forma ``path('edades/<int:age>/<int:year>', calculateAge)``.
La nueva URL sería de la forma http://127.0.0.1:8000/edades/24/2070
***

## Templates

### ¿Qúe son?
Las **Templates**, o plantillas, son básicamente cadenas de texto que pueden contener codigo HTML. Sirven para separar la parte lógica de la parte visual de un documento web. Hasta ahora habiamos incrustado nuestro código HTML en las vistas, pero esto no debería hacerse. Hay muchas formas de usar las templates. La más normal es guardar la cadena de texto (el documento HTML) en un documento o fichero independiente y despues simplemente cargar ese fichero en la vista.
<br>

### ¿Cómo se usan las plantillas?
El proceso básico para usar una plantilla consta de 3 pasos:
1. Crear un objeto de tipo Template que lea ese documento donde guardamos nuestra cadena de texto externa de HTML. La Template se crea de la siguiente forma: 
``plt = Template(doc_externo.read())`` 
2. Crear un **contexto**. El contexto son los datos adicionales que puede llegar a utilizar la template. Por ejemplo, si queremos añadir contenido dinámico al HTML (como los parámetros en el ejemplo anterior), estos iran almacenados dentro del contexto. El contexto siempre tendremos que crearlo, aunque esté vacío. El contexto se escribe de la forma 
``ctx = Context()``
3. Renderizar el objeto Template que hemos creado en el paso 1. Para ello solo usaremos la función render y le pasaremos el contexto como argumento, esté o no vacío. 
``documento = plt.render(ctx)``

### Ejemplo 1
Vamos a recrear la URL de saludo que creamos en la sección [Primera Página](#primera-página) con una Template. Para ello vamos a crear una plantilla con un código HTML, cargaremos la plantilla en una nueva vista `saludo_Template`, crearemos un contexto y renderizaremos la plantilla.

Como primer paso vamos a crear una carpeta *Templates* en nuestro directorio donde almacenar las plantillas, y dentro creamos un archivo HTML, donde copiaremos el código de nuestra función saludo. Dentro crearemos nuestro fichero HTML al que llamaremos ``saludo_Template.html``

```
<html>
  <body>
      <h1 style="color: red";>
          Hola Mundo! Primera pagina con una Template con Django
      </h1>
  </body>
</html>
``` 
<br>

Ahora tenemos que abrir este documento en nuestro vista y crear una template que lo lea. El código de la función queda de la siguiente forma: 

```
def saludo(request):
    doc_path = 'path of the template file'
    with open(doc_path) as doc_externo:
        templ = Template(doc_externo.read())  
    ctx = Context()
    document = templ.render(ctx)
    return HttpResponse(document)
```

<br>

En esta función hemos abierto nuestro documento HTML con el operador *with* y la función *open*, indicando el path del archivo en la variable *doc_path*. Hemos creado un archivo Template, un contexto vacío y renderizado la template con dicho contexto. Por último simplemente devolver el render de la template como Response de la vista.  Podemos ver con el URL que hemos enlazado a la vista, http://127.0.0.1:8000/saludo_template, que funciona perfectamente la plantilla.

### Variables y Propiedadess

Vamos a ver cómo usar variables en plantillas y como acceder a objetos y propiedades desde las plantillas. Para usar las variables de Python que creamos en las vistas en nuestras plantillas, vamos a utilizar el contexto. 

Cuando creamos un contexto, podemos pasarle como argumento un diccionario para que la plantilla pueda acceder a la información guardada dentro. Puede ser algo tan simple como una variable o cadena de texto o tan complejo como un objeto. Si en algun momento le pasamos un objeto en una variable, podemos acceder a las propiedades de las variables desde la template con la notacion del punto. Lo mismo pasaría con instancias de clases que crearamos.

 Vamos a crear una nueva vista igual que la anterior, pero con una variable, y vamos a crear otra plantilla donde usemos dicha variable. En el archivo view añadimos la siguiente función:

```
def saludo_Template_Variable(request):
    nombre = "Gon"
    apellido = "Estrada"
    doc_path = 'path of the template file'
    with open(doc_path) as doc_externo:
        templ = Template(doc_externo.read())  
    ctx = Context({"nombre_persona":nombre, "apellido":apellido, "fecha":fecha})
    document = templ.render(ctx)
    return HttpResponse(document)
```
<br>

Creamos una plantilla donde vayamos a usar las variables que tengamos, como *nombre_persona* y *apellido*. Para usar una variable en una template simplemente ponemos el nombre de la key del diccionario del context entre doble llave, es decir, {{key}}. La template quedaría de la siguiente forma:
```
<html>
  <body>
    <h1 style="color: red";>
      Hola Mundo! Primera pagina con una Template con Django
    </h1>
    <p>
      El nombre de la persona es {{nombre_persona}} {{apellido}}
    </p>
    <p>
      La fecha actual es {{fecha.date}}
    </p>
  </body>
</html>
```

Abrimos el URl que hayamos enlazado con la view, http://127.0.0.1:8000/saludo_template_variable/, y podremos ver que efectivamente, aparece el valor de las variables en la página web.


### Uso de listas y condicionales

Vamos a ver como usar métodos y listas en el contexto. Para agregarla a nuestra plantilla, simplemente añadimos en el diccionario del contexto la lista con una key. Para acceder al elemento que queramos de la lista, usamos la notación del punto y el índice del elemento al que queremos acceder de nuestra liasta.

Por ejemplo, vamos a crear una nueva view `lista_Ejemplos` que llame a una nueva plantilla, `lista_Ejemplos_Template.html`. Podemos coger cualquier vista anterior y simplemente añadirle el siguiente contexto: 
```
ctx = Context({"lista_nombres":["Jose", "Raul", "Pedro", "Juan", "Ramón"]})
```
<br>

En nuestra plantilla pondremos lo siguiente:

```
<html>
  <body>
    <h1>
        Ejemplo de listas en Django:
    </h1>
    <p> 
        El primer elemento de la lista {{lista_nombres}} es {{lista_nombres.0}} 
    </p>
  </body>
</html>
```

En caso de que quisieramos recorrer los elementos de una lista, como con un bucle for o while, podemos poner bucles en nuestras plantillas HTML. Para poner un bucle for en una plantilla, la sixtaxis es de la siguiente forma:

```
<p>
    {% for elem in lista_nombres %}
        {{elem}}
    {% endfor %}
</p>
```
La forma en la que queda la página puede no ser lo que queramos. Si ya queremos darle estilo o formato a los elementos de la lista, ya sería como un HTML normal. Podriamos crear parrafos que engloben los elementos con la etiqueta `<p>` o crear listas ordenadas o desordenadas con `<ul>`.
La template para ver todos los casos quedaria asi:

```
<html>
  <body>
    <h1>
        Ejemplo de listas en Django:
    </h1>
    <p> 
        El primer elemento de la lista {{lista_nombres}} es {{lista_nombres.0}} 
    </p>
    <p>
        {%if lista_nombres %}
          {% for elem in lista_nombres %}
              {{elem}}
          {% endfor %}
        {% else %}
          No hay elementos que  mostrar
        {% endif %}
    </p>
    <p>
      {% for elem in lista_nombres %}
          <p>{{elem}}</p>
      {% endfor %}
    </p>
    <ul>
      {% for elem in lista_nombres %}
          <li>{{elem}}</li>
      {% endfor %}
    </ul>
  </body>
</html>
``` 

Podemos ver el resultado con el siguiente enlace que hemos añadido al archivo de las URLs http://127.0.0.1:8000/lista_ejemplos/

También podemos añadir condicionales en nuestras templates, como para comprobar si una lista está vacía o no. Para añadir un if, la sintaxis es igual que la del bucle for.

``` 
{%if lista_nombres %}
  {% for elem in lista_nombres %}
    {{elem}}
  {% endfor %}
{% else %}
  No hay elementos que  mostrar
{% endif %}
```
Lo que hace este if es verificar si la variable *lista_nombres* existe y tiene información. Si ambas se cumple, entra en el if, si alguna de las dos condiciones falla, entra al else. Tambien podemos hacer comperaciones con los símbolos >, < o == en la plantilla. Por ejemplo 
``{%if lista_nombres.1 == 'Raul` %}``
Para añadir comentarios a una plantilla (no será visible en la página web, solo en el código), podemos hacerlo en una sola línea con la siguiente sintaxis: ``{#Comentario de una sola línea} ``, o si queremos que sea más de una linea, abriendo y cerrando una etiqueta *comment* 
```
{% comment %}
Comentario múltiples lineas
{% endcomment %}
```
<br>

### Filtros
Escribir un filtro es como escribir métodos con la nomenclatura del punto. Por ejemplo, si queremos escibir las palabras de la lista en mayúscula podríamos hacer `lista_nombres.upper`, que sería llamar al método *upper*; o `lista_nombres|upper`, que sería llamando el filtro. Para saber más sobre filtros puedes mirar sobre ellos en la documentación de Django, https://docs.djangoproject.com/en/4.2/ref/templates/builtins/. Una gran ventaja que también presentan es que los filtros pueden ir encandenandose unos con otros. Por ejemplo `lista_nombres|first|upper`me dará la primera letra de cada elemento de la lista en mayúscula.

### Cargadores de plantillas (o Loaders)

En nuestros pequeños proyectos no está mal abrir y renderizar las plantillas como lo hemos hecho hasta ahora, abriendo el archivo con un *open*, indicando el path, y luego cerrando el archivo. Pero normalmente en proyectos tendremos que cargar más de una plantilla, y hacer esto con cada uno no es lo más óptimo. Para ello usaremos lo que se llama un **Loader** o **Cargador**.

Consiste en decirle a Django que todas nuestras plantillas va a estar en un directorio concreto y asi cuando queramos usarlo, no tendremos que decirle a Django donde está, no tendremos que abrirlo ni cerrarlo; solo usar el nombre de la plantilla.

Para hacer esto, en nuestro archivo de vistas tendremos que importar desde la libreria de templates el loader
``` 
from django.template import loader
```
<br>

o bien si lo vamos a usar mucho
```
from django.template.loader import get_template
```
<br>

El método *get_template()* es la clave que le permitiria a Django saber qué plantilla del directorio es la que queremos.Vamos a ver cómo funciona el loader. Para ello vamos a crear una nueva vista ``saludo_Loader``. La vista (habiendo importado previamente el loader) consistira en el siguiente código:

```
def saludo_Loader(request):
    templ = loader.get_template('lista_Ejemplos_Template.html')
    #templ = get_template('lista_Ejemplos_Template.html')  #si solo hemos importado el get_template
    dict = {"lista_nombres":["Jose", "Raul", "Pedro", "Juan", "Ramón"]}
    document = templ.render(dict)
    return HttpResponse(document)
```

Para indicar el directorio donde vamos a tener almacenadas nuestras plantillas, tendremos que hacerlo desde el archivo `settings.py`. En el archivo settings tenemos una lista llamada *TEMPLATES* con un diccionario con toda la información relacionada con las plantillas. En el diccionario podemos ver una key llamada `DIRS` con una lista vacía. Cuando está vacia, Django busca en un directorio por defecto en la instalación de Django. Añadimos simplemente la ruta de la carpeta donde tenemos almacenadas nuestras templates a la lista de `DIRS`.

Una cosa muy **importante** que podemos notar es que ahora no usamos contexto. La función *get_template()* nos devuelve una instancia de una clase Template, PERO no es la misma clase Template que en los casos anteriores. Por asi decirlo es como una clase Template de Loader. Y en este tipo de Templates, el render funciona de manera diferente. No admite un Contexto como parámetro, sino directamente un diccionario, asi que aparte de ahorrarnos toda la parte de abrir leer y cerrar los archivos, tambien nos ahorramos una instancia del Context al usar Loaders. Podemos ver nuestro Loader en la URL http://127.0.0.1:8000/saludo_loader/

### Shortcuts

Nuestro código ahora mismo está muy simplificado, pero podriamos simplificarlo incluso más. Ahora mismo creamos una instancia de una template con el *get_template* y tenemos que renderizarla. Sin imbargo, hay una biblioteca de Django que nos permite hacerlo todo de una vez, la librería **shortcuts**.

Vamos a usar la función *render* de esta biblioteca, y en su documentación oficial (https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/) podemos ver más información sobre la función. 
 
Vamos a crear otra view para este ejemplo. El primer paso va a ser importar la función de la biblioteca. Entonces escribimos en la sección de imports del archivo de views 

```
from django.shortcuts import render
```

La función render toma como parámetros obligatorios una request y el nombre de la plantilla, y como parámetros opcionales un contexto. Vamos a ver como escribiriamos la sintaxis de la view.

```
def saludo_Shortcut(request):
    dict = {"lista_nombres":["Jose", "Raul", "Pedro", "Juan", "Ramón"]}
    return render(request,'lista_Ejemplos_Template.html',dict )       
```
Como podemos ver, ahora no ha sido necesaria la instancia de plantilla ni contexto, por lo que nos hemos ahorrado unas cuantas lineas, y ahora nuestra vista devuelve una función render, no una HttpResponse. Podemos verlo en la URL http://127.0.0.1:8000/saludo_shortcut/

### Templates incrustadas

A veces tendremos que unir varios HTML dentro de un mismo porque queremos reutilizar varias veces el mismo archivo. Por ejemplo, una barra de navegación que queramos poner en todas nuestras URLs en las cabeceras. Lo que se suele hacer es hacer la barra en un fichero HTML independiente e incrustarlo en nuestra página web.

Vamos a ver cómo funcionan las incrustaciones. Vamos a crear una nueva plantilla `barra.html` con una lista muy básica. ya después añadiremos CSS.
```
<html>
<body>
    <ul>
        <li>Home</li>
        <li>Servicios</li>
        <li>Quienes sómos</li>
        <li>Contacto</li>
        <li>Acerca de</li>
    </ul>
</body>
</html>
```

Despues simplemente tenemos que indicar en nuestra template principal donde ira incrustada nuestra plantilla secundaria.  

```
<html>
    <body>
        {% include "barra.html" %}
        <h1>
            Hemos incrustado una barra de navegación al inicio del todo.
        </h1>
    </body>
</html>
```

Como podemos ver, para incrustar una plantilla simplemente debemos escribir `{% include "nombre_fichero" %}` domde queramos situar la plantilla secundaria. Ya podemos añadirle a nuestar barra un poco de estilo con un CSS en el fichero HTML. Le damos el id *barra* a nuestra lista de elementos, `<ul id = "barra">
`, y simplemente añadimos a nuestro archivo de barra.html la siguiente etiqueta de estilo:

```

<style>
#barra{
    margin:0;
    padding: 0;
    list-style: none;
    text-transform: uppercase;
}

/* estilo descendiente */
#barra li{
    display: inline; /*elementos en linea*/
    margin: 0 30px;
}
</style>
```

Ahora parece más una barra de navegación

### Herencia de Templates

A veces puede ocurrir que una página web tenga que teneer los mismos elementos comunes en todos lados, como un header o un footer, pero el contenido tenga que ir cambiando. Entonces ir añadiendo el include en cada sitio puedo no ser lo más optimo. Para estos casos usamos la **Herencia de plantillas**

Es muy similar a como funciona la herencia de POO en Python. Tenemos una plantilla padre con todos los contenidos que van a ser común en todos los sitios web y un **bloque cambiante** que es lo que va a ir cambiando de plantilla en plantilla.

Para indicarle a Django que una plantilla va a heredar de una plantilla pader, simplemente tenemos que utilizar la etiqueta `{% extends "nombre_plantilla" %}`. Es muy importante para que funcione bien que esta etiqueta sea la primera que aparezca en las plantillas hija.

Vamos a empezar creando una plantilla padre, `padre_Template.html` con la siguiente estructura

```
<html>
    <head>
        <title>
            {% block title %}
            {% endblock %}
        </title>
    </head>
    <body>
        <h1> Test Gonzalo</h1>
        <h3> Prácticas de Django</h3>
        {% block content %}
        {% endblock %}
        <p>
            Pie de página común a todo
        </p>
    </body>
</html>
```

Para indicarle a Django que un bloque va a cambiar de template en template, simplemente usamos la etiqueta `{% block nombre_bloque %}` cerrándola posteriormente con `{% endblock %}`. En este ejemplo hemos creado un HTML básico donde el titulo y el contendio va a cambiar, pero los Headers y el pie de página será el mismo para todas las hijas. 

Ahora crearemos una template hija, `hija1_Template.html`, extendiendo de la template padre primero, y poniendo entre las etiquetas de block lo que queremos que contenga esa template.
```
{% extends "padre_Template.html" %}

{% block title %}
Hija numero 1
{% endblock %}

{% block content %}
<p> Estamos a día: {{fecha}}</p>
{% endblock %}
```

Si creamos una view que renderice `hija1_Template.html` como hemos visto en apartados anteriors, y creamos un URL para esta view, (http://127.0.0.1:8000/herencia1_template/ en mi caso), podemos ver que en el titulo de la pestaña aparece efectivamente el titulo de Hija número 1, y que paarece el párrafo con la fecha actual.

Si ahora creamos una segunda plantilla hija, `hija2_Template.html`, solo tenemos que cambiar el código de los bloques, y el resto seguirá igual. 

```
{% extends "padre_Template.html" %}

{% block title %}
Hija numero 2
{% endblock %}

{% block content %}
<p> Esta es la hija 2</p>
{% endblock %}
```

Podemos ver la nueva plantilla en http://127.0.0.1:8000/herencia2_template/ (abiendo creado previamente el URL de herencia2_template claro). Podemos incrustar plantillas en la plantilla padre, por ejemplo la barra de navegación que creamos en el apartado anterior, para que todas las hijas también lo tengan. En este caso queremos que esté bajo el titheaderulo que hemos creado, asi que incluiremos la barra bajo el la etiqueta h1 en la plantilla padre
```      
<h1> Test Gonzalo</h1>
{% include "barra.html" %}
<h3> Prácticas de Django</h3>`
```
<br>

## BASES DE DATOS

### Introducción
Hasta ahora hemos visto la parte Template y View del estilo MTV que es Django. Ahora vamos a pasar a ver la parte del Modelo. En esta sección trabajaremos con una base de datos de SQLlite3, que viene instalada por defecto con Django y es muy útil para pequeños proyectos.

Como la base de datos ya está creada, nosotros solo necesitaremos crear las tablas con las columnas e información que necesitemos. Para ello usaremos la clase ***Model*** de Django. 

Para trabjar con la base de datos vamos a crear un nuevo proyecto que será una Tienda Online con una aplicqación que gestione los pedidos y tenga diversas tablas de bases de datos. Un proyecto no tiene porque tener aplicaciones, sobre todo si es pequeño, pero para poder trabajar con modelos y bases de datos Django necesita que exista al menos una aplicación.