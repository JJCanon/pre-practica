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
* Solo mostrar transacciones de 2024 en adelante.

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
    * Filtra para que solo aparezcan registros de 2024.
3. Aplica los cambios y regresa a Power BI.