# Power BI for Data Science

## 1. Conexión a fuentes de datos en Power BI
En Power BI, el primer paso para cualquier proyecto es conectarse a la fuente de datos.
Power BI soporta muchas fuentes, entre ellas:
* Archivos locales: Excel, CSV, TXT.
* Bases de datos: SQL Server, MySQL, PostgreSQL, Oracle, etc.
* Servicios en la nube: Azure, Google BigQuery, AWS Redshift.
* APIs y Web: conectarse a URLs con datos en JSON, XML o HTML.

👉 Una vez que nos conectamos, podemos elegir cargar los datos directamente o pasar primero por Power Query, que permite limpiarlos y transformarlos antes de llevarlos al modelo.

### Ejemplos
#### Ejemplo 1 – Conexión a un archivo CSV
1. Abrir Power BI Desktop.
2. Ir a Inicio > Obtener datos > Texto/CSV.
3. Seleccionar el archivo ventas_powerbi.csv.

4. Power BI mostrará una vista previa de la tabla.
5. Puedes:
    * Cargar directamente al modelo.
    * Transformar datos (abre Power Query).

#### Ejemplo 2 – Conexión a Excel
1. Ir a Inicio > Obtener datos > Excel.
2. Seleccionar el archivo .xlsx.
3. Elegir la hoja de datos.

#### Ejemplo 3 – Conexión a SQL Server
1. Ir a Inicio > Obtener datos > SQL Server.
2. Escribir:
   * Servidor: dirección IP o nombre del servidor.
   * Base de datos: nombre de la BD.
3. Seleccionar tablas o escribir una consulta SQL.

### Ejercicio práctico
Usaremos el archivo `ventas_powerbi.csv`:
1. Abre Power BI Desktop.
2. Haz clic en Inicio > Obtener datos > Texto/CSV.
3. Busca el archivo `ventas_powerbi.csv` (el que te compartí antes).
4. En la ventana de vista previa:
   * Verifica que los campos se carguen bien (por ejemplo, Fecha se detecta como date y MontoTotal como decimal).
5. Elige:
   * Cargar: para llevarlo al modelo directamente.
   * Transformar datos: para abrir Power Query y revisar la calidad de las columnas.


## 2. Transformacion de datos con Power Query.
Cuando conectamos datos en Power BI, rara vez vienen "limpios".
Aqui entra Power Query, un editor integrado en Power BI que permite:
1. Corregir valores nulos o faltantes.
2. Cambiar tipos de datos (texto, número, fecha, etc.).
3. Filtrar filas y columnas.
4. Dividir o combinar columnas.
5. Crear columnas calculadas.
6. Unir o combinar tablas.
👉 Lo importante: las transformaciones en Power Query no modifican el archivo original, solo generan pasos en un “historial” que Power BI aplica cada vez que refrescas los datos.

### Ejemplos prácticos de transformación
Supongamos que cargamos `ventas_powerbi.csv`:

#### Ejemplo 1 – Revisar y cambiar tipos de datos
* La columna Fecha puede venir como texto → se convierte en Date.
* La columna MontoTotal debe estar en Decimal Number.

#### Ejemplo 2 – Eliminar nulos
* Si en Región hay valores vacíos, se pueden reemplazar por `"Desconocido"` o eliminarlos.

#### Ejemplo 3 – Crear una columna calculada
* Columna: PrecioPromedio = MontoTotal / Cantidad.

#### Ejemplo 4 – Filtrar datos
* Solo mostrar transacciones de 2023 en adelante.

### Ejercicio práctico
Usa el archivo `ventas_powerbi.csv` en Power BI Desktop y sigue:
1. Abre Transformar datos (esto abre Power Query).
2. Haz las siguientes transformaciones:
   * Verifica que `Fecha` sea de tipo Fecha.
   * Asegúrate de que `MontoTotal` sea Decimal Number.
   * Reemplaza los valores nulos en la columna `Región` con `"Sin región"`.
   * Crea una nueva columna llamada PrecioPromedio con la fórmula:
    ```
    PrecioPromedio = MontoTotal / Cantidad
    ```
    * Filtra para que solo aparezcan registros de 2023.
3. Aplica los cambios y regresa a Power BI.


