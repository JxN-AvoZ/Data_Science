# Sprint – Predicción de abandono de clientes (Churn) – Beta Bank

## Descripción del proyecto

Los clientes de **Beta Bank** están abandonando el banco gradualmente cada mes. El equipo de negocio ha identificado que **retener a los clientes actuales es significativamente más económico que adquirir nuevos**, por lo que se busca desarrollar un sistema que permita anticipar qué clientes podrían abandonar el banco.

El objetivo de este proyecto es **construir un modelo de machine learning capaz de predecir si un cliente dejará el banco**, utilizando datos históricos sobre el comportamiento de los clientes y su relación con la institución.

El modelo debe alcanzar un **valor mínimo de F1-score de 0.59** en el conjunto de prueba para cumplir con los requisitos del proyecto.

Además, se evaluará el rendimiento del modelo utilizando la **métrica AUC-ROC** para comparar su capacidad de discriminación frente al F1-score.

---

## Objetivos

- Preparar y limpiar el dataset de clientes.
- Analizar el **desequilibrio de clases** en la variable objetivo.
- Entrenar modelos de clasificación iniciales sin corregir el desequilibrio.
- Implementar **técnicas para manejar el desbalance de clases**.
- Optimizar hiperparámetros y seleccionar el mejor modelo.
- Evaluar el modelo final utilizando **F1-score y AUC-ROC**.

---


Cada fila del dataset representa la información de un cliente del banco.

---

## Diccionario de datos

| Columna | Descripción |
|-------|-------------|
| RowNumber | Índice del registro |
| CustomerId | Identificador único del cliente |
| Surname | Apellido del cliente |
| CreditScore | Puntaje crediticio |
| Geography | País de residencia |
| Gender | Sexo |
| Age | Edad del cliente |
| Tenure | Años que el cliente ha permanecido en el banco |
| Balance | Saldo de la cuenta |
| NumOfProducts | Número de productos bancarios utilizados |
| HasCrCard | Si el cliente posee tarjeta de crédito (1 = sí, 0 = no) |
| IsActiveMember | Si el cliente es un miembro activo (1 = sí, 0 = no) |
| EstimatedSalary | Salario estimado |
| Exited | Variable objetivo (1 = el cliente abandonó el banco, 0 = permanece) |

---

## Metodología

El proyecto se desarrolló siguiendo las siguientes etapas:

### 1. Preparación de los datos

- Carga del dataset
- Eliminación de variables irrelevantes (IDs y nombres)
- Codificación de variables categóricas
- Escalamiento de variables numéricas cuando fue necesario

---

### 2. Análisis del desequilibrio de clases

Se analizó la distribución de la variable **Exited**, identificando un **desequilibrio entre clientes que permanecen y clientes que abandonan el banco**.

Inicialmente se entrenó un modelo **sin corregir el desequilibrio**, lo que permitió observar cómo el modelo tiende a favorecer la clase mayoritaria.

---

### 3. Mejora del modelo

Para mejorar el desempeño del modelo se aplicaron diferentes estrategias para manejar el desbalance de clases, por ejemplo:

- **Ajuste de pesos de clase**
- **Submuestreo o sobremuestreo de clases**

Posteriormente se entrenaron distintos modelos de clasificación ajustando hiperparámetros y evaluando su desempeño en los conjuntos de **entrenamiento y validación**.

---

### 4. Selección del mejor modelo

Se compararon diferentes algoritmos de clasificación, evaluando principalmente:

- **F1-score**
- **AUC-ROC**

El modelo con mejor desempeño fue seleccionado para la evaluación final.

---

### 5. Evaluación final

El modelo final se evaluó en el **conjunto de prueba**, verificando que cumpliera con el requisito mínimo del proyecto:

- **F1-score ≥ 0.59**


También se calculó la **curva ROC y el valor AUC-ROC** para analizar la capacidad del modelo para distinguir entre clientes que abandonan y clientes que permanecen.

---

## Resultados

El modelo final logró superar el umbral requerido de **F1-score**, demostrando una capacidad adecuada para identificar clientes con riesgo de abandono.

El análisis de **AUC-ROC** confirmó que el modelo tiene una buena capacidad de discriminación entre ambas clases.

---

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter Notebook

---

## Conclusiones

Este proyecto demuestra cómo aplicar **machine learning para problemas de churn prediction**, un caso común en sectores como banca, telecomunicaciones y servicios digitales.

La capacidad de identificar clientes con alta probabilidad de abandono permite a las empresas:

- implementar **estrategias de retención**
- mejorar la **personalización de servicios**
- reducir la **pérdida de clientes**

Este tipo de modelos puede integrarse en sistemas de **Customer Relationship Management (CRM)** para apoyar la toma de decisiones basada en datos.
