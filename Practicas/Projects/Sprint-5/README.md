# Análisis de ingresos por tarifas prepago en Megaline


## Descripción del proyecto

En este proyecto se realiza un __análisis preliminar de datos para el operador de telecomunicaciones Megaline__, cuyo objetivo es determinar cuál de sus dos tarifas de prepago —__Surf__ o __Ultimate__— genera mayores ingresos en promedio. Esta información es clave para que el departamento comercial pueda __optimizar el presupuesto de publicidad__ y enfocar sus esfuerzos en el plan más rentable.

El análisis se basa en una muestra de __500 clientes__, e incluye información demográfica, la tarifa contratada y el uso real de los servicios durante el año 2018, como llamadas, mensajes de texto y consumo de datos móviles. A partir de estos datos, se estudia el comportamiento de los clientes y se calculan los ingresos generados por cada plan.

El proyecto culmina con la aplicación de __pruebas estadísticas__, que permiten evaluar si las diferencias observadas en los ingresos promedio entre ambas tarifas son estadísticamente significativas.


## Objetivo

Analizar el comportamiento de los clientes de Megaline y determinar qué tarifa de prepago —Surf o Ultimate— genera más ingresos en promedio, apoyándose en cálculos de consumo, facturación mensual y pruebas estadísticas.


## Contexto del negocio

Megaline aplica reglas específicas de facturación que influyen directamente en los ingresos:

* Las llamadas se redondean individualmente a minutos completos.

* Los datos móviles se acumulan mensualmente y se redondean hacia arriba a gigabytes completos.

* Los cargos adicionales se aplican únicamente cuando el cliente excede los límites incluidos en su plan.

Comprender estas reglas es fundamental para calcular correctamente los ingresos reales generados por cada usuario.


## Alcance del proyecto

El proyecto abarca las siguientes actividades principales:

* Exploración y limpieza de múltiples tablas relacionadas.

* Análisis del consumo mensual de llamadas, mensajes y datos por usuario.

* Cálculo del ingreso mensual por cliente según su tarifa.

* Comparación de los ingresos promedio entre los planes Surf y Ultimate.

* Aplicación de pruebas estadísticas para validar las conclusiones.

* Interpretación de los resultados desde una perspectiva de negocio.


## Tarifas analizadas

__Surf__

* Pago mensual: $20

* Incluye 500 minutos, 50 SMS y 15 GB

* Cargos extra por excedente:

    * Minutos: $0.03

    * SMS: $0.03

    * Datos: $10 por GB

__Ultimate__

* Pago mensual: $70

* Incluye 3000 minutos, 1000 SMS y 30 GB

* Cargos extra por excedente:

    * Minutos: $0.01

    * SMS: $0.01

    * Datos: $7 por GB


## Datos utilizados

El análisis se realiza a partir de cinco tablas principales:

* `users`: información demográfica y de suscripción de los clientes.

* `calls`: registros de llamadas realizadas.

* `messages`: registros de mensajes enviados.

* `internet`: consumo de datos por sesión.

* `plans`: características y costos de las tarifas.

La combinación de estas tablas permite construir una visión completa del uso y la facturación de cada cliente.


## Resultado esperado

Al finalizar el proyecto se obtiene:

* Un análisis claro del comportamiento de los clientes según su tarifa.

* El cálculo del ingreso promedio generado por cada plan.

* Una conclusión basada en evidencia estadística sobre cuál tarifa es más rentable.

* Recomendaciones útiles para la toma de decisiones del área comercial.


## Conclusiones

Este proyecto reproduce un escenario real de análisis de datos en telecomunicaciones, donde es necesario integrar múltiples fuentes, aplicar reglas de negocio específicas y utilizar herramientas estadísticas para respaldar decisiones estratégicas. El resultado final proporciona a Megaline una base sólida para ajustar su estrategia de marketing y maximizar sus ingresos.