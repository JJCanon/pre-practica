# Dataset
World Bank Projects & Operations Data
Datos del Banco Mundial que permiten trabajar con CSVs complejos y variados.
Enlace: World Bank Data ETL en Kaggle [kaggle](https://www.kaggle.com/datasets/johnymariah/world-bank-data-etl?utm_source=chatgpt.com)

# Instrucciones
1. Preparación
   * Crea un repositorio en GitHub.
   * clona este repositorio en tu máquina local.
   * Dentro del repo, crea la siguiente estructura:
    ```bash
    etl-kaggle-project/
    ├── data/
    │   ├── sales.csv         # del dataset Sample Sales Data
    │   └── worldbank.xlsx    # del World Bank
    ├── etl/
    │   ├── extract.py
    │   ├── transform.py
    │   └── load.py
    ├── requirements.txt
    └── README.md
    ```
2. ETL paso a paso
   1. Extract
      1. Descarga el dataset desde kaggle y colócalos en la carpeta `data/`.
      2. implementa lectura de archivos usando pandas.
   2. Transform
      1. realiza la limpieza/normalización, por ejemplo:
         1. Filtrar columnas importantes.
         2. Convertir fechas con `pd.to_datetime()`.
         3. Eliminar registros duplicados o NaN.
   3. Load
      1. Conecta con PostgreSQL usando SQLAlchemy y pandas.
      2. En tu script principal orquesta el flujo.
      3. Añade este proyecto a tu repositorio, incluyendo `requeriments.txt` y `README.md`.
3. Conexión con Power BI
   1. Abre Power BI Desktop.
   2. Selecciona **Obtener datos** -> **PostgreSQL**.
   3. Conéctate a tu base `etl_db`, e importa las tablas.
   4. Crea visualizaciones.
   5. Crea medidas DAX.
4. Publica tu proyecto en GitHub
Asegurate de subir tu repositorio completo. En tu README.md incluye:
    * Descripción del proyecto.
    * Enlaces a los datasets de Kaggle:
      * Sample Sales Data.
      * World Bank Data ETL.
    * Instrucciones para ejecutar ETL localmente.
    * Cómo conectar Power BI y ver el dashboard.
    * Instrucciones para ejecutar el script principal.