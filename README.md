
<img src="images/cabecera.png" alt="cabecera" width="900" height="500">

# 🧠 Proyecto de Machine Learning: Predicción de la Cronificación de la Depresión

### ESPAÑOL 🇪🇸

## 🌟 Descripción
Este proyecto utiliza técnicas avanzadas de Machine Learning para **predecir la probabilidad de cronificación de la depresión** en pacientes. Se emplea un dataset especializado de [Kaggle: Depression Dataset](https://www.kaggle.com/datasets/anthonytherrien/depression-dataset) que incluye variables relacionadas con la salud mental y demografía.

## 🎯 Objetivos
- 🔍 **Análisis Exploratorio**: Entender y explorar las características del dataset.
- 🤖 **Modelo Predictivo**: Construir un modelo que estime la cronificación de la depresión.
- 📊 **Evaluación del Modelo**: Medir el rendimiento con métricas relevantes.

## 🛠️ Herramientas Utilizadas
- **Python** 🐍
- **Bibliotecas**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Jupyter Notebook, Keras, Tensorflow, Streamlit
- **Machine Learning**: Modelos supervisados para clasificación

## 🧪 Modelos Probados
Durante el desarrollo del proyecto, se evaluaron varios modelos de Machine Learning para determinar el más efectivo en la predicción de la cronificación de la depresión:

- **Regresión Logística**
- **Random Forest**
- **XGBoost**
- **K-Nearest Neighbors (KNN)**
- **Máquinas de Vectores de Soporte (SVM)**
- **K-Means**
- **Red Neuronal**
- **SGDClassifier** (modelo definitivo seleccionado)

Cada modelo fue entrenado y evaluado utilizando técnicas de validación cruzada y recall  como métrica de orientación para asegurar una evaluación exhaustiva.

## 🌐 Implementación de la Aplicación con Streamlit
Para facilitar la interacción con el modelo predictivo, se desarrolló una aplicación web utilizando Streamlit. Esta aplicación permite a los usuarios ingresar datos relevantes y obtener una predicción sobre la probabilidad de cronificación de la depresión.

- **Archivo principal**: `app.py`
- **Dependencias**: Listadas en `requirements.txt`

Para ejecutar la aplicación localmente:

1. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecutar la aplicación:
   ```bash
   streamlit run app.py
   ```

## 📈 Resultados Esperados
Anticipar la cronificación de la depresión ayudará a los profesionales de la salud a **intervenir de forma temprana** y mejorar la calidad de vida de los pacientes.

---

# 🧠 Machine Learning Project: Predicting Chronic Depression

### ENGLISH 🇬🇧

## 🌟 Overview
This project applies advanced Machine Learning techniques to **predict the probability of chronic depression** in patients. A specialized dataset from [Kaggle: Depression Dataset](https://www.kaggle.com/datasets/anthonytherrien/depression-dataset) is utilized, which includes mental health, demographic, and risk factor variables.

## 🎯 Goals
- 🔍 **Exploratory Analysis**: Understand and explore the dataset's features.
- 🤖 **Predictive Model**: Build a model to estimate chronic depression risks.
- 📊 **Model Evaluation**: Assess performance using relevant metrics.

## 🛠️ Tools Used
- **Python** 🐍
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Jupyter Notebook
- **Machine Learning**: Supervised models for classification

## 🧪 Models Tested
Throughout the project's development, various Machine Learning models were evaluated to determine the most effective in predicting chronic depression:

- **Logistic Regression**
- **Random Forest**
- **XGBoost**
- **K-Nearest Neighbors (KNN)**
- **Support Vector Machines (SVM)**
- **K-Means**
- **Neural Network**
- **SGDClassifier** (final model selected)

Each model was trained and evaluated using cross-validation techniques and metrics such as accuracy, recall, and F1-score to ensure a comprehensive assessment.

## 🌐 Streamlit Application Implementation
To facilitate interaction with the predictive model, a web application was developed using Streamlit. This application allows users to input relevant data and receive a prediction regarding the probability of chronic depression.

- **Main file**: `app.py`
- **Dependencies**: Listed in `requirements.txt`

To run the application locally:

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   streamlit run app.py
   ```

## 📈 Expected Outcomes
Anticipating chronic depression will empower healthcare professionals to **intervene early** and improve patient quality of life.
```

Este README actualizado proporciona una visión detallada del proyecto, incluyendo los modelos de Machine Learning evaluados y la implementación de la aplicación web con Streamlit. 