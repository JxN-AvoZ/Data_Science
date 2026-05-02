# Predicción del valor de vehículos – Rusty Bargain

## Descripción del proyecto

Rusty Bargain es una plataforma de venta de coches de segunda mano que busca desarrollar una aplicación capaz de estimar rápidamente el valor de mercado de un vehículo.

El objetivo de este proyecto es construir y comparar distintos modelos de machine learning para predecir el precio de un coche, considerando no solo la calidad de la predicción, sino también el tiempo de entrenamiento y la velocidad de inferencia.

Este tipo de problema es representativo de sistemas reales de pricing, donde el balance entre precisión y eficiencia computacional es fundamental.

---

## Objetivos

- Predecir el precio de vehículos usados.
- Comparar distintos modelos de machine learning.
- Evaluar el trade-off entre:
  - Calidad de predicción
  - Tiempo de entrenamiento
  - Velocidad de predicción
- Identificar el modelo más eficiente para uso en producción.

---

## Dataset

Archivo: `/datasets/car_data.csv`

### Características principales:

- Tipo de vehículo
- Año de registro
- Tipo de transmisión
- Potencia del motor
- Modelo y marca
- Kilometraje
- Tipo de combustible
- Estado de reparación

### Variable objetivo:

- `Price` — precio del vehículo (en euros)

---

## Etapas del proyecto

### 1. Preparación de datos

- Limpieza de datos
- Manejo de valores ausentes
- Eliminación de registros irrelevantes
- Codificación de variables categóricas
- Análisis exploratorio

---

### 2. Modelado

Se entrenaron múltiples modelos para comparar desempeño:

- Regresión lineal (baseline)
- Árbol de decisión
- Bosque aleatorio (Random Forest)
- Gradient Boosting (LightGBM)
- (Opcional) XGBoost / CatBoost

---

### 3. Evaluación

Los modelos se evaluaron utilizando:

- **RMSE (Root Mean Squared Error)** como métrica principal
- Tiempo de entrenamiento
- Velocidad de predicción

---

### 4. Comparación de modelos

Se analizaron los siguientes aspectos:

- Precisión del modelo
- Costo computacional
- Escalabilidad para producción

---

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Scikit-learn
- LightGBM
- (Opcional) XGBoost / CatBoost
- Jupyter Notebook

---

## Resultados

- Los modelos de **gradient boosting (LightGBM)** mostraron el mejor balance entre precisión y eficiencia.
- Random Forest ofreció buen desempeño, pero con mayor costo computacional.
- La regresión lineal sirvió como baseline para validar resultados.
- Se identificó el modelo más adecuado considerando un entorno de producción real.

---

## Enfoque principal

Comparación de modelos de machine learning con enfoque en rendimiento práctico, evaluando no solo la precisión sino también el costo computacional y la viabilidad en sistemas reales.

---

## Impacto del proyecto

Este proyecto demuestra la capacidad de:

- Seleccionar modelos adecuados para producción
- Evaluar trade-offs entre precisión y rendimiento
- Implementar soluciones de machine learning en escenarios reales de negocio
