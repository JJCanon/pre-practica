# Analítica Descriptiva y Visualización de Datos

#### ¿Qué es la estadística descriptiva y la visualización de datos?
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
### Medidas de Tendencia Central
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

### Medidas de Dispersión
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

### Ejemplo práctico en Python
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

### Mini - Práctica
1. Crea una lista en Python con **15 números aleatorios entre 50 y 500**.
2. Calcula **media, mediana, moda, varianza, desviación estándar, rango, Q1 y Q3.**
3. Compara si tu media y mediana están cerca o muy diferentes (eso te dirá si hay outliers).

## Detección de Outliers.
### ¿Qué es un outlier?
Un outlier es un valor que **se aleja significativamente del resto de los datos**.
* Puede deberse a un **error de registro** (ejemplo: poner 10,000 en lugar de 100).
* O puede ser un **datos real pero atípico** (ejemplo: un cliente que gasta muchísimo más que el promedio).
Los outliers son importantes porque:
* **Distorsionan medidas** como la media y la desviación estándar.
* pueden ser **indicadores de fraude, fallos o fenómenos especiales**.
* En modelos de machine learning, pueden **afectar el rendimiento**.

### Métodos para detectar outliers
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

### Ejemplo práctico en Python
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

### Mini - Práctica
1. Genera una lista de **20 valores aleatorios entre 100 y 500**, y agrégale manualmente un valor muy alto (ej: 2000).
2. Detecta el outlier usando:
   * Método IQR.
   * Método de desviación estándar.
3. Compara si ambos métodos detectan el mismo valor.