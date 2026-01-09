PRUEBA TECNICA CONSULTOR ANALÍTICO

BLOQUE 1

Este proyecto es un construido con Django el cual incluye una tabla con datos simulados
(Fecha, Cliente, Métrica, Valor) generados desde el backend y renderizados en una 
plantilla HTML.

Características:

- Framework: Django
- Datos simulados en el backend con Python utilizando un ciclo for que llena una lista de datos
  de clientes y metricas y utilizando el metodo choice de la libreria random para hacer aleatoria
  la presentacion de los datos.
- Visualización de tabla.html y index.html este ultimo se le agrego un boton que direcciona
  directamente a la tabla.

Pasos para ejecutar el proyecto:

1. Descargar el repositorio
2. Crear y activar un entorno virtual
3. Instalar Django
4. Correr servidor Django
5. Abrir en el navegador
- Portal principal: http://127.0.0.1:8000/
- Tabla analítica: http://127.0.0.1:8000/tabla/

BLOQUE 2

Tabla analítica llamada: project.dataset.ventas_diarias

Columnas:
- fecha (DATE)
- cliente_id (STRING)
- producto (STRING)
- valor_venta (NUMERIC)
  
Parte A – SQL:

Escribe los queries para:

1. Total de ventas por cliente:
   SELECT cliente_id SUM(valor_venta) AS total_ventas
   FROM project.dataset.ventas_diarias
   GROUP BY cliente_id
   ORDER BY total_ventas DESC
   
2. Total de ventas por mes
   SELECT EXTRACT( YEAR FROM fecha) AS anio
                 ( MONTH FROM fecha) AS mes
   SUM(valor_venta) AS total_ventas
   FROM project.dataser,ventas_diarias
   GROUP BY anio, mes
   ORDER BY anio, mes   
   
3. Top 5 clientes por ventas
   SELECT cliente_id, SUM(valor_venta) AS total_venta
   FROM project.dataser,ventas_diarias
   GROUP BY cliente_id
   ORDER BY total_ventas DESC
   LIMIT 5;

   
Parte B – Conceptual:

Explica brevemente cómo consumirías estos datos desde una aplicación Django y cómo los
presentarías en el frontend.

Se configuraria settings.py con la DB project.dataser,ventas_diarias y pensaria que definiendo los modelos ventas diarias y en views.py se crearia un función para consultar datos y con HTML y JavaScript mostrar lo resultados con gráficos de barras, lineas o circulares.


BLOQUE 3

1. ¿Cómo abordarías un requerimiento técnicamente incorrecto solicitado por un cliente?
   Bueno yo creeria que primero asegurarse que realmente sea técnicamente incorrecto,
   es decir plantearlo con el equipo de trabajo y cuando se llegue a esa conclución se le expliaria
   al cliente con claridad y respeto los motivos o los riesgo que tendría el requerimiento, ademas
   como se hablo anteriormente con el equipo de trabajo de pronto se haya podido encontrar
   una alternativa o proponer un solución práctica.
2. ¿Qué harías si debes trabajar con una tecnología que no dominas y el proyecto ya inició?
   Yo creeria que lo mejor es dejar claro mis capacidades si no domino una tecnología lo mejor es
   decirlo desde un principio cuando aun hay tiempo de ver alternativas, pondria mi disposición y
   habilidad de aprender rapido para poder apoyar lo mejor posible.
3. ¿Cómo aseguras calidad técnica cuando trabajas bajo presión de tiempo?
   Pienso que la comunicación en el equipo es clave cuando hay presión de tiempo ya que si se
   tiene buena comunicacíon se pueden identificar o priorizar tareas optimizando tiempos.



