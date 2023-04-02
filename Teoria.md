# DJANGO FRAMEWORK 
## Índice

1. [Introducción](#introducción)
2. [Primer Proyecto](#primer-proyecto)


***

### INTRODUCCIÓN
#### ¿Qué es Django? 
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
### PRIMER PROYECTO

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
    
    
#### Inicio de la base de datos
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
