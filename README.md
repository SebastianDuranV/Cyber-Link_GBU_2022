# Proyecto "Cyber Link GBU 2022"
~~Traducir al ingles y portuges~~

# Objetivo del proyecto

Este es un proyecto creado con mucho amor, para la obra de Cristo, dentro de la universidad. En la que pueda traer mayor gozo dentro de las reuniones administrativas. 

*"Saludaos unos a otros con ósculo de amor. Paz sea con vosotros los que estáis en Jesucristo. Amén."*

**1 Pedro 5:14**

# Introducción 


# Manual de desarrollador
## Backend
Para el desarrollo eficiente del proyecto, es necesario desarrollar una api rest, en que pueda en uin futuro adecuarce a las necesidades de cada grupo o ministerio que lo necesite.
Por lo tanto ahora se mostrará las herramientas usadas.
Base de datos: MySQL
Codigo en python.
Librería de serviodor: Flask.

El diagrama de clases para el proyecto:
https://drive.google.com/file/d/10ZAML4FFIYqdfbN3EsozhDKaA7v2zIoR/view?usp=sharing

La arquitectura de la base de datos:
https://docs.google.com/drawings/d/1yPsAwcgLrZl_9ui5iSGcvJf1lK7UsoHk7CYx_2_HPjM/edit


## Requerimientos

## Base de datos
### Para windows:

----
### Para sistmesa linux (Basados en Debian)
Para instalar la base de datos es necesario seguir este tutorial hecho por la comunidad de digitalocean:

https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04-es

Como recordatorio es necesario, so o si, seguir todos los pasos para que pueda funcionar la implementación en un ordenador. (Así mismo es importante escribir una contraseña que tenga almenos una minuscula, una mayuscula, un caracter especial y un numero, ademas de un largo de 8 como indica las instrucciones.)

Ademas de isntalar las siguientes librerias necesarias. 

Por lo que en terminal ejecuta:

`sudo apt-get install libmysqlclient-dev`

Ademas:

`pip3 install mysqlclient` 

o

`pip3 install mysql-connector-python`

En el caso que no detecte el "pip3" cambielo por "pip"

---
## Implementación
### En linux:

Desde el archivo "backend" ejecuta en terminal:

`source venv/Script/activate`

`cd src`

`flask run`

Luego de esto tendrás que ir a navegador o implementador de consultas(postman) a localhost:5000/vote 

### Para windows:

-------
## Manual de usuario




---------
**Hecho por Grupo Bíblico Universitario de Chile**
