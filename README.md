# LumenSense

`LumenSense` es un proyecto del curso de Taller de Programación, que consiste en regular la intensidad lumínica de una determinada configuración de fuentes a través de sensores de proximidad.

## ¿Por qué _LumenSense_?

El objetivo este sistema es reducir el uso de energía, a través de la automatización de la regulación de la intensidad de los focos.

Para lograrlo, se usarás sensores cercanos a estos focos que se utilizarán para estimar que focos requieren mayor o menor intesidad lumínica.

## Estructura del proyecto

Por temas de organización, las instrucciones de uso de cada servicio indicado en esta sección están dentro del `README.md` de la carpeta respectiva.

- **`Resources`:** Contiene archivos solicitados por el profesor o que sirven para explicar la estructura del proyecto mismo, y que no representan una implementación como tal.
- **`Stomp`:** Corresponde a un generador de datos que utiliza la librería `stomp` de Python para conectarse al broker de RabbitMQ que _hosteará_ este servicio.
- **`MatrixInfoAggregator`:** Es el servicio representado en el modelo como _MatrixInfoAggregator_. Este contiene un paquete del mismo nombre que permite ejecutar el servicio, el cual utiliza nuevamente `stomp` para recibir los datos del broker local y enviarlos al broker en la nube, _hosteado_ en Amazon Web Services.
- **`BD`:** Contiene un sencillo script extensible, que permite manipular la base de datos alojada en Amazon Web Services (AWS), y se utiliza para establecer la información correspondiente a la infraestructura. Una variación más reducida y con sólo lo necesario para funcionar se encuentra levantada como una función Lambda registrada en AWS.
- **`ExpertSystem`:** Para saber cuanta energía lumínica se debe asignar a los controladores de voltaje, se debe calcular, en base a las distancias entre focos y foco-persona, a través de un _sistema experto_, y este es representado bajo el servicio de `ExpertSystem`, en su carpeta correspondiente del mismo nombre. Para efectos prácticos, se simula el sistema experto para que el servicio compuesto funcione.