# Recuperación de oro – Modelado predictivo del proceso de refinamiento

## Descripción del proyecto

En este proyecto se desarrolla un modelo de machine learning para predecir la eficiencia en el proceso de recuperación de oro a partir de datos industriales reales.

El objetivo es analizar y modelar las diferentes etapas del proceso de refinamiento (rougher y final), identificando patrones en los datos que permitan estimar métricas clave de recuperación de minerales. Este tipo de problema es representativo de aplicaciones reales en la industria minera, donde optimizar la recuperación impacta directamente en la rentabilidad.

El proyecto incluye validación de datos, análisis exploratorio, tratamiento de características faltantes y entrenamiento de modelos predictivos con evaluación mediante métricas especializadas.

---

## Objetivos

- Validar la calidad de los datos y verificar cálculos clave del proceso.
- Analizar la evolución de la concentración de metales (Au, Ag, Pb).
- Detectar y tratar valores atípicos.
- Construir modelos predictivos para estimar la recuperación de oro.
- Evaluar modelos utilizando la métrica **sMAPE**.

---

## Dataset

Se utilizan tres conjuntos de datos:

- `gold_recovery_train.csv` — datos de entrenamiento
- `gold_recovery_test.csv` — datos de prueba (sin variable objetivo)
- `gold_recovery_full.csv` — dataset completo con todas las variables

### Características importantes

- Los datos están indexados por fecha y hora.
- Algunas variables del entrenamiento **no están disponibles en el test**.
- Existen variables calculadas posteriormente al proceso (data leakage potencial).
- El dataset incluye múltiples etapas del proceso de refinamiento.

---

## Etapas del proyecto

### 1. Preparación de datos

- Carga y exploración inicial de los datasets.
- Validación del cálculo de recuperación (`rougher.output.recovery`).
- Identificación de variables ausentes en el conjunto de prueba.
- Limpieza y preprocesamiento de datos.

---

### 2. Análisis exploratorio de datos (EDA)

- Análisis de la concentración de metales (Au, Ag, Pb) por etapa.
- Comparación de distribuciones entre train y test.
- Evaluación del tamaño de partículas.
- Detección y eliminación de valores atípicos.
- Análisis de concentraciones totales en distintas fases del proceso.

---

### 3. Modelado

- Implementación de la métrica personalizada **sMAPE**.
- Entrenamiento de múltiples modelos de regresión.
- Evaluación mediante **validación cruzada**.
- Selección del mejor modelo.
- Evaluación final con el conjunto de prueba.

---

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter Notebook

---

## Resultados

- Se validó correctamente el cálculo de recuperación.
- Se identificaron variables no disponibles en el conjunto de prueba (evitando data leakage).
- Se eliminaron valores atípicos que afectaban la distribución de los datos.
- Se entrenaron múltiples modelos y se seleccionó el mejor en función de **sMAPE**.
- El modelo final logra una predicción confiable del proceso de recuperación de oro.

---

## Enfoque principal

Machine learning aplicado a procesos industriales, validación de datos, manejo de datasets incompletos y optimización de modelos con métricas personalizadas.

---
