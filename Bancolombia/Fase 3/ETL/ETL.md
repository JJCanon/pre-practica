# ETL
## ¿Qué es ETL?
ETL significa **Extract, Transform, Load** (Extraer, Transformar, Cargar).
Es un proceso muy usado en **Data Engineering y Business Intelligence** para mover datos desde diferentes fuentes (archivos, bases de datos, APIs, etc.), limpiarlos o transformarlos, y luego cargarlos en un sistema central (por ejemplo, un **Data Warehouse** o una base de datos).
* **Extract (Extraer)**: Obtener datos de distintas fuentes (CSV, Excel, APIs, bases de datos).
* **Transform (Transfomar)**: Limpiar, normalizar, estandarizar y enriquecer los datos.
* **Load (Cargar)**: Guardar los daots transformados en un destino (una base de datos, almacenamiento en la nube, o un Data Warehouse).
Python es una herramienta ideal para ETL porque tiene librerías muy poderosas como:
* **Pandas** (para manipulación de datos).
* **SQLAlchemy / psycopg2 / mysql-connector** (para conexión con bases de datos).
* **schedule / cron jobs** (para automatización).

## Uso de Pandas para extracción, limpieza y carga
**Pandas** es la librería más usada en Python para análisis y manipulación de datos. Dentro de un flujo de ETL, cumple un rol clave en:
* **Extracción (Extract):** leer datos desde diferentes fuentes:
  - Archivos: CSV, Excel, JSON, Parquet.
  - Bases de datos: usando `read_sql`.
  - APIs: con request + pandas.
* **Transformación (Transform):**
  - Limpieza de datos (valores nulos, duplicados, outliers).
  - Normalización de formatos (fechas, mayúsculas/minúsculas, tipos de datos).
  - Creación de nuevas columnas calculadas.
  - Unión de múltiples fuentes (merge, concat, join).
* **Carga (Load):**
  - Guardar datos en archivos: `to_csv()`,`.to_excel()`,`.to_parquet()`.
  - Insertar datos en bases de datos (PostgreSQL, MySQL).
  - Preparar datasets para visualización en Power BI o Tableau.

### Ejemplo práctico
Supongamos que tenemos un archivo ventas.csv con datos sucios:
```csv
id,nombre,fecha,venta
1,Juan,2024-01-10,100
2,Ana,2024-01-11,200
3,Pedro,2024/01/12,NaN
4,juan,2024-01-13,150
```
Podemos aplicar Pandas en un mini-ETL:
```Python
import pandas as pd

# 1. Extracción
df = pd.read_csv("ventas.csv")

# 2. Transformación
# Normalizar nombre (capitalizar)
df['nombre'] = df['nombre'].str.capitalize()

# Arreglar formato de fecha
df['fecha'] = pd.to_datatime(df['fecha'],errors='coerce')

# Rellenar valores nulos
df['venta'] = df['venta'].fillna(df['venta'].mean())

# Eliminar duplicados en ID
df = df.drop_duplicates(subset="id")

# 3. Carga
df.to_csv("ventas_limpias.csv",index=False)
print(df)
```
Resultado (archivo limpio `ventas_limpias.csv`):
```csv
id,nombre,fecha,venta
1,Juan,2024-01-10,100.0
2,Ana,2024-01-11,200.0
3,Pedro,2024-01-12,150.0
4,Juan,2024-01-13,150.0
```
### mini - práctica
1. Crea un archivo CSV ficticio llamado `clientes.csv` con estas columnas:
   * `id`,`nombre`,`ciudad`,`edad`,`correo`.
   * Introduce errores: algunos correos mal escritos, edades negativas o nulas, nombres en mayúsculas/minúsculas mezcladas.
2. Escribe un script en Python con Pandas que:
   * Lea el CSV.
   * Corrija los nombres (primera letra en mayúscula).  
   * Reemplace las edades negativas o nulas por la media de las edades válidas.
   * Valide los correos (si no tienen `@`, márcalos como `"correo_invalido"`).
   * Guarde el dataset limpio en un nuevo CSV.

## Automatización con scripts programados
En un entorno real, los procesos ETL no se ejecutan manualmente cada vez, sino que deben correr **automáticamente** en intervalos de tiempo definidos (ejemplo: cada noche, cada hora, cada semana).

Existen varias formas de lograr esta **automatización**:
1. Tareas programadas en el sistema operativo
   * **Windows**: Task Scheduler.
   * **Linux/Mac**: `cron`.
2. Automatización dentro de Python
   * Librerías como `schedule` o `APScheduler` permiten definir tareas periódicas sin depender del sistema operativo.
   * Útil para pruebas locales o procesos simples.
3. Orquestadores de ETL más avanzados (ya nivel empresarial)
   * **Airflow, Luigi, Prefect** -> permiten manejar dependencias, monitoreo, reintentos y notificaciones.
   * Esto ya entra en el terreno de __Data Engineering__ profesional.
En esta fase, nos enfocaremos en la **automatización básica** con **Python** y `schedule`.

