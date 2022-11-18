# MatrixInfoAggregator

_MatrixInfoAggregator_ es un servicio incluido dentro del proyecto _LumenSense_, que trata los datos recibidos del sensor para luego enviarlos de una forma compacta y útil a la cola en RabbitMQ, alojada en AWS.

## Forma de uso

### **Opción 1 (Recomendada):** Construir imagen

Puede utilizar nuestro servicio, puede construir una imagen usando Docker, el cual utiliza la imagen de Python 3.9.15. Por ejemplo, puede construir la imagen con:
```console
docker build -t palotes-de-perico/matrix-info-aggregator:0.0.1 .
```
para luego ejecutar un contenedor con:
```console
docker run <id>
```
donde el `<id>` se obtiene mediante el uso de:
```console
docker images
```
y revisando el tag asignado en el primer comando.

### **Opción 2:** Script

Para la facilidad del usuario final y de los desarrolladores mismos, se creó un sencillo script que permite levantar el proyecto de forma sencilla. Para ello, sólo debe ejecutar el script `run.sh` desde la carpeta `MatrixInfoAggregator`.

### **Opción 3:** Configuración manual

En caso de no poder ejecutar el script, se puede levantar el servicio manualmente, para ello:

1. Debe crear un entorno virtual para instalar las dependencias. Se recomienda usar el módulo `venv` de Python, de la siguiente forma:

```console
python -m venv <nombre>
```
donde nombre es el el nombre del entorno virtual a crear. Luego, puede ingresar usando:
```console
source <nombre>/bin/activate
```
en GNU/Linux con `bash`, o:
```console
<nombre>\Scripts\Activate.ps1
```

2. Utilice el comando:
```console
pip install -r requirements.txt
```
para instalar las librerias de Python necesarias para ejecutar el servicio.

3. Ejecute el servicio contenido en la carpeta `src`:
```console
python src/
```
