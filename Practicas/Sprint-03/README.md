# Análisis de hábitos de escucha en plataformas de música online


## Descripción del proyecto

En este proyecto se analizan __datos reales de transmisión de música online__ con el objetivo de explorar y comprender los hábitos de escucha de los usuarios y las usuarias en dos ciudades distintas: __Springfield__ y __Shelbyville__. A partir de esta información, se busca identificar patrones de comportamiento relacionados con el consumo musical y evaluar si existen diferencias significativas según la ciudad y el día de la semana.

El trabajo se desarrolla dentro de un cuaderno de Jupyter proporcionado como plantilla, en el cual se implementa el código necesario y se documentan los hallazgos mediante celdas Markdown. El enfoque del proyecto combina análisis exploratorio, limpieza de datos y análisis comparativo, siguiendo una estructura guiada y progresiva.


## Objetivo

Explorar, limpiar y analizar los datos de reproducción musical para determinar si la actividad de escucha varía en función de la ciudad y del día de la semana, apoyándose en un proceso estructurado de análisis de datos.


## Etapas del proyecto

El proyecto se divide en tres etapas principales:

### Etapa 1: Descripción de los datos

En esta fase se realiza una primera exploración del conjunto de datos, revisando su estructura general, las columnas disponibles y el tipo de información que contienen. Se documentan observaciones iniciales sobre la calidad y características de los datos.

### Etapa 2: Preprocesamiento de datos

En esta etapa se lleva a cabo la limpieza de los datos, incluyendo:

* Revisión y estandarización de los nombres de las columnas.

* Identificación y tratamiento de valores duplicados.

* Detección y manejo de valores ausentes.

* Documentación de los cambios realizados y sus implicaciones.

El objetivo es garantizar que el conjunto de datos esté en condiciones adecuadas para un análisis confiable.

### Etapa 3: Análisis

Esta es la etapa central del proyecto. En ella se analizan los hábitos de escucha para evaluar:

* Diferencias en la actividad de reproducción entre Springfield y Shelbyville.

* Variaciones en el comportamiento de los usuarios según el día de la semana.

* Patrones generales de consumo musical a partir de los datos procesados.

Cada hipótesis o afirmación se prueba mediante código y los resultados se interpretan y documentan en las secciones correspondientes del cuaderno.


## Datos utilizados

El conjunto de datos se encuentra en el archivo music_project_en.csv y contiene información detallada sobre las reproducciones de música. Las columnas incluidas son:

* `userID`: identificador único de cada usuario o usuaria.

* `track`: título de la canción reproducida.

* `artist`: nombre del artista.

* `genre`: género musical.

* `city`: ciudad del usuario o la usuaria.

* `time`: hora de reproducción (formato HH:MM:SS).

* `Day`: día de la semana.


## Resultado esperado

Al finalizar el proyecto, se obtiene un análisis claro y bien documentado que permite comprender cómo varían los hábitos de escucha entre diferentes ciudades y días, así como conclusiones fundamentadas en datos que resumen los principales hallazgos del estudio.


## Conclusiones

El proyecto concluye con una síntesis de los resultados obtenidos en todas las etapas, destacando los patrones más relevantes y proporcionando una visión general del comportamiento de los usuarios en la plataforma de música online.