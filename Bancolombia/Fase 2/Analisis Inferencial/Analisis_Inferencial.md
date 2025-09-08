# Análisis Inferencial
## ¿Qué es el Análisis Inferencial?
La **estadística inferencial** va más allá de describir los datos:
- Su objetivo es **sacar conclusiones sobre una población** basándonos en una **muestra de datos**.
En otras palabras: mientras la **estadística descriptiva** te dice que "cómo son tus datos", la **Estadística inferencial** te ayuda a responder "qué puedo concluir sobre el conjunto mayor".

### Diferencia clave.
* **Descriptiva** -> Resumir y visualizar lo que tenemos.
* **Inferencial** -> Generalizar, validar hipótesis, hacer predicciones.

### Flujo de trabajo típico en análisis inferencial
1. **Plantear hipótesis**: Ejemplo -> "Los clientes mayores de 40 gastan más que los menores de 40".
2. Elegir la **prueba estadística adecuada** según el tipo de variable (numérica, categórica, número de grupos).
3. **Ejecutar el test** (t-test. ANOVA, chi-cuadrado, regresión).
4. Interpretar p-valor:
   * si **p < 0.05** -> hay evidencia suficiente para rechazar hipótesis nula.
   * Si **p > 0.05** -> no hay evidencia suficiente, mantenemos la hipótesis nula.
5. **Visualizar y comunicar resultados** (gráficos de comparación, regresiones, tendencias de series de tiempo).

## Pruebas de Hipótesis
### ¿Qué es una hipótesis estadística?
Una **Hipotesis** es una afirmación sobre una población que queremos comprobar con una muestra de datos.

Siempre se plantean **dos hipótesis**:
* **Hipótesis nula (H₀)** No hay diferencia, efecto o relación.
* **Hipótesis alternativa** (H₁): Sí hay diferencia, efecto o relación.
Ejemplo:
* H₀: El gasto promedio de hombres y de mujeres es el mismo.
* H₁: El gasto promedio de hombres y mujeres es diferente.

### Pasos en una prueba de hipótesis
1. Formular H₀ y H₁.
2. Elejir la prueba estadistica adecuada según los datos.
3. Calcular el **estadistico de prueba** y el **p-valor**.
4. Tomar decisión:
   * Si **p < 0.05**: rechazamos H₀ (hay diferencia).
   * Si **p > 0.05**: no rechazamos H₀ (no hay diferencia).

### Tipos de pruebas que veremos
1. **t-test (Prueba t de Student)**
   * Compara **promedios** entre grupos.
   * Variantes:
     - **t-test de una muestra** -> comparar media de una muestra con un valor.
     - **t-test de dos muestras independientes** -> comparar medias entre dos grupos (ejemplo: hombres vs mujeres).
     - **t-test pareado** -> comparar medias en el mismo grupo antes y después de un tratamiento.
2. **ANOVA (Análisis de Varianza)**
   * Compara **medias de más de 2 grupos**.
   * Ejemplo: comparar ingresos medios entre 3 niveles educativos (bajo, medio, alto).
   * H₀: todas las medias son iguales.
   * H₁: al menos una media es diferente.
3. **Chi-cuadrado (χ²)**
   * Compara **freciencias de variables categóricas**.
   * Ejemplo: ¿la preferencia por un producto depende del género?.
   * Si la diferencia entre frecuencias observadas y esperadas es muy grande, hay dependencia.

### Ejemplo práctico en Python
Supongamos que tenemos datos de clientes con **género, gasto mensual y preferencia por producto**.
```
import pandas as pd
import numpy as np
from scipy import stats

# Dataset ficticio
np.random.seed(42)
n = 50
hombres = np.random.normal(2000,500,n)
mujeres = np.random.normal(2200,600,n)

df= pd.DataFrame({
    "Genero":['Hombre']*n + ['Mujer']*n,
    "Gasto": np.concatenate([hombres, mujeres])
})

# --- t-test: comparar gasto entre hombres y mujeres ---
t_stat, p_val = stats.ttest_ind(hombres, mujeres)

t_stat, p_val
```
Interpretación:
* Si **p_val < 0.05** → los gastos son significativamente diferentes.
* Si **p_val > 0.05** → no hay diferencia significativa.

