# Project
1. Análisis descriptivo y diagnóstico
- Importar dataset y explorar: .head(), .info(), .describe().
- Calcular medidas de tendencia central y dispersión para variables como age, balance, duration.
- Detección de outliers con IQR y desviación estándar.
- Visualizaciones:
    * Histogramas (age, balance).
    * Boxplots (comparar balance por marital, education).
    * Scatterplots (age vs balance).
2. Prueba de hipótesis sobre variables relevantes
- Ejemplos de hipótesis a comprobar:
  1. Balance promedio por género
    * H₀: no hay diferencia en el balance promedio entre hombres y mujeres.
    * Test: t-test de dos muestras.
  2. Balance promedio por nivel educativo
    * H₀: el balance promedio es igual en todos los niveles educativos.
    * Test: ANOVA.
  3. Suscripción al producto según estado civil
    * H₀: la decisión de suscribir es independiente del estado civil.
    * Test: Chi-cuadrado.
3. Modelos predictivos simples
   * Clasificación → predecir si el cliente suscribirá (yes/no).
     - Modelos candidatos: Regresión logística, Árbol de decisión.
     - Métricas: Accuracy, F1-score, matriz de confusión.
   * Regresión → predecir una variable numérica como balance o duration.
     - Modelo candidato: Regresión lineal simple/múltiple.
     - Métricas: MSE, R².
4. Documentación
   * Usa un Jupyter Notebook bien estructurado con secciones:
     - Introducción.
     - Carga y exploración de datos
     - Análisis descriptivo.
     - Pruebas de hipótesis.
     - Modelados predictivos.
     - Conclusiones.
   * Sube el notebook a un nuevo repositorio en GitHub con:
     - README explicando dataset, pasos y resultados.
     - Notebook (financial-analysis.ipynb).
     - Requisitos (requirements.txt).