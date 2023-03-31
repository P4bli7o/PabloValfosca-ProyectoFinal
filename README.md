# Proyecto Final - Pablo Valfosca

### Entrega Final Curso Python - Coderhouse - Marzo 2023
      - Profesor: German Martinez
      - Comision 48405
      - Video de explicacion: 

## Contenido de la pagina web

- La imagen "WORLDTECH" lleva al administrador cliqueando sobre ella.

- En el boton "INICIO" se presentan los publicaciones creadas recientemente con los ultimos reviews, noticias y novedades de tecnologia 
y computacion, en el carousel se muestran las destacadas y mas abajo las ultimas publicaciones creadas.

- El boton de BLOG se divide en "Todos los Posts" - "Mis Posts" y "Nuevo Post"

      - Si no se esta logueado solo permite ver todos los post, aparece una lista con todos los que hay 
      y se puede entrear al detalle y ver la nota completa, si no hay post aparece una leyenda.

      - Una vez logueado se habilita 2 botones mas, "Mis Posts" que se ven todas las creaciones propias con 
      permiso de actualizar y borrar, y el "Todos los Posts", los que no son de mi autoria solo deja ver el 
      detalle, no estan los botones de borrar y actualizar aca tambien si no hay nada creado muestra un 
      texto diciendo que esta vacio.

      - El boton "Nuevo Post" lleva a una pagina donde hay un formulario y se cargan los datos, texto e 
      imagenes para crear la publicacion, hay una esquematica al lado que muestra como va a quedar la 
      publicaion cargada y el orden en donde estan los elementos que se llenan del formulario.
      
      
- El boton de MENSAJES se divide en "Enviar mensaje" y "Ver mis mensajes", este ultimo solo se activa al iniciar sesion.

      - "Enviar mensajes" esta habilitado para cualquiera no es necesario tener usuario, dirige lleva a una 
      pagina donde hay un formulario para la carga del mensaje.
      
      - "Ver mis mensajes" una vez iniciado sesion se muestra la lista de mensajes con el asunto, nombre y 
      fecha de enviado y al cliquear en detalle lleva a mostrar el contenido, tiene la opcion de borrar, 
      si no hay mensajes muestra una leyenda.
      
      
- El boton SOBRE MI es una breve presentacion de quien soy a que me dedico y porque decidi hacer de esta tematica 
el proyecto final.

- El boton INICIAR SESION te envia a una pagina que pide usuario y contraseña para poder ingresar, una vez ingresado 
en la barra aparece el nombre con la foto, cliqueando en el esta la opcion de "Crear Perfil" o "Actualizar Perfil" 
segun sea el caso y la opcion de "SALIR" que dirige a cerrar sesion y me muestra en otra pagina que se ha salido.

      - "Crear Perfil y "Actualizar Perfil" va a una pagina donde pide a travez de un formulario simple 
      que cargue la foto de perfil, si no esta creado aparece el boton crear y despues de la primera vez 
      ese boton va a cambiar a actualizar.
      
      - "SALIR" cierra la sesion y desabilita algunas opciones por quedar deslogueado.


- El boton REGISTRARSE crea un usuario nuevo, me lleva a una pagina y me pide nombre de usuario, contraseña y 
repetir contraseña

- La barra de BUSCAR, permite realizar una consulta y encontrar lo relacionado con lo ingresado en el campo, si no 
hay coincidencias muestra una leyenda 




## Algunos comandos a tener en cuenta


### Abrir el proyecto en un repositorio local

  - Para correr este proyecto se necesita Python 3.10 o superior y el framework Djando

  - Instalar Django

        pip install django
  - Abrir Vs code y crear una carpeta donde se alojara el repositorio

  - Abrir una terminal bash/cmd/powershell y correr

        git clone (link nombre de la url del repositorio creado en github) .  <---  se clona lo que este en
        el repositorio no olvidarse del "espacio" y del "pto", hace que no se genere otra carpeta dentro de 
        la general creada.
  
        python manage.py migrate  <---  para realizar la creacion de las tablas de la bd



