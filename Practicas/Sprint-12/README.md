# Selección de regiones petroleras para nuevos pozos – OilyGiant

## Descripción del proyecto

La compañía de extracción de petróleo **OilyGiant** busca identificar las regiones más rentables para desarrollar **200 nuevos pozos petroleros**. Para apoyar esta decisión estratégica, se desarrolló un análisis basado en **modelos de regresión y simulaciones estadísticas** que permiten estimar el volumen de reservas de petróleo y evaluar el riesgo financiero de cada región.

El objetivo principal del proyecto es **predecir el volumen de reservas en nuevos pozos y seleccionar la región con el mayor beneficio esperado**, considerando tanto la rentabilidad como el riesgo de pérdidas.

Para ello se analizan **tres regiones potenciales**, utilizando modelos de **regresión lineal** y la técnica de **bootstrapping** para estimar la distribución de ganancias y el riesgo asociado a la inversión.

---

## Objetivos

* Analizar datos de exploración geológica de tres regiones.
* Construir modelos de **regresión lineal** para predecir el volumen de reservas.
* Evaluar la calidad de los modelos mediante métricas como **RMSE**.
* Estimar el beneficio potencial de los 200 pozos con mayor producción esperada.
* Analizar el **riesgo financiero utilizando bootstrapping**.
* Seleccionar la región con el **mayor beneficio esperado y riesgo de pérdidas inferior al 2.5%**.

---

## Dataset

Se utilizan tres datasets correspondientes a diferentes regiones de exploración:

```
/datasets/geo_data_0.csv
/datasets/geo_data_1.csv
/datasets/geo_data_2.csv
```

Cada fila representa un pozo petrolero potencial.

### Diccionario de datos

| Columna | Descripción                                         |
| ------- | --------------------------------------------------- |
| id      | Identificador único del pozo                        |
| f0      | Característica geológica                            |
| f1      | Característica geológica                            |
| f2      | Característica geológica                            |
| product | Volumen de reservas de petróleo (miles de barriles) |

Los datos son **sintéticos**, por lo que los detalles reales de los pozos y contratos no se publican.

---

## Condiciones del proyecto

* Se utiliza **regresión lineal** como único modelo de predicción.
* Se estudian **500 pozos por región**, seleccionando los **200 con mayor producción estimada**.
* Presupuesto total: **100 millones de dólares**.
* Ingreso por unidad de producto: **$4500 USD**.
* Para evitar pérdidas, cada pozo debe producir al menos **111.1 unidades de reservas**.
* Solo se seleccionarán regiones con **riesgo de pérdidas menor al 2.5%**.

---

## Metodología

El proyecto se desarrolló siguiendo las siguientes etapas:

### 1. Preparación de los datos

* Carga de los datasets de las tres regiones
* Análisis exploratorio
* Separación de variables predictoras y variable objetivo
* División de datos en conjuntos de **entrenamiento (75%) y validación (25%)**

---

### 2. Entrenamiento del modelo

Se entrenó un **modelo de regresión lineal** para cada región.

Para cada modelo se calcularon:

* Predicciones en el conjunto de validación
* Volumen promedio de reservas predicho
* Error cuadrático medio (**RMSE**)

Esto permitió comparar el desempeño del modelo en cada región.

---

### 3. Cálculo de beneficios potenciales

Se desarrolló una función para calcular la ganancia basada en:

* Selección de los **200 pozos con mayor predicción de reservas**
* Cálculo del volumen total de reservas
* Conversión del volumen a ingresos estimados
* Comparación con el presupuesto total de inversión

---

### 4. Análisis de riesgo con Bootstrapping

Para estimar la incertidumbre en las ganancias se aplicó **bootstrapping con 1000 muestras**.

Para cada región se calcularon:

* Beneficio promedio esperado
* Intervalo de confianza del **95%**
* Probabilidad de pérdidas

Esto permitió evaluar la **viabilidad financiera de cada región**.

---

## Resultados

El análisis permitió:

* Identificar la región con **mayor beneficio esperado**.
* Evaluar el **riesgo de pérdidas** en cada región.
* Seleccionar únicamente regiones con **riesgo menor al 2.5%**.

La región final recomendada es aquella que **maximiza el beneficio promedio manteniendo el riesgo dentro de los límites aceptables**.

---

## Tecnologías utilizadas

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Bootstrapping
* Jupyter Notebook

---

## Conclusiones

Este proyecto demuestra cómo combinar **modelos predictivos y análisis estadístico** para apoyar decisiones de inversión en proyectos de gran escala.

El uso de **regresión lineal para predicción de reservas** junto con **bootstrapping para estimación de riesgo** permite evaluar no solo el beneficio esperado, sino también la incertidumbre asociada a la inversión.

Este tipo de análisis es ampliamente utilizado en industrias como:

* energía
* minería
* exploración geológica
* finanzas de proyectos
