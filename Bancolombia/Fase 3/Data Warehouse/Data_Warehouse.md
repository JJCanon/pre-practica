# Data Warehouse
### ¿Qué es un Data Warehouse?
un **Data Warehouse (DW)** es una **base de datos centralizada** diseñada para almacenar grandes volúmenes de datos históricos de diferentes fuentes, con el fin de analizarlos y obtener información para la toma de desiciones.
* A diferencia de una **base de datos transaccional** (OLTP, como se usan los sistemas de ventas o bancarios), un DW está optimizado para consultas analíticas (OLAP).
* se utilizan en **Business Intelligence (BI)** y **reportes ejecutivos**.
Ejemplo:
- Una empresa puede tener datos de ventas en un sistema, datos de clientes en otro, y datos financieros en otro. El **DW consolida todo** en un solo lugar para analizar métricas como ventas por región, rentabilidad, tendencias en el tiempo, etc.
### Componentes clave de una Data Warehouse
* **Fuentes de datos** -> sistemas transaccionales, archivos, APIs.
* **ETL** -> extrae, transforma y carga la información hacia el DW.
* **Modelado dimensional** -> forma de organizar los datos para análisis eficiente.
* **Herramientas de BI** -> Power BI, Tableau, Looker, etc., que se conectan al DW para crear dashboards.
### Modelado dimensional
La forma más común de organizar los datos en un DW es mediante **esquemas dimensionales**:
1. **Star Schema (Esquema en estrella)**
   * Una tabla central de **hechos** (ej:ventas).
   * Varias tablas **dimensión** que describen los hechos (ej:clientes, productos, tiempo, regiones).
   * Rápido y simple para consultas.
    Ejemplo:
    ```scss
    HechosVentas (id_venta, id_cliente, id_producto, id_tiempo, monto)
    DimCliente (id_cliente, nombrem ciudad, edad)
    DimProducto (id_producto, categoría, precio)
    DimTiempo (id_tiempo, fecha, mes, año)
    ```
2. Snowflake Schema (Esquema en copo de nieve)
   * ES similar al **star schema**, pero sobre las dimensiones están normalizadas en varias tablas.
   * Consume menos espacio, pero las consultas son más complejas.
### Integración con Power BI
* Una vez los datos están en el DW (ej: PostgreSQL, MySQL, Redshift, BigQuery), **Power BI se conecta directamente** y permite crear dashboards que se actualizan según las tablas de DW.
* Así, si el pipeline ETL se ejecuta cada noche, Power BI muestra los datos más recientes al día siguiente.

## Modelado dimensional
El **modelado dimensional** el la técnica más usada en el diseño de Data Warehouses porque permite que los datos sean fáciles de consultar y analizar.
#### Dos tipos principales de tablas
1. Tabla de hechos (Fact Table)
   * Contiene **medidas numéricas** (valores que se analizan).
   * Ejemplo: monto de ventas, cantidad vendida, tiempo de engrega.
   * Suele ser muy grande, con millones de filas.
2. Tablas de dimensiones (Dimension Tables)
   * Contienen **atributos descriptivos** que dan contexto a los hechos.
   * Ejemplo: clientes, productos, fechas, regiones.
   * Normalmente son más pequéñas y más fáciles de mantener.

#### Star Schema (Esquema en estrella)
* Una **tabla de hechos central** conectada directamente a varias tablas de dimensiones.
* Es simple, rápido y el más usado en BI.
  Ejemplo: Ventas
```lua
                   DimCliente
                      |
                 DimProducto
                      |
DimTiempo ---- FactVentas ---- DimRegion
```
* **FactVentas**: id_cliente, id_producto, id_tiempo, id_region, cantidad, monto
* **DimCliente**: id_cliente, nombre, ciudad, edad
* **DimProducto**: id_producto, categoría, precio
* **DimTiempo**: id_tiempo, fecha, mes, año
* **DimRegion**: id_region, país, ciudad

#### Snowflake Schema (Esquema en copo de nieve)
* Similar al **star schema**, pero las **dimensiones están normalizadas** (divididas en más tablas).
* Menos redundancia, pero consultas más lentas.
Ejemplo: Ventas con snowflake
```lua
                 DimCiudad ---- DimRegion
                        |
                 DimCliente
                        |
DimTiempo ---- FactVentas ---- DimProducto ---- DimCategoria
```
#### Diferencia clave
| Característica        | Star Schema ⭐  | Snowflake ❄                        |
| --------------------- | -------------- | ---------------------------------- |
| Simplicidad           | Alta           | Media-baja                         |
| Rendimiento consultas | Rápido         | Más lento                          |
| Redundancia           | Más alta       | Menor                              |
| Uso típico            | BI, dashboards | Sistemas con millones de registros |

