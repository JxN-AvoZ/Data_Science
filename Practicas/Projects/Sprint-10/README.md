# Modelo de Clasificación para Recomendación de Planes (Megaline)

## Descripción del proyecto

La compañía de telecomunicaciones **Megaline** busca incentivar a sus clientes a migrar de planes heredados hacia sus nuevos planes **Smart** y **Ultra**. Para apoyar esta decisión, se requiere desarrollar un **modelo de machine learning** capaz de analizar el comportamiento de los usuarios y recomendar el plan más adecuado.

El objetivo del proyecto es construir un **modelo de clasificación** que determine qué plan debería utilizar un cliente basándose en su comportamiento mensual de uso del servicio.

Para aprobar el proyecto, el modelo debe alcanzar un **nivel mínimo de exactitud (accuracy) de 0.75**.

Este proyecto forma parte del proceso de formación en **Data Science** y se enfoca en la construcción, evaluación y validación de modelos de clasificación.

---

## Objetivos

- Analizar el dataset de comportamiento de usuarios.
- Dividir los datos en **conjuntos de entrenamiento, validación y prueba**.
- Entrenar diferentes modelos de clasificación.
- Ajustar **hiperparámetros** para mejorar el rendimiento.
- Evaluar la calidad del modelo utilizando el **conjunto de prueba**.
- Realizar una **prueba de cordura (sanity check)** para validar que el modelo aprende patrones reales y no resultados aleatorios.

---

## Dataset

Archivo utilizado:

`/datasets/users_behavior.csv`


Cada fila del dataset representa el **comportamiento mensual de un usuario**.

### Diccionario de datos

| Columna | Descripción |
|-------|-------------|
| `calls` | Número de llamadas realizadas |
| `minutes` | Duración total de llamadas en minutos |
| `messages` | Número de mensajes de texto enviados |
| `mb_used` | Tráfico de internet utilizado en MB |
| `is_ultra` | Plan del usuario (Ultra = 1, Smart = 0) |

La variable **`is_ultra`** es la **variable objetivo** del modelo.

---

## Metodología

El flujo de trabajo del proyecto incluye las siguientes etapas:

### 1. Exploración inicial de los datos
- Revisión del dataset
- Identificación de características relevantes

### 2. División del dataset
Los datos se separaron en tres subconjuntos:

- **Entrenamiento**
- **Validación**
- **Prueba**

Esto permite entrenar el modelo y evaluar su rendimiento de forma objetiva.

### 3. Entrenamiento de modelos

Se evaluaron diferentes algoritmos de clasificación, variando sus **hiperparámetros** para mejorar el rendimiento del modelo.

Ejemplos de modelos utilizados:

- Árboles de decisión
- Bosques aleatorios
- Otros modelos de clasificación

### 4. Evaluación del modelo

Los modelos fueron evaluados utilizando la métrica:

**Accuracy (exactitud)**

El modelo final fue seleccionado en función de su rendimiento en el **conjunto de validación** y posteriormente evaluado en el **conjunto de prueba**.

### 5. Prueba de cordura (Sanity Check)

Se realizó una prueba adicional para verificar que el modelo realmente aprende patrones del dataset y no genera resultados aleatorios.

---

## Resultados

El modelo seleccionado logró superar el umbral mínimo requerido:


Accuracy ≥ 0.75


Esto indica que el modelo puede **predecir correctamente el plan adecuado para los usuarios con una precisión aceptable**, lo que lo hace útil para sistemas de recomendación de planes.

---

## Tecnologías utilizadas

- Python
- Pandas
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter Notebook

---

## Conclusión

Este proyecto demuestra la aplicación práctica de **modelos de clasificación en problemas reales de negocio**. El modelo desarrollado permite analizar patrones de uso de los clientes y recomendar automáticamente el plan más adecuado.

Este tipo de soluciones puede ayudar a las empresas de telecomunicaciones a:

- Optimizar la migración hacia nuevos planes
- Personalizar recomendaciones a clientes
- Incrementar ingresos y mejorar la satisfacción del usuario