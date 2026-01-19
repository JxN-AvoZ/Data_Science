# Análisis de viajes en taxi y clima en Chicago – Zuber


## Descripción del proyecto

En este proyecto actúo como analista de datos para Zuber, una nueva empresa de viajes compartidos que busca ingresar al mercado de Chicago. El objetivo principal es identificar patrones en los viajes en taxi, comprender las preferencias de los pasajeros y evaluar cómo los factores externos, especialmente el clima, influyen en la frecuencia y duración de los viajes.

Para lograrlo, se analiza una base de datos relacional con información de viajes, taxis, barrios y condiciones meteorológicas, combinando consultas SQL, análisis exploratorio en Python y pruebas estadísticas de hipótesis.


## Objetivos

* Analizar el comportamiento de los viajes en taxi en Chicago.

* Identificar las empresas de taxis más populares.

* Explorar la distribución de viajes por barrios.

* Evaluar el impacto de las condiciones climáticas en la duración de los viajes.

* Probar una hipótesis estadística relacionada con el clima y los viajes.


## Descripción de los datos

La base de datos contiene las siguientes tablas:

**neighborhoods**

Información sobre los barrios de Chicago:

* `name`: nombre del barrio
* `neighborhood_id`: identificador del barrio

**cabs**

Información sobre los taxis:

* `cab_id`: identificador del taxi
* `vehicle_id`: ID técnico del vehículo
* `company_name`: empresa propietaria del taxi

**trips**

Información sobre los viajes:

* `trip_id`: identificador del viaje
* `cab_id`: identificador del taxi
* `start_ts`: fecha y hora de inicio del viaje
* `end_ts`: fecha y hora de finalización
* `duration_seconds`: duración del viaje en segundos
* distance_miles`: distancia recorrida en millas
* `pickup_location_id`: barrio de inicio
* `dropoff_location_id`: barrio de destino

**weather_records**

Información meteorológica:

* `record_id`: identificador del registro
* `ts`: fecha y hora del registro
* `temperature`: temperatura
* `description`: descripción del clima (ej. lluvia, tormenta, nubes)

__*No existe una relación directa entre `trips` y `weather_records`, por lo que se vinculan utilizando la hora de inicio del viaje (`start_ts`) y la hora del registro meteorológico (`ts`).__*


## Metodología y etapas del proyecto

### Paso 1. Obtención de datos climáticos

Análisis de datos meteorológicos de Chicago en noviembre de 2017 a partir de una fuente web externa.

### Paso 2. Análisis exploratorio de datos (SQL)

Número de viajes por empresa de taxis (15–16 de noviembre de 2017).

Viajes de empresas cuyo nombre contiene “*Yellow*” o “*Blue*” (1–7 de noviembre de 2017).

Comparación entre las empresas más populares (Flash Cab y Taxi Affiliation Services) frente al resto agrupado como __Other__.

### Paso 3. Prueba de hipótesis (SQL)

Identificación de los barrios Loop y Aeropuerto Internacional O’Hare.

Clasificación del clima en condiciones __Good__ y __Bad__ usando expresiones `CASE`.

Extracción de viajes realizados los sábados desde Loop hasta O’Hare.

Integración de duración del viaje y condiciones climáticas, excluyendo registros sin información meteorológica.

### Paso 4. Análisis exploratorio de datos (Python)__

Análisis de archivos CSV resultantes de consultas SQL:

`"project_sql_result_01.csv"`: viajes por empresa de taxis.

`"project_sql_result_04.csv"`: promedio de viajes finalizados por barrio.

Incluye:

* Importación y validación de datos.
* Identificación de los 10 barrios con más viajes finalizados.
* Visualizaciones:
    * Número de viajes por empresa.
    * Top 10 barrios por finalización de viajes.
* Interpretación de resultados basada en los gráficos.

### Paso 5. Prueba de hipótesis (Python)

Archivo:

`"project_sql_result_07.csv"`: viajes desde Loop hasta O’Hare con condiciones climáticas y duración.

__Hipótesis evaluada:__

_**“La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O’Hare cambia los sábados lluviosos.”**_

Incluye:

* Planteamiento de hipótesis nula y alternativa.
* Selección del nivel de significancia (α).
* Elección y justificación del método estadístico.
* Conclusión basada en el valor p.


### Tecnologías utilizadas

* __SQL__ (JOIN, GROUP BY, CASE, filtros temporales)
* __Python__
    * pandas 
    * matplotlib / seaborn
    * scipy (pruebas estadísticas)
* Jupyter Notebook