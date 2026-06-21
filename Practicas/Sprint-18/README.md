# Sprint 18 - Proyecto
# Visión Artificial para Estimación de Edad – Good Seed

## Descripción del proyecto

La cadena de supermercados **Good Seed** busca evaluar si la ciencia de datos y la visión artificial pueden ayudar a cumplir las regulaciones relacionadas con la venta de bebidas alcohólicas, evitando la venta a personas menores de edad.

Para ello, se desarrolló un modelo de **Deep Learning** capaz de estimar la edad de una persona a partir de imágenes faciales capturadas por cámaras instaladas en las áreas de pago.

El objetivo principal fue determinar si un sistema basado en visión artificial puede proporcionar estimaciones de edad suficientemente precisas para apoyar procesos de validación de identidad en entornos comerciales.

---

## Objetivos

* Analizar un conjunto de imágenes etiquetadas con edades.
* Realizar exploración y preprocesamiento de datos.
* Construir un modelo de estimación de edad basado en redes neuronales convolucionales.
* Evaluar el desempeño utilizando la métrica **MAE (_Mean Absolute Error_)**.
* Analizar las limitaciones y oportunidades de mejora del modelo.

---

## Tecnologías utilizadas

* Python
* TensorFlow
* Keras
* ResNet50
* NumPy
* Pandas
* Matplotlib
* Computer Vision
* Deep Learning

---

## Metodología

### 1. Exploración de datos

Se analizaron las distribuciones de edad y las características generales del conjunto de imágenes para identificar posibles sesgos y desbalances.

### 2. Extracción de características

Debido a las limitaciones de hardware disponibles (_GPU GTX 1660 Ti con 6GB de VRAM_), se utilizó una estrategia de **transfer learning** mediante una red **ResNet50 preentrenada en ImageNet**.

El modelo fue utilizado como extractor de características congelado, generando vectores de representación de 2,048 dimensiones para cada imagen.

### 3. Construcción del modelo

Sobre los embeddings generados por ResNet50 se entrenó una red neuronal completamente conectada con capas densas y técnicas de regularización mediante Dropout para reducir el sobreajuste.

### 4. Evaluación

El rendimiento se evaluó mediante:

* MAE (_Mean Absolute Error_)
* Comparación entre error de entrenamiento y validación
* Análisis de capacidad de generalización

---

## Resultados

| Métrica               | Valor      |
| --------------------- | ---------- |
| MAE Entrenamiento     | ~6.0 años  |
| MAE Validación        | 6.56 años  |
| Objetivo del proyecto | MAE < 8    |
| Resultado             | ✓ Cumplido |

---

## Conclusiones

### Objetivo alcanzado

El modelo logró un **MAE de validación de 6.56 años**, superando satisfactoriamente el objetivo establecido de mantener un error inferior a 8 años.

### Transfer Learning como estrategia clave

La extracción de embeddings utilizando una arquitectura **ResNet50 congelada** permitió superar las restricciones de hardware disponibles y obtener representaciones visuales altamente informativas.

Los vectores de características de 2,048 dimensiones generados por la red preentrenada fueron suficientes para capturar patrones relevantes relacionados con la edad facial.

### Control del sobreajuste

Se observó un sobreajuste moderado:

* MAE entrenamiento ≈ 6.0
* MAE validación ≈ 6.56

La diferencia relativamente pequeña entre ambas métricas indica una buena capacidad de generalización, favorecida por la incorporación de capas **Dropout (0.4 y 0.3)** durante el entrenamiento.

### Limitaciones del hardware

El principal factor limitante fue la disponibilidad de una **GPU GTX 1660 Ti con 6GB de VRAM**, lo que impidió realizar fine-tuning completo de ResNet50.

Con hardware más potente (12GB o más de VRAM) sería posible ajustar las capas profundas de la red y potencialmente reducir el error medio absoluto hasta valores cercanos a 4–5 años.

### Dataset utilizado

Se utilizó el dataset **UTKFace**, que contiene:

* 23,708 imágenes faciales
* Rango de edad: 1 a 116 años

Comparado con el dataset original del curso (7,591 imágenes), UTKFace ofrece una mayor diversidad de edades y condiciones visuales.

Sin embargo, también presenta un desbalance importante hacia adultos jóvenes, con una edad promedio cercana a los 33 años, lo que puede influir en el desempeño del modelo para edades extremas.

---

## Valor de negocio

Los resultados demuestran que los modelos de visión artificial basados en Deep Learning pueden utilizarse como herramientas de apoyo para procesos de validación de edad en puntos de venta.

Aunque el sistema no reemplaza la verificación oficial de identidad, puede servir como una capa adicional de control para detectar posibles compras de alcohol realizadas por menores de edad.

---

## Competencias demostradas

* Computer Vision
* Deep Learning
* Transfer Learning
* Redes Neuronales Convolucionales (_CNN_)
* TensorFlow y Keras
* Evaluación de Modelos
* Regularización y Prevención de Overfitting
* Procesamiento de Imágenes
* Optimización bajo restricciones de hardware
