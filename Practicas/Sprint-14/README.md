# Machine Learning aplicado a seguros – Sure Tomorrow

## Descripción del proyecto

La compañía de seguros **Sure Tomorrow** busca aprovechar el uso de machine learning para mejorar sus procesos de negocio, incluyendo marketing, predicción de beneficios y protección de datos sensibles.

En este proyecto se desarrollan múltiples soluciones basadas en datos para abordar diferentes necesidades del negocio, desde la identificación de clientes similares hasta la protección de información personal mediante técnicas de transformación de datos.

---

## Objetivos

- Identificar clientes similares para estrategias de marketing.
- Predecir la probabilidad de que un cliente reciba beneficios de seguro.
- Estimar la cantidad de beneficios que un cliente podría recibir.
- Proteger los datos personales sin afectar el rendimiento de los modelos.

---

## Dataset

Archivo: `/datasets/insurance_us.csv`

### Características:
- Género
- Edad
- Salario
- Número de familiares

### Variable objetivo:
- Número de beneficios de seguro recibidos en los últimos 5 años

---

## Etapas del proyecto

### 1. Análisis y validación de datos
- Exploración inicial del dataset
- Verificación de valores ausentes
- Detección de valores atípicos
- Validación de consistencia de datos

---

### 2. Búsqueda de clientes similares (k-NN)

- Implementación de algoritmo basado en distancia (k-Nearest Neighbors)
- Identificación de clientes similares a partir de características numéricas
- Aplicación para segmentación y marketing personalizado

---

### 3. Clasificación: predicción de beneficios

- Construcción de modelos de clasificación
- Comparación contra un modelo dummy (baseline)
- Evaluación de desempeño
- Análisis de si el modelo puede ser peor que el baseline

---

### 4. Regresión: estimación de beneficios

- Implementación de modelo de regresión lineal
- Predicción de la cantidad de beneficios de seguro
- Evaluación del rendimiento del modelo

---

### 5. Protección de datos (Data Obfuscation)

- Desarrollo de un algoritmo de transformación de datos basado en álgebra lineal
- Aplicación de enmascaramiento para proteger información sensible
- Validación de que el modelo mantiene su desempeño tras la transformación

---

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Scikit-learn
- Machine Learning
- Álgebra lineal

---

## Resultados

- Se lograron identificar clientes similares para segmentación efectiva.
- Los modelos de clasificación superaron el rendimiento del modelo dummy.
- Se construyó un modelo de regresión capaz de estimar beneficios de manera consistente.
- Se implementó un método de protección de datos que mantiene la calidad del modelo.

---

## Enfoque principal

Aplicación de machine learning en múltiples escenarios de negocio, combinando análisis predictivo, segmentación de clientes y protección de datos mediante transformaciones matemáticas.
