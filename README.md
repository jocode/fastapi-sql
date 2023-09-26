# SQLAlchemy: el ORM de FastAPI

SQLAlchemy es un ORM (Object Relational Mapper) que permite trabajar con bases de datos relacionales de una forma más sencilla y orientada a objetos.


> :bulb: Activar el entorno virtual
> - **`python3 -m venv venv`**
> - **`source venv/bin/activate`**


## Qué es un ORM?

Es una librería que nos permite la manipulación de tablas de una base de datos como si fueran objetos de nuestra aplicación.

## Qué es SQLAlchemy?

Es una librería para python que facilita el acceso a una base de datos relacional mapeando tablas SQL a clases.

## Instalación y configuración de SQLAlchemy

Primero debemos instalar las dependencias que necesitaremos en el proyecto.

- **`pip install fastapi`**
- **`pip install uvicorn`**
- **`pip install sqlalchemy`**

- **`uvicorn main:app --reload --port 5000`**

## Estructura del proyecto

La estructura del proyecto separa cada una de las capas de la aplicación en diferentes directorios. En este caso,
tendremos los siguientes directorios:

```
project/
├── config/
├── middlewares/
├── models/
├── routers/
├── schemas/
├── services/
└── main.py
```

- **`config/`**: En este directorio se encuentran los archivos de configuración de la aplicación. Como por ejemplo, la
  configuración de la base de datos, la configuración de los logs, etc.
- **`middlewares/`**: En este directorio se encuentran los middlewares de la aplicación. Un middleware es un componente
  que se ejecuta entre el cliente y el servidor. Por ejemplo, un middleware puede ser un componente que se encargue de
  validar el token de un usuario.
- **`models/`**: En este directorio se encuentran los modelos de la aplicación. Un modelo es una clase que representa
  una tabla de la base de datos.
- **`routers/`**: En este directorio se encuentran los routers de la aplicación. Un router es un componente que se
  encarga de recibir las peticiones HTTP y enviarlas al controlador correspondiente.
- **`schemas/`**: En este directorio se encuentran los schemas de la aplicación. Un schema es una clase que representa
  el esquema de un modelo, es decir, la información que se va a recibir o enviar en la petición HTTP.
- **`services/`**: En este directorio se encuentran los servicios de la aplicación. Un servicio es una clase que se
  encarga de realizar una tarea específica. Por ejemplo sera el encargado de realizar las operaciones CRUD de un modelo,
  o el encargado de enviar un correo electrónico. También se puede llamar a los servicios como controladores.
- **`main.py`**: En este archivo se encuentra el punto de entrada de la aplicación. Es decir, el archivo que se encarga
  de ejecutar la aplicación.