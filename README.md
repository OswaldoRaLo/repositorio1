# repositorio1

# Practica con uso de docker

En este repositorio se creo el archivo compose.yaml, con la configuración con la configuracion
de permite crear una imagen de python en docker y ejecutar al final el código hecho en python.

## Requisitos

- Tener instalado Docker en su máquina.

## Instrucciones.

### 1. Clonar el Repositorio:

bash
git clone https://github.com/OswaldoRaLo/repositorio1
cd tu_proyecto

###2. Configuración del Docker Compose:
revisar que exista el archivo docker-compose.yaml en la raíz del proyecto con el siguiente contenido:

yaml
version: '3'
services:
  python_app:
    image: python:3
    volumes:
      - ./codigo:/app
    working_dir: /app
    command: python3 suma.py 5 6

###3. Ejecutar la Aplicación:
Ejecutar el comando en la terminal para iniciar la aplicación:

bash
docker-compose up

###4. Verificar la Salida:
Revisar la salida en la terminal para ver los resultados.
#### [1,1]

5. Se puede detener la Aplicación:
Se puede detener la aplicación con el siguiente comando:

bash
docker-compose down
