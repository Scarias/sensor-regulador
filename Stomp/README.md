# Stomp Sensor Regulador

## Iniciando servidor RabbitMQ

### Windows

1. Descargar e instalar [RabbitMQ para Windows](https://www.rabbitmq.com/install-windows.html#downloads), en la parte
   que
   dice "Direct Downloads".
2. Verificar la instalación de RabbitMQ instalando y iniciando el servicio. Esto se hace a través de la consola del
   RabbitMQ. Los comandos son:
    - Para instalar: `.\rabbitmq-service.bat install`.
    - Para desinstalar: `.\rabbitmq-service.bat remove`.
    - Para iniciar: `.\rabbitmq-service.bat start`.
    - Para detener: `.\rabbitmq-service.bat stop`.
3. Luego de verificar su instalación correcta, se debe instalar los plugins usando los siguientes comandos en la consola
   de RabbitMQ:
    - `rabbitmq-plugins.bat enable rabbitmq_management`.
    - `rabbitmq-plugins.bat enable rabbitmq_stomp`.
4. Después de instalar los plugins, detener e iniciar RabbitMQ (con los comandos de la parte 2) y luego ingresar
   a http://localhost:15672/ con el usuario y contraseña 'guest' y 'guest'.

### Linux

1. Instalar RabbitMQ para
   Linux ([Debian/Ubuntu](https://rabbitmq.com/install-debian.html), [RHEL/CentOs/Fedora](https://rabbitmq.com/install-rpm.html),
   [construyendo binarios](https://rabbitmq.com/install-generic-unix.html)
   o [Solaris](https://rabbitmq.com/install-solaris.html)), siguiendo las instrucciónes indicadas.
2. Instalar, con tu gestor de paquetes de la distribución, `rabbitmq-server`.
3. Verificar la instalación y configurar RabbitMQ Server en la máquina con los comandos (con privilegios de
   super-usuario):
    - Para instalar: `rabbitmq-server install`.
    - Para desinstalar: `rabbitmq-server remove`.
    - Para iniciar: `rabbitmq-server start`.
    - Para detener: `rabbitmq-server stop`.
4. Configurar plugins para usar stomp (con privilegios de super-usuario):
    - `rabbitmq-plugins enable rabbitmq_management`.
    - `rabbitmq-plugins enable rabbitmq_stomp`.
5. Dentro de la página seguir los pasos
   del [siguiente tutorial](https://funprojects.blog/2020/05/14/stomp-protocol-with-rabbitmq-node-red-and-python/).

## Ejecutando el Stomp

1. Dentro de la página seguir los pasos
   del [siguiente tutorial](https://funprojects.blog/2020/05/14/stomp-protocol-with-rabbitmq-node-red-and-python/).
2. Instalar Stomp en python con 'pip install stomp.py'.
3. Correr stomp_listener.py y en otra consola correr stomp_producer.py.

> Una modificación que hice pero creo que no sirvió de nada, fue colocar explicitamente el puerto. Esto lo hice creando
> un archivo en C:\Users\User\AppData\Roaming\RabbitMQ\rabbitmq-env-conf.bat y colocándole 'set DIST_PORT=44556'.