### Mini - práctica
1. Simula un dataset con 3 grupos de estudiantes (`A`,`B`,`C`) con notas en un examen.
   * Grupo A: media 70, sd 10.
   * Grupo B: media 75, st 12.
   * Grupo C: media 80, st 8.
2. Aplíca un ANOVA para ver si las medias de los 3 grupos son iguales.
3. Luego crea una tabla de **frecuencias** (ejemplo: preferencia de producto `x` o `y` entre hombres y mujeres) y aplica un **chi-cuadrado**.

## Correlación y Regresión Lineal
### Correlación
La **correlación** mide la **fuerza y dirección de la relación entre dos variables numéricas**.
* Se representa con el **coeficiente de correlación de Pearson (r)**:
  * Valores entre -1 y +1.
  * **r ≈ +1** -> fuerte correlación positiva (si X sube, Y sube).
  * **r ≈ -1** -> fuerte correlación negativa (si X sube, Y baja).
  * **r ≈ 0** -> no hay relación lineal.

- Importante: correlacion ≠ causalidad
  
Ejemplo: "Edad y gasto mensual" pueden estar correlacionados, pero eso no significa que la edad cause directamente más gasto.

### Regresión lineal
la **regresión lineal** busca **modelar matemáticamente la relación entre variables** para **predecir valores**.
#### 1. Regresión lineal simple
* Una varible independiente (X) -> predice una dependiente (Y).
* Ecuación:
  $$Y = \beta_0 + \beta_1X + \epsilon$$
Ejemplo: predecir `Gasto` a partir de `Ingresos`.
#### 2. Regresión lineal múltiple
* Varias variables independientes (X₁, X₂, …, Xn) -> predicen Y.
* Ecuación:
  $$Y = \beta_0 + \beta_1X_1 + \beta_0X_2 + ... + \beta_nX_n + \epsilon$$
Ejemplo: predecir `Gasto` en función de `Ingresos` y `Edad`.

### Ejemplo práctico en Python
```
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset ficticio
np.random.seed(42)
n=50
ingresos = np.random.normal(4000,1000,n)
edad = np.random.randint(20,60,n)
gasto = 500 + 0.4*ingresos + 5*edad + np.random.normal(0,500,n)

df = pd.DataFrame({"Ingresos":ingresos, "Edad":edad, "Gasto":gasto})

# --- Correlación ---
print(df.corr())

# --- Regresión lineal simple: Gasto ~ Ingresos ---
X = df[["Ingresos"]]
y = df["Gasto"]
modelo_simple = LinearRegression().fit(X,y)

print(f"Intercepto: {modelo_simple.intercept_}")
print(f"Coeficiente: {modelo_simple.coef_[0]}")

# --- Regresión lineal múltiple: Gasto ~ Ingresos + Edad ---
X_multi = df[["Ingresos","Edad"]]
modelo_multiple = LinearRegression().fit(x_multi,y)

print(f"Intercepto: {modelo_multiple.intercept_}")
print(f"Coeficientes: {modelo_multiple.coef_}")
```
Interpretación:
* En la regresión simple, el coeficiente de `Ingresos` indica cuanto aumenta el gasto por cada dolar extra de ingreso.
* En la regresión múltiple, los coeficientes de `Ingresos` y `Edad` muestran la contribución de cada variable al gasto.

### Mini - práctica
1. Crea un dataset ficticio con 60 observaciones:
   * `Horas_estudio` (entre 0 y 15).
   * `Nota_examen` (entre 0 y 100, que dependa en parte de las horas de estudio + ruido).
   * `Edad` (entre 18 y 30).
2. Calcula la **correlación** entre `Horas_estudio` y `Nota_examen`.
3. Ajusta una **regresión simple**: `Nota_examen ~ Horas_estudio`.
4. Ajusta una **regresión múltiple**: `Nota_examen ~ Horas_estudio + Edad`.
5. Interpreta si la edad influye en la nota cuando controlas las horas de estudio.

## Series de tiempo y modelos predictivos
### ¿Qué es una serie de tiempo?
Una **serie de tiempo** es una secuencia de observiaciones tomadas en momentos sucesivos (diarios, mensuales, anuales, etc.).

Ejemplos:
* Precio del dolar día a día.
* Consumo eléctrico por hora.
* Número de pacientes en un hospital cada semana.
El análisis de series de tiempo busca **identificar patrones** y **predecir valores futuros**.