### Crear un repositorio desde Cero

  - Crear un repositorio en Github

      - Debemos ir a arriba a la derecha donde tenemos nuestra sesion iniciada y vamos a ver un mas, cliqueamos ahi y en 
      new repositorio

      - Agregamos el nombre que se le quiera dar, siempre y cuando este disponible.

      - Se tilda la opcion de agregar archivo readme.

      - Buscar la opcion .gitignore y elegir python  <--- esto hace que cuando estemos trabajando y querramos enviar lo creado de manera 
      local no guarde archivos basura y tampoco la base de datos creada con la que trabajamos en el local.

      - Crear repositorio

  - Abrir Vs code y crear una carpeta donde se alojara el repositorio

  - Correr los siguientes comandos en la terminal (pueden variar de un sist operativo a otro) bash en windows

        django-admin starproject (nombre del proyecto) .  <---  creacion de la carpeta del proyecto

        python manage.py startapp (nombre de la app) .  <---  creacion de la carpeta de la app



### Correr el servidor

  - Desde la terminal
  
        python manage.py runserver   <---  se genera por defecto en esta direccion http://127.0.0.1:8000/



### Si se modifica algun modelo

  - Desde la terminal
  
        python manage.py makemigrations  <---  para detectar los cambios y generar los scripts para 
        actualizar y modificar la bd
        python manage.py migrate   <---  corre los scripts y crea/modifica la tabla de la bd



### Crear un administrador

  - Desde la terminal bash en windows para crear un super-usuario

        python manage.py createsuperuser --username (nombre del administrador)
        
        Ingresar Email y Password(el cursor no se mueve y no se registra tipeo por seguridad, parece que no 
        funciona) y una verificacion del Password



### Utilizar archivo de prueba de carga de datos

  - Usar el archivo seed_data.py

  - Desde terminal bash en windows

        python manage.py shell < seed_data.py
        
  - Desde terminal powershell

        python manage.py shell
        
  - Dentro del shell hacer

        import seed_data



### Comandos de Git

  - Desde la terminal

        - git clone (link nombre de la url del repositorio creado en github) .    <---  se clona lo que este 
        en el repositorio remoto, no olvidarse del "espacio" y del "pto", hace que no se genere otra carpeta 
        dentro de la general creada.

        - git branch / git branch --list  <---  muestra el listado de ramas que se tienen en el repositorio

        - git branch -m (nombre rama)   <---  cambiar nombre de la rama que fuimos creando a lo largo del 
        proyecto

        - git log  <---  para ver los commit q tengo, todos los ptos de recuperacion q fuimos creando a lo 
        largo de la vida de nuestro proyecto

        - git status    <---  nos muestra cuales archivos estan siendo seguidos para ser versionados, como 
        tambien los q no y ademas las modificaciones, creaciones o borrados del contenido hasta ahora

        - git checkout  (nombre de la rama)  <---  permite movernos en las disitntas versiones del codigo, 
        ir a una rama en particular

        - git checkout -b (nombre-de-tu-rama)  <---  crear una rama nueva y movernos a ella directamente

        - git branch -d (nombre rama) / git branch --delete (nombre rama)  <---  borra una rama

        - history te muestra todos los comandos que se usaron en esa sesion

        - git merge (nombre de la rama q se quiere fusionar)  <---  fusiona una rama con otra agregandole 
        los ptos de commit que tiene y las modificacioens que se hicieron, pararse en la rama a la que se 
        le quiere fusionar la otra 

        - git reset –hard (codigo alfanunerico commit)  <---  elimina los commit que estan arriba de ese 
        pto de recuperacion no hay vuelta atras si se usa este comando

        - git add .   <---  hace que toda modificacion creacion o borrado o archivo que no esta siendo 
        seguido se agregue para el proximo commit

        - git add (nombre del archivo)   <---  para agregar solo un archivo al stagging 

        - git commit -m "mensaje de descripcion de lo q se hizo"   <---  se crea un pto seguro de todo 
        lo que se agrego anteriormente

        - git remote -vv  <---  para ver en que directorio estoy

        - git push origin (nombre rama)  <---  para enviar solo la rama donde estoy parado de mi 
        repositorio local al remoto

        - git push --all origin  <---  sube todas las ramas con todos los commits que tiene cada uno al 
        repositorio remoto de GitHub

        - git pull   <---  para enviar desde el repositorio remoto alguna actualizacion del codigo que no 
        esta en nuestro repositorio local 
