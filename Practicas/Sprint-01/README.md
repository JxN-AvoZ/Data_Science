# Preparación y limpieza de datos para el Programa de Fidelización de Store 1


## Descripción del proyecto

Este proyecto se centra en la preparación y transformación de datos de clientes para la empresa de comercio electrónico __Store 1__, la cual se encuentra en la fase inicial del lanzamiento de un nuevo __Programa de Fidelización de Clientes__. Antes de diseñar campañas personalizadas y optimizar futuras estrategias de marketing, la empresa necesita asegurarse de que su base de datos de clientes sea consistente, limpia y esté correctamente estructurada para el análisis.

Como parte del equipo de análisis, el objetivo principal de este proyecto es revisar una muestra de los datos existentes y realizar las transformaciones necesarias para dejarlos listos para etapas posteriores de análisis y generación de indicadores de negocio (KPIs).

Este proyecto corresponde a la primera fase del trabajo. En el siguiente sprint se llevará a cabo un análisis más profundo que responderá directamente a las preguntas de negocio del cliente.


## Objetivo

El objetivo de esta etapa es preparar los datos de clientes para facilitar su segmentación y análisis, permitiendo a Store 1 comprender mejor el comportamiento de sus usuarios y sentar las bases para un programa de fidelización efectivo.


## Alcance del proyecto

Durante esta fase se realizan las siguientes tareas:

* Limpieza de los perfiles de clientes.

* Estandarización de nombres de usuario y edades.

* Validación de la consistencia de los datos.

* Corrección de errores e inconsistencias detectadas.

* Cálculo del gasto total por cliente a partir de su gasto por categoría.

* Preparación de los datos para su uso en análisis posteriores y generación de KPIs.

El proyecto se enfoca en la calidad y estructura de los datos, más que en la interpretación final de los resultados.


## Descripción de los datos

Los datos proporcionados por Store 1 se presentan en forma de una lista de Python, donde cada registro representa a un cliente. Cada cliente contiene la siguiente información:

* `usuario_id`: Identificador único del usuario.

* `usuario_nombre`: Nombre del cliente (con posibles inconsistencias de formato).

* `usuario_edad`: Edad del cliente.

* `categorias_fav_low`: Lista de categorías de productos comprados por el usuario.

* `gasto_por_categoria`: Lista de valores enteros que representan el gasto total en cada categoría correspondiente.

Estos datos requieren normalización y validación antes de poder ser utilizados en análisis más avanzados.


## Resultado esperado

Al finalizar este proyecto, se obtiene un conjunto de datos limpio, consistente y estructurado, listo para:

* Segmentar clientes por edad, comportamiento de compra y categorías.

* Calcular métricas clave relacionadas con el gasto de los usuarios.

* Servir como base para el análisis completo que se desarrollará en el siguiente sprint.