### Ejemplo práctico con tablas (Star Schema)
Supongamos que diseñamos un DW para un **supermercado**:
1. Tabla de hechos: `FactVentas`
```sql
id_venta | id_cliente | id_producto | id_tiempo | cantidad | monto
-----------------------------------------------------------------
1        | 101        | 501         | 20240110  | 2        | 50.00
2        | 102        | 502         | 20240111  | 1        | 30.00
```
2. Tabla de dimensiones: `DimCliente`
```sql
id_cliente | nombre   | ciudad
--------------------------------
101        | Juan     | Medellín
102        | Ana      | Bogotá
```
3. Tabla de dimensiones: `DimProducto`
```sql
id_producto | nombre   | categoria   | precio
----------------------------------------------
501         | Arroz    | Granos      | 25.00
502         | Leche    | Lácteos     | 30.00
```
4. Tabla de dimensiones: `DimTiempo`
```sql
id_tiempo | fecha       | mes  | año
------------------------------------
20240110  | 2024-01-10  | Ene  | 2024
20240111  | 2024-01-11  | Ene  | 2024
```
Con esto ya tendrías un **esquema en estrella** simple que soporta como:
* Ventas por cliente.
* Ventas por categoría de producto.
* Ventas por mes o año.
### Mini - práctica
Imagina que tu empresa quiere un **Data Warehouse para analizar ventas por cliente, ciudad y tiempo**.
- Definimos la Tabla de Hechos
   - FactVentas
    Contendrá las métricas numéricas (hechos) de las ventas.
    | id\_venta | id\_cliente | id\_tiempo | cantidad | monto |
    | --------- | ----------- | ---------- | -------- | ----- |
    | 1         | 101         | 20240110   | 2        | 200   |
    | 2         | 102         | 20240111   | 1        | 150   |
    | 3         | 103         | 20240112   | 3        | 450   |
- Definimos las Tablas de Dimensiones
   - DimCliente
    Información descriptiva de los clientes.
    | id\_cliente | nombre | ciudad   | correo                                    |
    | ----------- | ------ | -------- | ----------------------------------------- |
    | 101         | Juan   | Medellín | [juan@email.com](mailto:juan@email.com)   |
    | 102         | Ana    | Bogotá   | [ana@email.com](mailto:ana@email.com)     |
    | 103         | Pedro  | Cali     | [pedro@email.com](mailto:pedro@email.com) |
   -  DimTiempo
    Permite analizar las ventas por fecha, mes año.
    | id\_tiempo | fecha      | mes | año  |
    | ---------- | ---------- | --- | ---- |
    | 20240110   | 2024-01-10 | 01  | 2024 |
    | 20240111   | 2024-01-11 | 01  | 2024 |
    | 20240112   | 2024-01-12 | 01  | 2024 |
- Esquema en estrella resultante
   ```lua
             DimCliente
                |
    DimTiempo — FactVentas

   ```
   * FactVentas contiene las metricas (`cantidad`,`monto`).
   * DimCliente agrega contexto de quién compró.
   * DimTiempo permite análisis temporar (por día, mes año).
- Preguntas que se pueden responder con este modelo:
   * ¿Cuál fue el monto total de ventas por ciudad?
   * ¿Cuántas ventas se hicieron en enero de 2024?
   * ¿Qué cliente gastó más dinero en el último mes?

1. A partir de tus datasets (`ventas.csv` y `clientes.xlsx`), diseña un **Star Schema** que te permita responder preguntas como:
   * ¿Qué productos se vendieron más por ciudad?
   * ¿Cuál fue el cliente con más compras en el año?
2. Crea las tablas en SQL:
   * `FactVentas`
   * `DimCliente`
   * `DimTiempo`
