# Analítica Descriptiva y Visualización de Datos.

#### ¿Qué es la estadística descriptiva y la visualización de datos?.
La **estadística descriptiva** es la rama de la estadística que se encarga de **resumir, organizar y presentar los datos** de forma clara y comprensible, sin sacar conclusiones más allá de lo que los datos muestran.

Sirve para **entender el comportamiendo de los datos** antes de aplicar modelos más complejos.

Por ejemplo, si tienes un dataset de gastos mensuales de clientes:
* La estadística descriptiva te ayuda a saber **cuál es el gasto promedio**, **qué tan dispersos son los gastos**, y **qué valores son extremos**.
**La visualización de datos**, por otro lado, es el complemento gráfico:
* Nos permite **detectar patrones, tendencias, anomalías y relaciones** que a veces no se ven solo con números.
* Ejemplo: un histograma muestra cómo se distribuyen los datos; un boxplot revela valores atípicos; un scatterplot permite observar relaciones entre variables.

#### ¿Por qué es importante?
1. **Primer paso en ciencia de datos** -> Antes de aplicar machine learning, debemos entender cómo son los datos.
2. **Calidad de datos** -> Podemos detectar errores o outliers.
3. **Comunicación clara** -> Un gráfico explica más que tablas llenas de números. 

## Medidas de tendencia central y disperción.
### Medidas de Tendencia Central.
Son valores que representan **el centro** o **el comportamiento** "típico" de los datos.
1. Media (Promedio):
   $$\bar{x} = \frac{\sum x_i}{n}$$
   * Es el valor promedio de todos los datos.
   * Muy sensible a valores extremos (outliers).
2. Mediana:
   * Valor que divide el conjunto en dos mitades iguales.
   * Más robusta frente a outliers.
3. Moda:
   * Valor que más se repite.
   * Puede haber más de una moda (multimodal).

### Medidas de Dispersión.
Indican **qué tan alejados están los datos del centro**.
1. Rango:
   $$Rango = máx - mín$$
2. Varianza (σ²):
   Promedio de las desviaciones cuadradas respecto a la media.
3. Desviación estándar (σ):
   Raíz cuadrada de la varianza. Indica en promedio cuánto se alejan los datos de la media.
4. Coeficiente de variación (CV):
   $$CV=\frac{σ}{\bar{x}}$$
   * Mide la dispersión relativa (útil para comparar las variables en distintas escalas).
5. Percentiles y cuartiles:
   * Percentil 50: Mediana.
   * Cuartil 1 (Q1): 25% de los datos están por debajo.
   * CUartil 3 (Q3): 75% de los datos están por debajo.
   * Muy útiles para boxplots.

### Ejemplo práctico en Python.
Imagina un dataset de **gastos mensuales (en USD)** de 10 clientes:
```
import numpy as np
import pandas as pd

# Datos ficticios
gastos = [200, 220, 250, 300, 310, 320, 500, 520, 1000, 1500]
df = pd.DataFrame(gastos, columns['Gasto'])

# Medidas de tendencia central
media = df['Gasto'].mean()
mediana = df['Gasto'].median()
moda = df['Gasto'].mode()[0]

# Medidas de dispersión
rango = df['Gasto].max() - df['Gasto'].min()
varianza = df['Gasto'].var()
desviacion = df['Gasto'].std()
cv = desviacion / media
q1 = df['Gasto'].quantile(0.25)
q3 = df['Gasto'].quantile(0.75)

(media, mediana, moda, rango, varianza, desviacion, cv, q1, q3)
```
Este código devolverá algo como:
* Media = 612
* Mediana = 310
* Moda = 200 (en este caso porque solo aparece una vez, pero es la más baja)
* Rango = 1300
* Varianza ≈ 214.600
* Desviación estándar ≈ 463
* CV ≈ 0.75 (alta dispersión)
* Q1 = 250
* Q3 = 520

Observa cómo la **media** está muy **inflada** por el valor extremo de 1500, mientras que la **mediana representa mejor el centro real** de los datos.

### Mini - Práctica.
1. Crea una lista en Python con **15 números aleatorios entre 50 y 500**.
2. Calcula **media, mediana, moda, varianza, desviación estándar, rango, Q1 y Q3.**
3. Compara si tu media y mediana están cerca o muy diferentes (eso te dirá si hay outliers).

## Detección de Outliers.
### ¿Qué es un outlier?.
Un outlier es un valor que **se aleja significativamente del resto de los datos**.
* Puede deberse a un **error de registro** (ejemplo: poner 10,000 en lugar de 100).
* O puede ser un **datos real pero atípico** (ejemplo: un cliente que gasta muchísimo más que el promedio).
Los outliers son importantes porque:
* **Distorsionan medidas** como la media y la desviación estándar.
* pueden ser **indicadores de fraude, fallos o fenómenos especiales**.
* En modelos de machine learning, pueden **afectar el rendimiento**.

### Métodos para detectar outliers.
1. Método del rango intercuartílico (IQR):
   * Calcular: 
        $$IQR=Q3-Q1$$
   * Umbrales:
        - Límite inferior = Q1 - 1.5 x IQR
        - Límite superior = Q3 + 1.5 x IQR
   * Valores fuera de ese rango = outliers.
   * Muy usado en **boxplot**.
2. Método de la desviación estándar:
   * Calcular media y desviación estándar (σ).
   * Si un dato está más de **2σ o 3σ de la media**, puede considerarse un outlier.
3. Métodos visuales:
   * **Boxplot** -> detecta valores extremos fácilmente.
   * **Scatterplot** -> ayuda a ver puntos alejados de la tendencia general.
   * **Histogramas** -> muestran concentraciones de datos y valores raros.

