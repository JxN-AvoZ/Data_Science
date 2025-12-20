# Análisis y limpieza de datos de compras en Instacart


## Descripción del proyecto

En este proyecto se trabaja con __datos reales de Instacart__, una plataforma de entregas de comestibles similar a Uber Eats y DoorDash, donde los clientes pueden realizar pedidos de supermercado y recibirlos a domicilio. El conjunto de datos original fue publicado por Instacart en 2017 como parte de una competición en Kaggle, y posteriormente adaptado para fines educativos.

La versión utilizada en este proyecto es una __muestra modificada del dataset original__, reducida en tamaño para facilitar el procesamiento y enriquecida intencionalmente con __valores ausentes y duplicados__, manteniendo las distribuciones originales de los datos. Esto permite simular un escenario realista de trabajo con datos imperfectos.

El objetivo principal del proyecto es __limpiar, preparar y analizar los datos__, y posteriormente elaborar un informe que brinde información relevante sobre los __hábitos de compra de los clientes de Instacart__, apoyándose tanto en análisis descriptivo como en visualizaciones claras y bien documentadas.


## Objetivo

Preparar un conjunto de datos confiable a partir de múltiples tablas relacionadas y realizar un análisis exploratorio que permita comprender cómo compran los clientes de Instacart, cuándo realizan sus pedidos y qué productos adquieren con mayor frecuencia.


## Alcance del proyecto

El proyecto abarca tres grandes fases:

### Exploración inicial de los datos

* Carga y revisión general de cinco tablas relacionadas.

* Comprensión de la estructura, tamaño y contenido de cada conjunto de datos.

* Identificación preliminar de posibles problemas de calidad de datos.

### Preprocesamiento de datos

En esta etapa se realiza un trabajo exhaustivo de limpieza, que incluye:

* Verificación y corrección de tipos de datos (especialmente columnas de identificadores).

* Identificación y tratamiento de valores ausentes.

* Detección y eliminación de registros duplicados.

* Documentación de las decisiones tomadas y justificación de los métodos utilizados.

* Análisis de las posibles causas de valores faltantes y duplicados en los datos.

El objetivo es garantizar la consistencia y confiabilidad de los datos antes del análisis.

### Análisis exploratorio de datos

Con los datos ya procesados, se lleva a cabo un análisis detallado que responde a preguntas clave sobre el comportamiento de compra, incluyendo:

* Patrones de pedidos según la hora del día y el día de la semana.

* Tiempo de espera entre pedidos consecutivos.

* Diferencias en los hábitos de compra entre distintos días.

* Distribución del número de pedidos por cliente.

* Identificación de los productos más comprados y más frecuentemente reordenados.

* Análisis del número de artículos por pedido.

* Evaluación de la proporción de productos reordenados tanto a nivel de producto como de cliente.

* Identificación de los artículos que suelen añadirse primero al carrito.

Los resultados se apoyan en __gráficos claros y bien etiquetados__, diseñados para comunicar de forma efectiva los hallazgos.


## Datos utilizados

El análisis se realiza utilizando cinco tablas principales:

* `instacart_orders`: información general de cada pedido.

* `products`: catálogo de productos disponibles.

* `order_products`: relación entre pedidos y productos.

* `aisles`: categorías de pasillos de los productos.

* `departments`: departamentos de los productos.

El uso conjunto de estas tablas permite construir una visión completa del comportamiento de compra de los clientes.


## Resultado esperado

Al finalizar el proyecto se obtiene:

* Un conjunto de datos limpio, consistente y listo para análisis.

* Un informe analítico bien documentado en un Jupyter Notebook.

* Visualizaciones que describen claramente los hábitos de compra de los clientes.

* Insights clave sobre productos, frecuencia de pedidos y comportamiento de recompra.


## Conclusiones

Este proyecto reproduce un escenario real de análisis de datos en el que es necesario combinar múltiples fuentes, resolver problemas de calidad de datos y extraer conclusiones relevantes para el negocio. El resultado final proporciona una comprensión sólida del comportamiento de los clientes de Instacart y sirve como base para la toma de decisiones estratégicas y análisis más avanzados en el futuro.