3. LLena esas tablas con tus datos ya transformados (desde tu pipeline ETL).
* Crear esquema opcional para organizar el DW
```sql
CREATE SCHEMA IF NOT EXISTS dw;
```
Tablas de dimensiones
a. DimCliente
```sql
CREATE TABLE IF NOT EXISTS dw.DimCliente (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100),
    correo VARCHAR(150)
);
```
b. DimTiempo
```sql
CREATE TABLE IF NOT EXISTS dw.DimTiempo (
    id_tiempo INT PRIMARY KEY,
    fecha DATE NOT NULL,
    mes INT,
    anio INT
);
```
c. DimProducto
```sql
CREATE TABLE IF NOT EXISTS dw.DimProducto (
    id_producto SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    categoria VARCHAR(50),
    precio NUMERIC(10,2)
);
```
Tabla de hechos
* FactVentas
```sql
CREATE TABLE IF NOT EXISTS dw.FactVentas (
    id_venta SERIAL PRIMARY KEY,
    id_cliente INT REFERENCES dw.DimCliente(id_cliente),
    id_tiempo INT REFERENCES dw.DimTiempo(id_tiempo),
    id_producto INT REFERENCES dw.DimProducto(id_producto),
    cantidad INT,
    monto NUMERIC(12,2)
);
```
Inserciones de prueba
```sql
-- Insertar clientes
INSERT INTO dw.DimCliente (nombre, ciudad, correo) VALUES
('Juan', 'Medellín', 'juan@email.com'),
('Ana', 'Bogotá', 'ana@email.com'),
('Pedro', 'Cali', 'pedro@email.com');

-- Insertar fechas
INSERT INTO dw.DimTiempo (id_tiempo, fecha, mes, anio) VALUES
(20240110, '2024-01-10', 1, 2024),
(20240111, '2024-01-11', 1, 2024),
(20240112, '2024-01-12', 1, 2024);

-- Insertar productos (opcional)
INSERT INTO dw.DimProducto (nombre, categoria, precio) VALUES
('Arroz', 'Granos', 25.00),
('Leche', 'Lácteos', 30.00);

-- Insertar ventas
INSERT INTO dw.FactVentas (id_cliente, id_tiempo, id_producto, cantidad, monto) VALUES
(1, 20240110, 1, 2, 50.00),
(2, 20240111, 2, 1, 30.00),
(3, 20240112, 1, 3, 75.00);
```
Consultas de ejemplo
```sql
-- Total de ventas por ciudad
SELECT c.ciudad, SUM(f.monto) AS total_ventas
FROM dw.FactVentas f
JOIN dw.DimCliente c ON f.id_cliente = c.id_cliente
GROUP BY c.ciudad;

-- Total de ventas por mes
SELECT t.mes, t.anio, SUM(f.monto) AS total_ventas
FROM dw.FactVentas f
JOIN dw.DimTiempo t ON f.id_tiempo = t.id_tiempo
GROUP BY t.mes, t.anio;
```
## Integración con Power BI
Power BI es una de las herramientas más usadas para **visualización y análisis de datos**.
En un flujo de **ETL + Data Warehouse**, el papel de Power BI es:
1. **Conectarse al Data Warehouse** (ej: PostgreSQL, MySQL, Redshift, BigQuery).
2. **Importar o consultar datos en tiempo real**.
3. **Construir dashboards interactivos** con métricas clave.
4. **Actualizar automáticamente** cuando el pipeline ETL cargue nuevos datos en el DW.
Esto convierte los datos crudos en **información accionable para el negocio**.
### Formas de conexión de Power BI a un DW
1. Import Mode (modo importación)
   * Los datos se copian dentro de Power BI.
   * Consultas muy rápidas.
   * Requiere actualizar manualmente o programar actualizaciones.
2. DirectQuery (consulta directa)
   * Power BI consulta la base en tiempo real.
   * Los dashboards siempre muestran datos frescos.
   * Puede ser más lento si la base es muy grande.
En proyectos académicos/prácticos, lo más sencillo es usar **Import Mode** con actualizaciones automáticas cada cierto tiempo.
### Ejemplo práctico con PostgreSQL
1. Habilitar el conector
   * Instalar el conector oficial de PostgreSQL en Power BI.
   * En Windows, instalar PostgresSQL ODBC driver.
2. Conectar Power BI a PostgreSQL
   * En Power BI:
    `Inicio -> Obtener datos -> Base de datos -> PostgreSQL`.
   * Introducir:
     - Servidor: `localhost`
     - Base de datos: `etl_practica` (o `dw`)
     - Usuario y contraseña.
3. Seleccionar tablas
   * Escoger `FactVentas`, `DimCliente`, `DimTiempo`, `DimProducto`.
   * Power BI reconoce las relaciones automáticamente si tienen claves foráneas.
4. Modelar datos en Power BI
   * Revisar el diagrama de relaciones -> debería verse como un **esquema en estrella**.
   * Crear medidas con DAX, por ejemplo:
    ```DAX
    TotalVentas = SUM(FactVentas[monto])
    VentasPromedio = AVERAGE(FactVentas[monto])
    ```
5. Construir Dashboard
   * Ejemplos de visualizaciones:
     * Gráfico de barras: ventas por ciudad.
     * Gráfico de líneas: ventas por mes.
     * Tarjeta: cliente con más compras.
6. Actualizar automáticamente
   * Configurar actualización programada (ej: cada 24h).
   * Así, cuando tu **pipeline ETL cargue datos nuevos en PostgreSQL**, Power BI los reflejará automáticamente.
### Ejercicio práctico
1. Tener listo el Data Warehouse
ya tienes el script SQL que define:
* DimCliente
* DimProducto
* DimTiempo
* FactVentas
- Asegúrate de:
    1. Haber creado la base de datos (ej: `dw_practica` en PostgreSQL).
    2. Tener algunos datos cargados (puedes insertar manualmente o con tu pipeline ETL).
