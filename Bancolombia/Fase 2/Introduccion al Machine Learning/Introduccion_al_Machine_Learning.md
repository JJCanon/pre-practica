# Introducción al Machine Learning
## ¿Qué es Machine Learning?
El **Machine Learning (ML)** es una rama de la inteligencia artificial que permite que las computadoras **aprendan patrones a partir de los datos** sin ser programados explícitamente para cada tarea.
En vez de dar instrucciones fijas, en ML entrenamos un **modelo** con ejemplos, y luego ese modelo puede **hacer predicciones o clasificaciones** sobre datos nuevos.
### Ejemplo cotidiano:
* **Netflix / Spotify**: recomiendan películas o canciones según lo que viste/escuchaste.
* **Correo electrónico**: filtra spam usando patrones en mensajes.
* **Bancos**: detectan fraudes observando transacciones inusuales.

### ¿Cómo funciona ML?
1. **Datos** -> recolectamos ejemplos con variables (features) y la respuesta que queremos predecir (label).
2. **Entrenamiento** -> el algoritmo busca patrones matemáticos en los datos.
3. **Validaciones y prueba** -> verificamos que el modelo funciones en datos que nunca ha visto.
4. **Predicción** -> aplicamos el modelo a nuevos datos para hacer inferencias.

### Categorías principales de ML
1. **Supervisado** -> tenemos etiquetas (ej: predecir nota final de un estudiante, clasificar si un cliente pagará o no).
   * **Regresión**: predecir valores numéricos (ej: gasto mensual).
   * **Clasificación**: predecir categorías (ej: aprobar/reprobar).
2. **No supervisado** -> no hay etiquetas, buscamos estructura en los datos.
   * **Clustering**: agrupar clientes según hábitos.
   * **Reducción de dimencionalidad**: simplificar datos manteniendo la información (ej: PCA).
3. **Reforzamiento** -> un agente aprende tomando decisiones y recibiendo recompensas (ej: un robot aprendiendo a caminar, AlphaGo jugando Go).

### Conceptos clave
* **Entrenamiento**: fase donde el modelo aprende patrones.
* **Validación**: comprobamos el redimiento de datos distintos al entrenamiento.
* **Overfitting (sobreajuste)**: el modelo memoriza los datos y falla en datos nuevos.
* **Generalización**: la capacidad de funcionar bien con datos nuevos.

### Herramientas clave: Scikit-learn
* Librería de Python para ML.
* Ofrece algoritmos de **regresión, clasificación, clustering, preprocesamiento y métricas de evaluación**.
* Flujo típico:
  1. Importar dataset.
  2. Dividir en train/test.
  3. Escoger modelo.
  4. Entrenar (`.fit()`).
  5. Evaluar (`.predict()`, métricas).

## Conceptos clave (Entrenamiento, Validación, Overfitting)
### 1. Entrenamiento
Es la fase en la que el modelo **aprende patrones a partir de los datos**.
* Se le da un **conjunto de entrenamiento (training set)** que contiene ejemplos con variables de entrada (features) y la respuesta (label).
* El algoritmo ajusta parámetros internos para minimizar el error.
Ejemplo: entrenar un modelo con datos de horas de estudio (X) y nota obtenida (Y).

### 2. Validación
Sirve para comprobar si el modelo **aprendió de manera general y no solo memorizó**.
* Se usa un **conjunto de validación/test** (datos que el modelo nunca vio).
* Si el modelo tiene buen rendimiento en entrenamiento pero **malo en validación**, hay **overfitting**.

### 3. Overfitting (sobreajuste)
Ocurre cuando el modelo **aprende demasiado bien los datos de entrenamiento (los memoriza)**, incluyendo ruido y valores atípicos, y pierde capacidad de generalizar.
* Síntomas:
  - Error de entrenamiento bajo.
  - Error de validación alto.
* Soluciones comunes:
  - Obtener más datos.
  - Regularización (penalizar complejidad del modelo).
  - Usar modelos más simples.
  - Validación cruzada (cross-validation).

