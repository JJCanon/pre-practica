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