2. Conectar Power BI a PostgreSQL
   1. Abre Power BI Desktop.
   2. Haz clic en Inicio -> Obtener datos -> Más.
   3. Busca PostgreSQL database y selecciona.
   4. Conéctate con:
      1. Servidor: `localhost` (o la IP de tu servidor si está en la nube).
      2. Base de datos: `dw_practica`.
      3. Usuario y contraseña
Si no aparece la opción de PostgreSQL, necesitas instalar el conector (driver)
3. Seleccionar tablas
   1. importa: `FactVentas`,`DimCliente`,`DimProducto`, `DimTiempo`.
   2. Power BI debería reconocer automáticamente las relaciones (fact -> dimensiones) gracias a las claves foráneas.
   3. Si no, conéctalas manualmente:
      1. `FactVentas.idCliente` → `DimCliente.idCliente`
      2. `FactVentas.idProducto` → `DimProducto.idProducto`
      3. `FactVentas.idTiempo` → `DimTiempo.idTiempo`
Esto es un esquema estrella dentro de power BI.
4. Crea medida con DAX:
En la pestaña de datos o modelado, crea medidas:
```DAX
TotalVentas = SUM(FactVentas.monto)
PromedioVentas = AVERAGE(FactVentas.monto)
```
5. Construir el dashboard
   1. Tarjeta -> Muestra el `TotalVentas`.
   2. Gráfico de barras -> Ventas por `DimCLiente.ciudad`.
   3. Gráfico de lineas -> Ventas por `DimTiempo.mes`.
   4. Tabla -> Detalle con cliente, producto y monto.
Ahora ya tienes un dashboard interactivo basado en tu Data Warehouse.
6. Automatizar actualización
   1. Si tu pipeline ETL carga datos nuevos en `FactVentas`, power BI debe reflejarlos.

## Herramientas como Google BigQuery o AWS Redshift
### Herramientas cloud para Data Warehousing: BigQuery y Redshift
Cuando hablamos de **Data Warehousing en la nube**, dos de las herramientas más usadas en entornos empresariales son:
* Google BigQuery
  * Servicio de **Data Warehousing serverless** (no necesitas gestionar servidores).
  * Basado en SQL estándar.
  * Escala automáticamente según la carga de consultas.
  * Se paga **por almacenamiento y por consulta** (ej: $5 por TB procesado).
  * Muy integrado con el ecosistema de google cloud (Data Studio, IA Platform, looker).
* Amazon Redshift
  * Data Warehouse de **Amazon Web Services**.
  * Permite manejar **petabytes de datos**.
  * Basado en clústeres -> puedes elegir el tamaño y escalabilidad.
  * Compatible con SQL estándar y con herramientas BI como Power BI y Tableau.
  * Se paga **por hora de uso de clúster** o con Redshift Serverless.

- **BigQuery** es más fácil de empezar porque no gestionas nada.
- **Redshift** te da más control (pero requiere manejar clústeres).
### Ejemplo práctico (simulado con BigQuery)
Suponemos que tenemos nuestra tabla `FactVentas` en PostgreSQL y queremos **Subirla a BigQuery**.
1. Exportar datos a CSV con Python
```Python
import pandas as pd
import psycopg2

# Conexión a PostGreSQL
conn = psyconpg2.connect(
    dbname="dw_practica",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)

# Extraer datos de PostgreSQL
df = pd.read_sql('SELECT * FROM factventas', conn)

# Guardar en CSV
df.to_csv("factventas.csv",index=False)

conn.close()
```
2. Subir a BigQuery
Con la CLI de Google Cloud:
```bash
bq load --autodetect --source_format=CSV \ mi_dataset.FactVentas factventas.csv
```
Esto crea la tabla `FactVentas` en BigQuery con detección automática de esquemas.
3. Consulta en BigQuery
En la consola web de BigQuery:
```sql
SELECT idCliente, SUM(monto) AS total_ventas
FROM `mi_proyecto.mi_dataset.FactVentas`
GROUP BY idCliente
ORDER BY total_ventas DESC;
```
ya tendrías tu tabla de ventas en la nube lista para conectar a Power BI o Looker.
### Mini - práctica 
1. Toma tu tabla `FactVentas` de PostgreSQL.
2. Expórtala a un CSV con Python.
3. Simula que la subes a la nube:
   * Crea un nuevo esquema dw_cloud en PostgreSQL y carga ahí el CSV allí, como si fuera tu "Data Warehouse en la nube".
4. Haz una consulta SQL de ejemplo sobre esa tabla para obtener:
   * Top 3 clientes con más ventas.
   * Ventas totales por mes.