### Ejemplo práctico en Python
Simulemos datos de **horas de estudio vs nota de examen** y entrenemos un modelo de regresión lineal:
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Dataset ficticio
np.random.seed(42)
horas_estudio = np.random.randint(0, 10, 30)
nota = 3*horas_estudio + np.random.normal(0, 5, 30) # Nota = 3*hotas + ruido
df = pd.DataDrame({"Horas": horas_estudio, "Nota": nota})

# Dividir en entrenamiento y test (80% - 20%)
X = df[["Horas"]]
y = df["Nota"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predicciones
y_pred_train = modelo.predict(X_train)
y_pred_test = modelo.predict(X_test)

# Errores
error_train = mean_squared_error(y_train, y_pred_train)
error_test = mean_squared_error(y_test, y_pred_test)

print("Error en entrenamiento:", error_train)
print("Error en test:", error_test)
```
Interpretación esperada:
* Si los errores en train y test son **similares y bajos**, el modelo generaliza bien.
* Si el error en train es muy bajo y en test muy alto -> **overfitting**.

### Mini - práctica
1. Genera un dataset ficticio con:
   * `Horas_estudio` (entre 0 y 15).
   * `Nota_examen` (≈ 5*horas + ruido).
2. Divide en **70% entrenamiento, 30% test**.
3. Ajusta un **modelo de regresión lineal**.
4. Calcula el error en train y test.
5. Reflexiona: ¿tu modelo está generalizando bien o está sobreajustado?

## Scikit-learn: regresión, clasificación y métricas de evaluación
### ¿Qué es Scitik-learn?
* Es la **librería más usada de Machine Learning en Python**.
* Ofrece algoritmos listos para usar: regresión, clasificación, clustering, reducción de dimensionalidad, metricas de evaluación, preprocesamiento de datos.
* Flujo típico de uso:
  1.  Importar dataset.
  2.  Dividir en **train/test**.
  3.  Escoger un **modelo**.
  4.  Entrenar (`.fit()`).
  5.  Predecir (`.predict()`).
  6.  Evaluar el rendimiento

#### Regresión
Se usa cuando la **variable objetico (y)** es **numérica continua**.
* Ejemplo: predecir la nota de un examen en función de horas de estudio.
* Algoritmo típico: **Regresión lineal**(`LinearRegression`).

#### Clasificación
Se usa cuando la **variable objetivo (y)** es **categórica**.
* Ejemplo: predecir si un estudiante **aprueba/reprueba** un examen.
* Algoritmo típico: **Regresión logística, Árboles de decisión, KNN**.

#### Métricas de Evaluación
* Regresión:
  - `MSE` (Error cuadrático medio).
  - `RMSE` (Raíz del error cuadrático medio).
  - `R²` (Coeficiente de determinación).
* Clasificación:
  - **Accuracy** = % de aciertos.
  - **Precisión, Recall, F1-score** -> útiles cuando hay clases desbalanceadas.
  - **Matriz de confusión** -> muestra aciertos y errores por clase.

### Ejemplo práctico de regresión en Python
predecir nota de un estudiante según horas de estudio
```
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean__squared_error, r2_score
from sklearn.model_selection import train_test_split

# dataset ficticio
np.random.seed(42)
horas = np.random.randint(0, 10, 50)
nota = 5*horas + np.random.normal(0, 5, 50)

X = horas.reshape(-1, 1)
y = nota

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo
modelo = LinearRegression().fit(X_train, y_train)

# Predicción
y_pred = modelo.predict(X_test)

# Evalucación
print(f"MSE: {mean_squared_error(y_test, y_pred)}")
print(f"R²: {r2_score(y_test, y_pred)}")
```

### Ejemplo práctico de clasificación en Python
Clasificar si un estudiante aprueba (nota ≥ 50) o no:
```
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Crear variable binaria: 1 = aprueba, 0 = reprueba
y_class = (y >= 50).astype(int)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_class, test_size=0.2, random_state=42)

# Modelo
modelo_clas = LogisticRegression().fit(X_train, y_train)

# Predicción
y_pred = modelo_clas.predict(X_test)