### Componentes de una serie de tiempo
1. **Tendencia (T)**: dirección general (creciente, decreciente).
2. **Estacionalidad (S)**: patrones que se repiten regularmente (ej: más ventas en diciembre).
3. **Ciclo (C)**: fluctuaciones a largo plazo, no fijas (ej: crisis económicas).
4. **Ruido (R)**: variaciones aleatorias no explicables.

### Modelos básicos
1. ARIMA (AutoRegressive Integrated Moving Average)
   * **AR (AutoRegresivo)**: la serie depende de sus valores pasados.
   * **I (Integrado)**: se diferencia al serie para hacerla estacionaria.
   * **MA (Media Movil)**: usa errores pasados para mejorar predicciones.
Notación: **ARIMA(p, d, q)**
* p: número de términos autoregresivos.
* d: número de diferenciaciones necesarias para estacionarizar.
* q: número de medias móviles.
Ejemplo: ARIMA(1,1,1).

2. Prophet (Meta/Facebook)
   * Desarrollado por Facebook para pronósticos de negocio.
   * Ventajas:
      - Maneja bien **tendencias no lineales** y **estacionalidades múltiples**.
      - Facil de usar y automatiza muchos pasos que en ARIMA son manuales.
   * Ideal para datos con **estacionalidad fuerte** (por ejemplo: ventas con picos en ciertas temporadas).

### Ejemplo práctico con Python
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet

# Generamos una serie de tiempo ficticia (ventas mensuales con estacionalidad)
np.random.seef(42)
fechas = pd.date_range(start="2020-01-01", periods=36, freq="M")
ventas = 100 + np.linspace(0,20,36) + 10*np.sin(np.arange(36)/6) + np.random.normal(0,5,36)

df = pd.DataFrame({"Fecha":fechas,"Ventas":ventas})

# --- ARIMA ---
modelo_arima = ARIMA(df['Ventas'], order=(1,1,1)).fit()
pred_arima = modelo_arima.predict(start=30, end=40, typ="levels")

plt.figure(figsize=(10,5))
plt.plot(df['Fecha'], df['Ventas'], label="Ventas reales")
plt.plot(df['Fecha'].iloc[30:], pred_arima, label="Precicción ARIMA", linestyle="--")
plt.legend()
plt.show()

# --- Prophet ---
df_prophet = df.rename(columns={"Fecha": "ds", "Ventas": "y"})
modelo_prophet = Prophet().fit(df_prophet)
futuro = modelo_prophet.make_future_dataframe(periods=6, freq="M")
pronóstico = modelo_prophet.predict(futuro)

modelo_prophet.plot(pronostico)
plt.show()
```
Interpretación:
* ARIMA requiere que ajustemos manualmente (p, d, q).
* Prophet detecta automáticamente tendencia y estacionalidad.

### Mini - práctica
1. Crea una serie de tiempo ficticia con **datos diarios de temperatura durante 2 años** con algo de estacionalidad (ej: más calor en junio-julio).
2. Ajusta un modelo **ARIMA** y observa si logra capturar la estacionalidad.
3. Ajusta un modelo con **Prophet** y compara la predicción.
4. Reflexiona: ¿Cuál modelo capturó mejor los patrones?.

## Proyecto Integrador (Análisis Inferencial)
1. Dataset
   * Seleccionamos un dataset de kaggle (ej: **Student Performance Dataset** o un de **Customer Spending**).
   * Debe tener variables númericas (edad, ingresos, gasto) y categóricas (género, nivel educativo, preferencia).
2. Prueba de hipótesis
   * Ejemplo: ¿Gastan mas los hombres que la mujeres? (t-test).
   * Ejemplo: ¿Existen diferencias de gasto entre tres niveles educativos? (ANOVA).
   * Ejemplo: ¿la experiencia de producto depende del género? (chi-cuadrado).
3. Correlación y regresión
   * Calcular **correlaciones** entre edad, ingresos, gasto.
   * Ajustar una **regresión simple** (ej: gasto ~ ingresos).
   * ajustar una **regresión múltiple** (ej: gasto ~ ingresos + edad).
4. Series de tiempo (si el dataset tiene fechas)
   * Reportar qué hipótesis se rechazaron y qué patrones se encontraron.
   * Explicar si hay correlaciones fuertes y si los modelos de predicción funcionaron.