### Ejemplo práctico en Python.
Tomemos los mismos datos de gastos:
```
import numpy as np
import pandas as pd

gastos = [200, 220, 250, 300, 310, 320, 500, 520, 1000, 1500]
df = pd.DataFrame(gastos, columns=["Gasto"])

# --- Método IQR ---
Q1 = df['Gasto'].quantile(0.25)
Q3 = df['Gasto'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers_iqr = df[(df['Gasto] < limite_inferior) | (df['Gasto] > limite_superior)]

# --- Método Desviación Estándar ---
media = df['Gasto'].mean()
desviacion = df['Gasto'].std()

outliers_std = df[(df['Gasto]< media - 3*desviacion) | (df['Gasto'] > media + 3*desviacion)]

(outliers_iqr, outliers_std)
```
Resultado esperado:
* Con **IQR** -> detecta `1000` y `1500` como outliers.
* Con **Desviación estándar** -> probablemente solo `1500`, porque `1000` está dentro de 3σ.

### Mini - Práctica.
1. Genera una lista de **20 valores aleatorios entre 100 y 500**, y agrégale manualmente un valor muy alto (ej: 2000).
2. Detecta el outlier usando:
   * Método IQR.
   * Método de desviación estándar.
3. Compara si ambos métodos detectan el mismo valor.

## Histogramas, Boxplots y Scatterplots.
### Histogramas.
* Son gráficos que muestran la **distribución de una variable numérica**.
* Dividen los datos en intervalos ("bins) y cuentan cuántos valores caen en cada intervalo.
* Útiles para_
  - Ver si los datos son **simétricos** o **sesgados**.
  - Detectar concentraciones y valores raros.
Ejemplo: distribución de edades de clientes.

### Boxplots (Diagrama de caja y bigotes).
* Muestran la **dispersión y outliers** de manera resumida.
* Elementos:
  - Caja: entre **Q1 y Q3** (50% central de los datos).
  - Línea dentro de la caja: la **mediana**.
  - Bigotes: hasta el valor máximo/mínimo dentro del rango permitido.
  - Puntos fuera: **outliers**.
* Muy usados para comparar **varias categorías**.
Ejemplo: comparar salarios de hombres vs. mujeres.

### Scatterplots (Gráficos de dispersión).
* Representan **dos variables numéricas** en un plano XY.
* Cada punto es una observación.
* Útiles para:
  - Ver si hay **correlación** (positiva, negatica o nula).
  - Detectar **patrones o clusters**.
  - Identificar outliers en relaciones bivariadas.
Ejemplo: comparar **horas de estudio vs. nota obtenida**.

### Ejemplo práctico en Python.
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset ficticio
data ={
    "Gasto":[200, 220, 250, 300, 310, 320, 500, 520, 1000, 1500],
    "Edad":[22, 25, 27, 30, 32, 35, 40, 42, 50, 60]
}
df = pd.DataFrame(data)

# --- Histograma ---
plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.hist(df['Gasto'], bins=6, edgecolor="black")
plt.title("Histograma de Gasto)
plt.xlable("Gasto ($))
plt.ylabel("Frecuencia")

# --- Boxplot ---
plt.subplot(1,3,2)
sns.boxplot(y=df['Gasto'])
plt.title("Boxplot de Gasto")

# --- Scatterplot ---
plt.subplot(1,3,3)
plt.scatter(df['Edad'], df['Gasto'], c='blue')
plt.title("Scatterplot: Edad vs Gasto")
plt.xlabel("Edad")
plt.ylabel("Gasto ($))

plt.tight_layout()
plt.show()
```
Este cógigo produce:
1. **Histograma** -> muestra que la mayoría gasta entre 200-500, pero hay dos casos extremos.
2. **Boxplot** -> resalta claramente 1000 y 1500 como outliers.
3. **Scatterplot** -> muestra que el gasto tiende a subir con la edad, pero con dos casos atípicos.

### Mini - Práctica
1. Crea un dataset con dos variables:
   * `Ingresos` (ej. valores entre 1,000 y 10,000).
   * `Edad` (ej. valores entre 20 y 60).
2. Genera:
   * Un **Histograma** para `Ingresos`.
   * Un **Boxplot** para `Ingresos`.
   * Un **Scatterplot** entre `Edad` y `Ingresos`.
3. Interpreta si hay **patrones, simetría o outliers**.

## Práctica de Integración
#### 1. Dataset
Simulemos un dataset de **clientes de un banco** con las siguientes variables:
* `Edad` (años, entre 18 y 70).
* `Ingresos` (en USD, entre 800 y 10000, con algunos valores extremos).
* `Gasto_mensual` (en USD, entre 100 y 5000).

#### 2. Estadística descriptiva
* Calcula para **Ingresos** y **Gasto_mensual**:
  - Media, mediana, moda.
  - Rango, varianza, desviación estándar.
  - Q1 y Q3.

#### 3. Detección de outliers
* Usa el **método IQR** para detectar outliers en `Ingresos` y `Gasto_mensual`.
* Usa el **método de desviación estándar** y compara los resultados.
  
#### 4. Visualización
* Crea un **histograma** para `Ingresos` y `Gasto_mensual`.
* Crea un **boxplot** para `Ingresos` y `Gasto_mensual`.
* Haz un **scatterplot** entre `Ingresos` y `Gasto_mensual` -> ¿los clientes con más ingresos gastan más?

#### 5. Interpretación
Responde con base en tus resultados:
1. ¿Cuál es la media y la mediana de los ingresos? ¿Qué dice eso sobre la simetría de los datos?.
2. ¿Se detectaron outliers? ¿Son errores o clientes "reales" de alto valor?
3. Según el scatterplot, ¿existe relación entre los ingresos y gasto mensual?