# Evaluación
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Matriz de confución:\n", confusion_matrix(y_test, y_pred))
print("Reporte de clasificación:\n, classification_report(y_test, y_pred))
```

### Mini práctica
1. Usa el dataset de Student Performance de kaggle que escogiste.
2. Crea dos tareas distintas:
   * **Regresión**: predecir la nota final (variable numérica).
   * **Clasificación**: crear una variable binaria (ej: 1 = aprobó, 0 = reprobó) y entrenar un clasificador.
3. Evalúa con:
   * Para regresión:`MSE`,`R²`.
   * Para clasificación:`Accuracy`, matriz de confusión, `F1-score`.

## Preprocesamiento de datos (normalización, codificación, imputación)
Antes de entrenar un modelo de Machine Learning, los datos deben estar en un **formato adecuado**. los algoritmos no manejan bien **valores faltantes, escalas distintas o variables categóricas**.
#### 1. Normalización y estandarización
* Se usan cuando las variables tienen **escalas muy diferentes**.
* **Normalización (Min-Max scaling)** -> escala los valores en un rango fijo (ej. [0,1]).
  $$x' = \frac{x-min(x)}{max(x)-min(x)}$$
* **Estandarización (Z-score)** -> centra los datos con una media 0 y desviación estándar 1.
  $$x' = \frac{x-μ}{σ}$$
* Ejemplo: si `Edad` está en años (20-60) y `Ingresos` en miles (1000-10000), un modelo de regresión puede sesgarse hacia los ingresos por su magnitud.

#### 2. Codificación de variables categóricas
Los algoritmos trabajan con **números, no con texto**.
* **Label Encoding** -> asigna un número entero a cada categoría (ej: Hombre = 0, Mujer = 1).
* **One-Hot Encoding** -> crea una columna binaria para cada categoría (ej: Género_Hombre, Género_Mujer).
* Se prefiere **One-Hot** cuando no existe un orden natural entre las categorías.

#### 3. Imputación de valores faltantes
Los **valores nulos pueden dañar el entrenamiento. Opciones:
* Eliminar filas/columnas (si son pocos).
* **Imputación estadística**:
  - Media (para variables numéricas).
  - Mediana (si hay outliers).
  - Moda (para categóricas).
* **Imputación avanzada**: modelos predictivos, KNN Imputer, etc.

### Ejemplo práctico en Python
```
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer

# Dataset ficticio
data = {
  "Edad": [20, 25, 30, np.nan, 40],
  "Ingresos": [1000, 2000, 3000, 4000, np.nan],
  "Genero": ["Hombre", "Mujer", "Mujer", "Hombre", "Mujer"]
}
df = pd.DataFrame(data)
print("Dataset original:\n", df)

# --- Imputación ---
imputer_media = SimpleImputer(strategy = "mean")
df["Edad"] = imputer_media.fit_transform(df[["Edad"]])
df["Ingresos"] = imputer_media.fit_transform(df[["Ingresos"]])

# --- Normalización ---
scaler = MinMaxScaler()
df[["Edad_norm", "Ingresos_norm"]] = scaler.fit_transform(df[["Edad","Ingresos"]])

# --- Estandarización --- 
scaler_std = StandardScaler()
df[["Edad_std", "Ingresos_std"]] = scaler_std.fit_transform(df[["Edad,Ingresos"]])

# --- Codificación ---
encoder = OneHotEncoder(sparse=False)
genero_encoded = encoder.fit_transform(df[["Genero"]])
df_encoded = pd.DataFrame(genero_enconded, columns=encoder.get_feature_names_out(["Genero"]))

# --- Final ---
df_final = pd.contact([df, df_encoded], axis=1)
print("\nDataset preprocesado:\n",df_final)
```

### Mini práctica
1. carga el dataset `bank.csv`.
2. Revisa si hay columnas con valores nulos.
3. aplica imputación: media o meidana para numericas, moda para categóricas.
4. Aplica normalización o estandarización a variables como `edad`, `duracion`(duración de la llamada), `balance`, etc., para que estén a una escala comparable.
5. aplica **One-Hot Encoding** para variables como `educación`, `marital`, `job`,`campaign`,etc.
6. si alguna variable tiene un orden natural, usa **Label Encoding** (por ejemplo, `education` si va de menos a más formación).
7. Combina las columnas preprocesadas en un dataframe listo para modelar.
8. Asegurate de que no haya valores faltantes, y que todas las variables estén en formato numérico.
