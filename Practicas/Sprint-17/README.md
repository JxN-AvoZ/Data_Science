# Clasificación de reseñas de películas con NLP – Film Junky Union

## Descripción del proyecto

Film Junky Union, una comunidad enfocada en películas clásicas, busca desarrollar un sistema automático para filtrar y clasificar reseñas de películas según su sentimiento.

El objetivo de este proyecto es construir un modelo de procesamiento de lenguaje natural (NLP) capaz de identificar automáticamente si una reseña es positiva o negativa, utilizando un dataset de reseñas de películas de IMDB.

El modelo desarrollado debe alcanzar un valor mínimo de:

_**F1-score ≥ 0.85**_

---

## Objetivo

Desarrollar y evaluar distintos modelos de clasificación de texto para detectar críticas negativas de películas a partir de reseñas escritas por usuarios.

__Dataset__

Archivo: `imdb_reviews.tsv`

*__Variables principales__*

| Columna   | Descripción                                        |
| --------- | -------------------------------------------------- |
| `review`  | Texto de la reseña                                 |
| `pos`     | Etiqueta objetivo (`0` = negativa, `1` = positiva) |
| `ds_part` | División del dataset (`train` / `test`)            |


Dataset original publicado en:

Maas, Andrew L., et al. Learning Word Vectors for Sentiment Analysis (ACL 2011)

---

## Metodología

### 1. Carga y exploración de datos
- Importación del dataset
- Revisión de estructura y tipos de datos
- Análisis de balance de clases
- Exploración de distribución de reseñas positivas y negativas

### 2. Preprocesamiento de texto

Se aplicaron técnicas de limpieza y transformación de texto:

- Conversión a minúsculas
- Eliminación de signos de puntuación
- Eliminación de caracteres especiales
- Tokenización
- Eliminación de stopwords
- Vectorización de texto mediante:
    - TF-IDF
    - Bag of Words

### 3. Modelado

Se entrenaron múltiples modelos de clasificación, incluyendo:

- Regresión logística
- Random Forest
- Gradient Boosting
- (Opcional) modelos basados en embeddings/BERT

Cada modelo fue evaluado utilizando métricas de clasificación.

### 4. Evaluación

La métrica principal utilizada fue:

**_F1-score_**

También se analizaron:

- Accuracy
- Precision
- Recall
- Matriz de confusión

### 5. Pruebas manuales

Se escribieron reseñas personalizadas para probar el comportamiento de los modelos en escenarios reales y comparar sus predicciones.

Resultados
Se logró entrenar modelos capaces de clasificar reseñas con alto desempeño.
El mejor modelo alcanzó un valor de F1-score superior a 0.85.
Los modelos basados en TF-IDF + Regresión Logística mostraron un excelente balance entre velocidad y precisión.
Conclusiones
El preprocesamiento de texto tiene un impacto significativo en el rendimiento de los modelos NLP.
Modelos relativamente simples pueden ofrecer resultados muy competitivos en tareas de análisis de sentimientos.
La vectorización TF-IDF resultó altamente efectiva para este problema.
Este tipo de sistemas puede aplicarse en plataformas reales para moderación automática, análisis de opinión y clasificación de contenido.
Tecnologías utilizadas
Python
pandas
numpy
matplotlib
scikit-learn
nltk
spaCy
transformers (opcional)
Jupyter Notebook
Habilidades aplicadas
Procesamiento de lenguaje natural (NLP)
Limpieza y transformación de texto
Clasificación supervisada
Evaluación de modelos
Análisis de sentimientos
Ingeniería de características textuales
