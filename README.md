# Django_project
Proyecto desarrollado con Django

Proyecto desarrollado con base en una prueba técnica proporcionado por el equipo de "Dev Tech", la cual tiene como finalidad conocer los conocimientos y aptitudes de mí parte en relación al manejo de ciertas 
Tecnologías.
El proyecto fue desarrollado con el lenguaje  programación más popular de la actualidad "Python", el cual es uno de lo más flexibles y usado en la actualidad, además se usó el Framwork “Django” para generar una 
Aplicación web que cumplirá con los estándares establecidos en la descripción del documento.

Lo cual consistia en lo siguiente:
Objetivo de la prueba técnica:
Evaluar la capacidad del candidato para crear un CRUD sencillo utilizando Django.
Instrucciones:
1. Genera un nuevo proyecto Django llamado "mi_crud_project".
2. Crea una base de datos MySQL llamada miCrudProject.
3. Crea una aplicación llamada "mi_crud_app" en el proyecto.
4. Define un modelo llamado “Producto” en la aplicación "mi_crud_app". El modelo debe tener
los siguientes campos:
a. Nombre (CharField)
b. Descripción (TextField)
c. Precio (DecimalField)
d. Fecha de creación (DateField)
5. Crea una vista basada en clases que permita mostrar una lista de todos los productos en
na página llamada "lista_productos".
6. Crea una vista basada en clases que permita agregar un nuevo producto en una página
llamada "agregar_producto". Debe incluir un formulario para ingresar la información del
producto.
7. Crea una vista basada en clases que permita ver los detalles de un producto en una página
llamada "detalle_producto". Debe mostrar todos los campos del producto.
8. Crea una vista basada en clases que permita editar la información de un producto en una
página llamada "editar_producto". Debe incluir un formulario prellenado con la información
actual del producto.
9. Crea una vista basada en clases que permita eliminar un producto en una página llamada
"eliminar_producto". Debe mostrar una confirmación antes de eliminar el producto.
10. Configura las URL para las vistas mencionadas anteriormente.
11. Crea un archivo README que explique cómo ejecutar el proyecto y las pruebas.
12. Todas las transacciones se deberán realizar con la base de datos creada en el paso 2.
Esta prueba evaluará la capacidad del candidato para crear un CRUD básico utilizando Django,
incluyendo la definición de modelos, vistas basadas en clases y URLs. También se espera que el
candidato siga las mejores prácticas de desarrollo de Django.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Los pasos para ejecutar la aplicación ya sea el codespace de github o de manera local son los siguientes:

Ejecutarlo de manera local:
1-al ingresar al link que les propociones, deben cambiar ciertos parámetros para la visualización del proyecto.
Deben de cambiar de "main" a "master", para que el proyecto esté disponible.

2-Descargan el proyecto y lo ejecutan de manera correcta, preferiblemente en "visual studio code"

Ejecutarlo de manera virtual en el Codespace de Github:
1-cambiamos parámetros como en el anterior proceso, de "main" a "master", lo cual hara visible el proyecto.

2-damos clic en la opción "Code", luego seleccionamos la opcion de "Codespaces", lo cual generara una ventana como visual studio para ver el código fuente del proyecto.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Para ejecutar el proyecto de manera local, tendremos que hacer lo siguiente:
1-desplegamos el árbol de trabajo que desarrolle

2-nos dirigimos a la carpeta "mi_crud_project"

3-desplegamos sus elementos e identificamos el archivo "manage.py"

4-damos derecho y seleccionamos la opción "Open in Integred Terminal"

5-una vez desplegada la terminal, ejecutamos el siguiente código: python manage.py runserver

6-una vez ejecutado el código, nos proporcionará cierta información, una de ellas es enlace al proyecto ejecutado en el navegador:  http://127.0.0.1:8000/ ---> similar a este

7-listo podremos ejecuta pruebas, para revisar la funcionalidad que le he dado

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Pruebas del proyecto:
Una vez desplegado el proyecto podremos ejecutar las tareas previamente codificadas, con la funcionalidad de proveer herramientas al usuario.

En el menú tendremos una descripción del proyecto, su menú y su desarrollado:
El menú principal cuenta con dos opciones:

1-agregar producto: este proyecto redirige a una nueva ventana construida con Html5 + Boostrap(Css3), la cual provee un formulario, en donde el usuario deberá llenar todos los 
campos

2-Listar producto: al dar clic sobre esta ventana nos muestra un listado de los productos previamente ingresados en la base de datos, cada producto tiene 3 opciones:

2.1-Editar: al dar clic en esta opción, no muestra el formulario con los datos en cada opción, de manera que editarlo sea más fácil, después damos guardar y volvemos
al listado de producto.

2.2-Eliminar: al dar clic sobre esta opción nos redirigirá a una ventana nueva, en donde tendremos un aviso de las implicaciones de eliminar el producto y con el botón que cumple
la determinada acción.

2.3-Detalle: Nos muestra la información sobre cada producto ingresado a la base de datos.