### Ejemplo práctico
Supongamos que queremos ejecutar nuestro ETL (leer un CSV, limpiarlo y guardarlo) **cada 10 segundos**.
```Python
import pandas as pd
import schedule
import time

def etl_job():
    print('Ejecutando ETL...')

    # Extracción
    df = pd.read_csv('ventas.csv')

    # Transformación
    df['nombre'] = df['nombre'].str.capitalize()
    df['fecha'] = pd.to_datetime(df['fecha'],errors='coerce')
    df['venta'] = df['venta'].fillna(df['venta'].mean())

    # Carga
    df.to_csv('ventas_limpias.csv',index=False)
    print('ETL completado y datos guardados')

# Programar ejecución cada 10 segundos
schedule.every(10).seconds.do(etl_job)

# Mantener el script corriendo
while True:
    schedule.run_pending()
    time.sleep(1)
```
* Explicación:
  + `schedule.every(10).seconds.do(etl_job)` -> ejecuta la función cada 10 segundos.
  + El bucle `while True` mantiene el script vivo, verificando cada segundo si hay algo pendiente.

### Mini práctica
1. Toma tu script de clients.csv que hiciste en el subtema anterior.
2. Automatízalo para que se ejecute cada 1 minuto y guarde un archivo nuevo `clean_clients.csv`
3. Agrega un `print('ETL running at: 'current_time)` para verificar cuándo corre.

## Conexión a bases de datos
En un pipeline ETL, muchas veces el destino final de los datos no es un CSV, sino una **base de datos relacional** como **PostgreSQL** o **MySQL**, desde donde luego se podrán consumir en dashboards (Power BI, Tableau) o en un Data Warehouse.

Para trabajar con estas bases en Python se usan dos enfoques principales:
1. Conectores directos
   * `psycopg2` -> para PostgreSQL.
   * `mysql-connector-python` -> para MySQL.
   * Permiten ejecutar SQL directamente (`INSERT`,`SELECT`, etc.).
2. ORM / Abstracción con SQLAlchemy
   * Funciona como una "capa intermedia" que permite trabajar con Pandas y objetos en lugar de escribir SQL manual.
   * Muy útil para ETL porque Pandas puede escribir directamente en una base usando `to_sql()`.
### Ejemplo práctico con PostgreSQL
Supongamos que tenemos PostgreSQL corriendo localmente y queremos **cargar el CSV limpio a la base**.
Paso 1. Instalar dependencias
```bash
pip install psycopg2-binary sqlalchemy
```
Paso 2. Conexión y carga con Pandas
```Python
import pandas as pd
from sqlalchemy import create_engine

# Datos de conexión
usuario = 'postgres'
password = 'tu_password'
host = 'localhost'
puerto = '5432'
base_datos = 'etl_db'

# Crear motor de conexión
engine = create_engine(f"postgresql://{usuario}:{password}@{host}:{puerto}/{base_datos}")

# Leer CSV limpio
df = pd.read_csv("ventas_limpias.csv")

# Cargar en tabla 'ventas' (si no existe la crea)
df.to_sql('ventas',engine,if_exists='replace',index=False)

print("Datos cargados en PostgreSQL correctamente")
```
Esto crea o reemplaza la tabla `ventas` en la base de datos `etl_db`.

### Ejemplo práctico con MySQL
Solo cambia la librería y la cadena de conexión:
```bash
pip install mysql-connector-python
```
```python
from sqlalchemy import create_engine

usuario = 'root'
password = 'tu_password'
host = 'localhost'
puerto = '3306'
base_datos = 'etl_db'

engine = create_engine(f"mysql+mysqlconnector://{usuario}:{password}@{host}:{puerto}/{base_datos}")
```
### Mini práctica
1. Crea una base de datos llamada **etl_practica** en PostgreSQL o MySQL.
2. usa tu dataset limpio de `clients.csv`.
3. Escribe un script en Python que lo cargue en una tabla llamada **clientes_limpios**.
4. Haz una consulta en la base (`SELECT * FROM clean_clients;`) para verificar que los datos fueron insertados.

## Proyecto Integrador
Datos de entrada:
* `sales.csv`.
  ```csv
   id,nombre,fecha,venta
   1,juan,2024-01-10,100
   2,Ana,2024-01-11,200
   3,pedro,2024/01/12,NaN
   4,JUAN,2024-01-13,150

  ```
* `clients.xlsx`.
  | id  | nombre\_cliente | ciudad   | correo                                      |
  | --- | --------------- | -------- | ------------------------------------------- |
  | 1   | Maria           | Medellín | maria\_gmail.com                            |
  | 2   | Andres          | Bogotá   | [andres@gmail.com](mailto:andres@gmail.com) |
  | 3   | carlos          | Cali     | [carlos@yahoo.com](mailto:carlos@yahoo.com) |

1. Cada minuto se ejecuta el ETL.
2. Extrae datos de **CSV (ventas) y Excel (clientes)**.
3. Transforma los datos:
   * Normalize nombres.
   * Corrige fechas y NaN en ventas.
   * Valida correos en clientes.
4. Carga los datos limpios en PostgreSQL en las tablas:
   * `ventas`
   * `clientes`
5. Ejecuta el request:
   ```sql
   SELECT * FROM ventas;
   sELECT * FROM clientes;
   ```
   Se deben ver los datos limpios y normalizados