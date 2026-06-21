# Sprint 19 - Proyecto Final

# Predicción de Cancelación de Clientes (Churn) – Interconnect

## Descripción del proyecto

La empresa de telecomunicaciones **Interconnect** busca reducir la pérdida de clientes mediante el uso de técnicas de **Machine Learning**.

El objetivo del proyecto consiste en desarrollar un modelo capaz de predecir qué clientes tienen mayor probabilidad de cancelar sus servicios (**churn**) para que el área de marketing pueda implementar estrategias de retención, tales como promociones personalizadas o planes especiales.

Para ello, se integraron múltiples fuentes de información relacionadas con contratos, servicios contratados, datos personales y características de los servicios de telefonía e internet.

---

## Objetivo

Construir un modelo predictivo capaz de identificar clientes con alta probabilidad de abandonar la compañía, maximizando el desempeño del modelo y proporcionando información útil para la toma de decisiones de negocio.

---

## Descripción de los datos

Los datos se obtuvieron a partir de cuatro archivos diferentes:

### `contract.csv`

Información relacionada con los contratos de los clientes:

* Tipo de contrato.
* Método de pago.
* Facturación mensual.
* Facturación total.
* Fecha de inicio del contrato.
* Facturación electrónica.

### `personal.csv`

Información demográfica de los clientes:

* Género.
* Estado civil.
* Dependientes.

### `internet.csv`

Información sobre los servicios de internet contratados:

* Tipo de conexión (_DSL/Fibra óptica_).
* Seguridad en línea.
* Antivirus.
* Backup en la nube.
* Soporte técnico.
* Servicios de streaming.

### `phone.csv`

Información relacionada con servicios telefónicos:

* Servicio telefónico.
* Líneas múltiples.

Cada cliente se identifica mediante la variable:

* `customerID`

---

## Tecnologías utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* LightGBM / CatBoost / XGBoost
* Machine Learning

---

## Metodología

### 1. Integración y preparación de datos

Se realizó la unión de las diferentes tablas utilizando la variable `customerID` como clave principal.

Las principales tareas de preparación incluyeron:

* Unión de múltiples fuentes de datos.
* Tratamiento de valores ausentes.
* Conversión de tipos de datos.
* Codificación de variables categóricas.
* Creación de nuevas características.
* Análisis exploratorio de datos.

---

### 2. Análisis Exploratorio (EDA)

Se analizaron distintos factores asociados a la cancelación de clientes, incluyendo:

* Tipo de contrato.
* Antigüedad del cliente.
* Cargos mensuales y totales.
* Método de pago.
* Tipo de servicio de internet.
* Servicios adicionales contratados.

El análisis permitió identificar patrones asociados con una mayor probabilidad de abandono.

---

### 3. Ingeniería de características

Se generaron nuevas variables para mejorar el desempeño del modelo, tales como:

* Tiempo de permanencia del cliente.
* Número total de servicios contratados.
* Agrupaciones de planes y métodos de pago.
* Variables derivadas de la antigüedad del contrato.

---

### 4. Entrenamiento de modelos

Se entrenaron y compararon distintos algoritmos de clasificación:

* Regresión Logística.
* Árbol de Decisión.
* Random Forest.
* Gradient Boosting.
* LightGBM.
* CatBoost.
* XGBoost.

Para cada modelo se realizaron ajustes de hiperparámetros y validación cruzada.

---

### 5. Evaluación del modelo

El rendimiento se evaluó utilizando métricas orientadas a clasificación:

* Accuracy.
* Precision.
* Recall.
* F1-score.
* ROC-AUC.

Se seleccionó el modelo con el mejor equilibrio entre capacidad predictiva y generalización.

---

## Resultados

El modelo final permitió identificar clientes con alto riesgo de cancelación, proporcionando una herramienta útil para diseñar campañas de retención y reducir pérdidas económicas.

Las variables más relevantes para la predicción fueron:

* Tipo de contrato.
* Antigüedad del cliente.
* Cargo mensual.
* Tipo de conexión a internet.
* Método de pago.
* Cantidad de servicios contratados.

---

## Conclusiones

* Los clientes con contratos mensuales presentan una mayor probabilidad de abandono que aquellos con contratos de largo plazo.
* Los usuarios con conexión de fibra óptica y mayores cargos mensuales muestran tasas de cancelación más elevadas.
* La permanencia del cliente es uno de los factores más importantes para predecir el churn.
* Los modelos basados en técnicas de boosting mostraron el mejor desempeño predictivo.
* La implementación de modelos predictivos permite identificar clientes en riesgo y diseñar estrategias de retención de manera proactiva.

---

## Valor de negocio

La solución desarrollada permite:

* Reducir la pérdida de clientes.
* Optimizar campañas de marketing.
* Incrementar la retención de usuarios.
* Disminuir costos asociados a la adquisición de nuevos clientes.
* Mejorar la rentabilidad del negocio.

---

## Competencias demostradas

* Integración de múltiples fuentes de datos.
* Ingeniería de características.
* Análisis exploratorio de datos (_EDA_).
* Machine Learning supervisado.
* Clasificación binaria.
* Ajuste de hiperparámetros.
* Evaluación de modelos.
* Interpretación de resultados.
* Toma de decisiones basada en datos.
