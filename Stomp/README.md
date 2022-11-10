## Como hacer funcionar Stomp

Disclaimer: Yo lo instalé en Windows, no tengo idea como hacerlo en Linux.

1) Descargar e instala RabbitMQ en https://www.rabbitmq.com/install-windows.html#downloads en la parte que dice "Direct Downloads"
2) Ahora intentar correr el RabbitMQ para ver si se instaló bien. Esto se hace a través de la consola del RabbitMQ. Los comandos son:
  - Para instalar: .\rabbitmq-service.bat install
  - Para desinstalar: .\rabbitmq-service.bat remove
  - Para iniciar: .\rabbitmq-service.bat start
  - Para detener: .\rabbitmq-service.bat stop
3) Suponiendo que funcionó, hay que instalar los plugins usando los siguientes comandos en la consola de RabbitMQ:
  - rabbitmq-plugins.bat enable rabbitmq_management
  - rabbitmq-plugins.bat enable rabbitmq_stomp
4) Después de instalar los plugins, detener e iniciar RabbitMQ (con los comandos de la parte 2) y luego ingresar a http://localhost:15672/ con el usuario y pass 'guest' y 'guest'.
5) Dentro de la página seguir los pasos de este tutorial https://funprojects.blog/2020/05/14/stomp-protocol-with-rabbitmq-node-red-and-python/
6) Instalar Stomp en python con 'pip install stomp.py'
7) Correr stomp_listener.py y en otra consola correr stomp_producer.py

*) Una modificación que hice pero creo que no sirvió de nada, fue colocar explicitamente el puerto. Esto lo hice creando un archivo en C:\Users\User\AppData\Roaming\RabbitMQ\rabbitmq-env-conf.bat y colocándole 'set DIST_PORT=44556'.
