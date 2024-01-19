# repositorio1

# Practica con uso de Docker

En este repositorio se ha creado el archivo Dockerfile en lugar de usar Docker Compose, con la configuración que permite crear una imagen de Python en Docker y ejecutar al final el código hecho en Python.

## Requisitos

- Tener instalado Docker en su máquina.

## Instrucciones.

### 1. Clonar el Repositorio:

```bash
git clone https://github.com/OswaldoRaLo/repositorio1
cd tu_proyecto
```

### 2. Configuración del Dockerfile:
Revisar que exista el archivo `Dockerfile` en la raíz del proyecto con el siguiente contenido:

```Dockerfile
FROM python:3
WORKDIR /app
COPY ./codigo /app
CMD ["python3", "suma.py", "5", "6"]
```

Las variables 5 y 6 son las que se suman y pueden ser cambiadas.

### 3. Construir la Imagen y Ejecutar la Aplicación:
Ejecutar los siguientes comandos en la terminal para construir la imagen y iniciar la aplicación:

```bash
docker build -t my-python-app .
docker run my-python-app
```

### 4. Verificar la Salida:
Revisar la salida en la terminal para ver los resultados.
#### [1,1]

### 5. Detener la Aplicación:
Se puede detener la aplicación con el siguiente comando:

```bash
docker container stop $(docker container ls -q --filter ancestor=my-python-app)
```

Ten en cuenta que ahora estamos utilizando un Dockerfile en lugar de un archivo de Docker Compose.