## 3. Creación de visualizaciones y dashboards interactivos en Power BI.
Una vez que los datos están limpios y cargados en Power BI, pasamos a lo más poderoso: La visualización.

En Power BI puede crear:
* Gráficos de barras y columnas → comparar cantidades.
* Gráficos de líneas → analizar tendencias en el tiempo.
* Mapas → mostrar datos geográficos (por región, ciudad, país).
* Tablas y matrices → detalle de transacciones.
* Tarjetas → indicadores clave (KPI), como ventas totales o número de clientes.
* Slicers (segmentadores) → filtros interactivos (por año, región, producto).

👉 Lo importante es combinar varias visualizaciones en un dashboard interactivo, donde el usuario pueda filtrar, explorar y entender los datos fácilmente.

### Ejemplos
Supongamos que cargamos el dataset ya transformado.
Podemos crear un dashboard con:
1. Tarjetas:
   * Ventas totales (`MontoTotal`).
   * Total de productos vendidos (`Cantidad`).
2. Gráfico de barras:
   * Ventas totales por región (`Región` en eje, `MontoTotal` como valor).
3. Gráfico de líneas (serie de tiempo):
   * Ventas por mes (`Fecha` en el eje, `MontoTotal` como valor).
4. Mapa:
   * Ventas por región (`Región` en mapa).
5. Slicer (filtro):
   * Un segmentador por `Producto`.

### Ejercicio práctico
1. Abre tu archivo ventas_powerbi.csv en Power BI.
2. Realiza las siguientes visualizaciones:
   * Una tarjeta que muestre el total de ventas (`MontoTotal`).
   * Un gráfico de columnas con las ventas por `Región`.
   * Un gráfico de líneas que muestre cómo han evolucionado las ventas a lo largo del tiempo (`Fecha` vs `MontoTotal`).
   * Agrega un slicer para filtrar por `Producto`.
3. Combina todo en una sola página para tener un dashboard interactivo.

## 4. DAX básico (Data Analysis Expressions.)
DAX es el lenguaje de fórmulas en Power BI, similar a Excel, pero diseñado para trabajar con grandes volúmenes de datos y relaciones entre tablas.
Se usa principalmente para:
* Medidas (Measures): cálculos que se hacen sobre los datos (ejemplo: total de ventas, promedio, % de crecimiento).
* Columnas calculadas: nuevos campos creados a partir de columnas existentes.
* Tablas calculadas: cuando se necesitan subconjuntos de datos derivados.
Algunas funciones DAX más usadas:
* `SUM()`: suma de valores.
* `AVERAGE()`: promedio.
* `COUNT()` / `DISTINCTCOUNT()`: contar registros o valores únicos.
* `CALCULATE()`: aplicar filtros sobre una medida.
* `IF()` / `SWITCH()`: condiciones.
* `RELATED()`: traer valores de otra tabla relacionada.

### Ejemplo
Supongamos que tenemos nuestra tabla Ventas con columnas:
* `Fecha`, `Región`, `Producto`, `Cantidad`, `MontoTotal`.
Podemos crear estas medidas en Power BI:
1. Ventas Totales:
   ```
   Ventas Totales = SUM(Ventas[MontoTotal])
   ```
2. Cantidad Total de Productos Vendidos
   ```
   Cantidad Vendida = SUM(Ventas[Cantidad])
   ```
3. Promedio de Venta por Transacción
   ```
   Promedio Venta = AVERAGE(Ventas[MontoTotal])
   ```
4. Ventas en 2023 únicamente
   ```
   Ventas 2023 = CALCULATE(
    SUM(Ventas[MontoTotal]),
    YEAR(Ventas[Fecha]) = 2023
   )
   ```
5. Clasificación de ventas según monto (columna calculada)
   ```
   CategoriaVenta = IF(Ventas[MontoTotal] > 5000, "Alta", "Baja")
   ```

### Ejercicio práctico
1. Crea una medida de ventas totales.
2. Crea una medida de cantidad total de productos vendidos.
3. Crea una medida de promedio de venta por transacción.
4. Crea un slicer de año y prueba la medida filtrando las ventas de 2023 y 2023.
Crea una columna calculada que clasifique las transacciones en:
   * Alta si el monto total > 5000.
   * Media si está entre 2000 y 5000.
   * Baja si es menor a 2000.

