# Panel de control web para análisis exploratorio de datos



## Descripción del proyecto

Este proyecto consiste en el desarrollo y despliegue de una aplicación web interactiva para el análisis exploratorio de datos (EDA), construida con Python y Streamlit, y desplegada en la nube mediante Render. El objetivo principal es aplicar buenas prácticas de ingeniería de software, incluyendo la gestión de entornos virtuales, control de versiones con GitHub y el despliegue continuo de una aplicación web funcional.

La aplicación permite visualizar de forma interactiva un conjunto de datos en formato CSV —por defecto, anuncios de venta de coches— mediante gráficos dinámicos creados con Plotly. Aunque se proporciona un dataset base, la aplicación es flexible y puede adaptarse fácilmente para trabajar con otros conjuntos de datos similares.

Este proyecto no se centra en el análisis profundo de los datos, sino en el flujo completo de desarrollo: desde la exploración inicial en notebooks, pasando por la construcción de un dashboard web, hasta su publicación en un entorno productivo en la nube.


## Funcionalidad principal

La aplicación web ofrece las siguientes funcionalidades:

* Carga de un conjunto de datos desde un archivo CSV.

* Visualización interactiva de los datos mediante:

    * Histogramas.
    * Gráficos de dispersión.

* Interacción del usuario a través de botones o casillas de verificación para generar los gráficos bajo demanda.

* Interfaz web simple e intuitiva accesible desde un navegador.


## Tecnologías utilizadas

* Python como lenguaje principal.

* pandas para la manipulación y carga de datos.

* plotly para la creación de gráficos interactivos.

* streamlit para el desarrollo de la aplicación web.

* Jupyter Notebook para el análisis exploratorio inicial.

* Git y GitHub para control de versiones.

* Render para el despliegue de la aplicación en la nube.



## Estructura del proyecto

El proyecto sigue una estructura clara y organizada:

* app.py: archivo principal de la aplicación Streamlit.

* 'DB/vehicles_us.csv': conjunto de datos en formato CSV.

* requirements.txt: lista de dependencias del proyecto.

* notebooks/EDA.ipynb: notebook para el análisis exploratorio de datos.

* README.md: documentación del proyecto.


## Ejecución local

Para ejecutar la aplicación de forma local, es necesario:

1. Crear y activar un entorno virtual de Python.

2. Instalar las dependencias listadas en requirements.txt.

3. Ejecutar el comando streamlit run app.py desde la raíz del proyecto.

4. Abrir la aplicación en el navegador usando la URL local proporcionada por Streamlit.


## Despliegue

La versión final de la aplicación está desplegada en Render y es accesible a través de un navegador web. El proceso de despliegue se realiza directamente desde un repositorio público de GitHub y utiliza comandos de construcción e inicio configurados para instalar dependencias y lanzar la aplicación con Streamlit.


## Objetivo del proyecto

Este proyecto tiene como finalidad reforzar habilidades clave de la ingeniería de software orientada a datos, demostrando la capacidad de construir, documentar y desplegar una aplicación web completa. Además, sirve como ejemplo práctico de integración entre análisis de datos y desarrollo de aplicaciones, aportando valor como proyecto demostrativo para fines académicos y profesionales.
