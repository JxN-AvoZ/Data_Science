# Predicción de demanda de taxis – Sweet Lift Taxi

## Descripción del proyecto

La compañía **Sweet Lift Taxi** ha recopilado datos históricos sobre pedidos de taxis en
aeropuertos. Con el objetivo de optimizar la disponibilidad de conductores durante horas pico,
se requiere construir un modelo de machine learning capaz de predecir la cantidad de pedidos
de taxis para la próxima hora.

Este proyecto aborda un problema real de predicción de demanda utilizando series temporales,
permitiendo mejorar la toma de decisiones operativas y la asignación de recursos.

---

## Objetivo

Desarrollar un modelo predictivo que estime el número de pedidos de taxis por hora,
cumpliendo con la siguiente condición:

\begin{equation}
\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)^2} \leq 48
\end{equation}

---

## Metodología

### 1. Preprocesamiento de datos
- Conversión de la columna de fecha a formato `datetime`
- Establecimiento del índice temporal
- Remuestreo de los datos a intervalos de 1 hora
- Verificación de valores faltantes

### 2. Análisis exploratorio (EDA)
- Visualización de la serie temporal
- Identificación de:
  - Tendencias
  - Estacionalidad
  - Comportamientos cíclicos
- Análisis de distribución de la demanda

### 3. Ingeniería de características
Creación de variables basadas en el tiempo:
- Hora del día
- Día de la semana
- Lags (valores pasados)
- Medias móviles

### 4. Entrenamiento de modelos
Se entrenaron distintos modelos de machine learning:

| Modelo | Tipo |
|---|---|
| Regresión lineal | Baseline |
| Árbol de decisión | — |
| Bosque aleatorio | — |
| Modelos de boosting | — |

Se realizó ajuste de hiperparámetros para mejorar el rendimiento.

### 5. Evaluación

**División de datos:**

| Conjunto | Proporción |
|---|---|
| Entrenamiento | 90% |
| Prueba | 10% |

**Métrica utilizada:** RMSE

Se seleccionó el modelo con mejor desempeño en el conjunto de validación y se evaluó
en el conjunto de prueba.

---

## Resultados

- Se entrenó un modelo capaz de predecir la demanda horaria de taxis.
- El modelo final cumple con el criterio establecido: $\text{RMSE} \leq 48$.
- Se identificaron patrones claros de demanda en función del tiempo (horas pico y variaciones semanales).

---

## Conclusiones

- La demanda de taxis presenta patrones temporales claros que pueden ser aprovechados mediante modelos predictivos.
- La ingeniería de características (lags y variables temporales) es clave para mejorar el rendimiento del modelo.
- Esta solución puede implementarse en sistemas reales para optimizar la asignación de conductores.

---

## Tecnologías utilizadas

| Herramienta | Uso |
|---|---|
| `Python` | Lenguaje principal |
| `pandas` | Manipulación de datos |
| `numpy` | Operaciones numéricas |
| `matplotlib` | Visualización |
| `scikit-learn` | Modelado ML |
