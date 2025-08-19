# 1 Tablas dinámicas, segmentación y filtros avanzados

##### objetivo: Convertir datos crudos en resúmenes interactivos para el análisis rápido

##### Conceptos clave



* Tabla Dinamica -> permite resumir datos (sumas, promedios, conteos) sin modificar el dataset original.
* Segmentación -> botones interactivos para filtrar rápidamente.
* Filtros avanzados -> permiten aplicar condiciones múltiples y complejas.



##### Ejemplo practico:

Supongamos que tienes este dataset de ventas:



| Fecha      | Región | Producto   | Cantidad | Precio Unitario |

| ---------- | ------ | ---------- | -------- | --------------- |

| 01/01/2024 | Norte  | Laptop     | 5        | 1000            |

| 03/01/2024 | Sur    | Tablet     | 8        | 500             |

| 05/01/2024 | Norte  | Tablet     | 3        | 500             |

| 06/01/2024 | Oeste  | Laptop     | 2        | 1000            |

| 08/01/2024 | Este   | Smartphone | 10       | 300             |



###### Tarea inicial:

1. Abre excel y pega esos datos.
2. Selecciónalos y ve a insertar -> Tabla dinámica.
3. En "filas pon región, en "Columnas" pon producto, y en "Valores" pon cantidad.
4. Agrega una segmentación por "Fecha" para filtrar por periodos.


##### 1. Tablas dinámicas

**¿Que son?**

Son una herramienta de excel para resumir, analizar y reorganizar datos sin alterar la tabla original.

Ventajas:

* Haces resúmenes por categorías (por ejemplo, ventas por región).
* Puedes filtrar, agrupar y calcular automáticamente.
* Puedes interactuar con los datos sin fórmulas complejas.



###### Pasos para crear una tabla dinámica

1. Prepara tu tabla de datos

   * Asegúrate de que cada columna tenga un nombre único.
   * No dejes filas o columnas en blanco.
2. Selecciona tu rango de datos y ve a:
   *  **Insertar** -> **Tabla dinámica**
   *  elige "Nueva hoja de cálculo".	
3. Organizar campos
   * Filas: Categoría que tienes que ver en la izquierda.
   * Columnas: Categorías que quieres ver arriba.
   * Valores: el dato numérico que vas a resumir (suma, promedio, conteo, etc.).
   * Filtros: criterios para mostrar u ocultar datos.

##### Ejemplo práctico
con el dataset dado anteriormente:
| Fecha      | Región | Producto   | Cantidad | Precio Unitario |
| ---------- | ------ | ---------- | -------- | --------------- |
| 01/01/2024 | Norte  | Laptop     | 5        | 1000            |
| 03/01/2024 | Sur    | Tablet     | 8        | 500             |
| 05/01/2024 | Norte  | Tablet     | 3        | 500             |
| 06/01/2024 | Oeste  | Laptop     | 2        | 1000            |
| 08/01/2024 | Este   | Smartphone | 10       | 300             |

- **queremos saber cuántas unidades vendimos de cada producto por región.**
- **Configuración:**
    * Filas: Región.
    * Columnas: Producto.
    * Valores: Cantidad (función: Suma).

##### 2. Segmentación (Slicers)
Sirve para agregar filtros visuales interactivos (botones).

**Cómo agregarla:**
* Haz clic en la tabla dinamica.
* Ve a insertar -> Segmentación de datos.
* Seleccionar el campo a segmentar (ejemplo: Fecha, Región o Producto).
* Aparecerán botones para filtrar rápidamente.

##### 3. Filtros avanzados
Cuando no quieres una tabla diámica, sino filtrar en tu tabla original con condiciones mas complejas:
    1. Copia de los encabezados de tu tabla en otra zona.
    2. Debajo de ellos escribe las condiciones.
    3. Ve a Datos -> Filtro avanzado.
    4. Elige si quieres filtrar en el lugar o copiar los datos filtrados.

##### Ejercicio para hacer
1. Abre Excel y pega los datos.
2. Crea la tabla dinámica como en el ejemplo.
3. Agrega una Segmentación por Producto.
4. Aplica un filtro para mostrar solo las ventas de Enero.

# 2. Fórmulas clave de Excel para análisis de datos
Aqui aprenderemos las fórmulas más importantes para búsquedas y referencias dinámicas.

##### BUSCARX (XLOOKUP)
* Es la evolución de BUSCARV y BUSCARH.
* Pemirte buscar valores en una columna y devolver resultados de otra, inncluso hacia la izquierda.

#### **Sintaxis**
```
=BUSCARX(valor_buscado; matriz_buscada; matriz_resultado; [si_no_encontrado]; [modo_coinciencia]; [modo_búsqueda])
```

#### **Ejemplo**
Si tienes una tabla de productos:
| Producto | Precio |
| -------- | ------ |
| Laptop   | 1000   |
| Tablet   | 500    |
| Celular  | 300    |

y quieres saber el precio de la Tablet:

```
=BUSCARX("Tablet",A2:A4,B2:B4)
```
- Resultado: 500.

##### 2. ÍNDICE + COINCIDIR
muy útil cuando no puedes usar BUSCARX (o en versiones antiguas de Excel).
* ÍNDICE: devuelve el valor de una celda según su fila y columna.
* COINCIDIR: devuelve la posición de un valor en un rango.

#### **Sintaxis de INDICE**
```
=INDICE(matriz; num_fila; [num_columna])
```
- matriz: El rango de celdas donde se buscará el valor.
- num_fila: la fila donde se encuentra el valor deseado.
- num_columna: (Opcional) La columna donde se encuentra el valor deseado. Si se omite, se asume la primera columna de la matriz.

#### **Sintaxis de COINCIDIR**
```
=COINCIDIR(valor_buscado; matriz_buscada; [tipo_de_coincidencia])
```
- valor_buscado: El valor que se quiere buscar.
- matriz_buscada: El rango de celdas donde se buscará el valor.
- tipo_de_coincidencia: (Opcional) Especifica el tipo de coincidencia:
   * 0: Coincidencia exacta (por defecto).
   * 1: Coincidencia aproximada menor que.
   * -1: Coincidencia aproximada mayor que.

#### **Sintaxis combinada**
```
=INDICE(matriz; COINCIDIR(valor_buscado; matriz_buscada; [tipo_de_coincidencia]))
```
  

Ejemplo:
| Producto | Precio |
| -------- | ------ |
| Laptop   | 1000   |
| Tablet   | 500    |
| Celular  | 300    |

Queremos el precio de "Celular".
```
=ÍNDICE(B2:B4; COINCIDIR("Celular"; A2:A4; 0))
```
- Resultado: 300.

##### 3. DESREF
Crea referencias dinámicas desplazándose desde una celda inicial.

#### **Sintaxis**:
```
=DESREF(celda_inicial; filas; columnas; [alto]; [ancho])
```

* celda_inicial → el punto de partida.
* filas → cuántas filas bajar (positivo) o subir (negativo).
* columnas → cuántas columnas moverte a la derecha (positivo) o izquierda (negativo).
* alto y ancho (opcionales) → el tamaño del rango.

#### **Ejemplo**
si A1 = 10, A2 = 20, A3 = 30
```
=DESREF(A1;2;0)
```
- Resultado: 30 (porque se mueve 2 filas hacia abajo desde A1).
Útil para crear rangos dinámicos en reportes.

##### 4. Otras funciones útiles
* SI: lógica condicional.
```
=SI(B2>1000; "Alto"; "Bajo")
```
   * SI.CONJUNTO: varias condiciones sin anidarlas.
   * CONTAR.SI / CONTAR.SI.CONJUNTO: contar celdas que cumplen criterios.

##### Ejercicio práctico con tu dataset de transacciones
1. Usar BUSCARX para obtener el Valor Transaccion de un producto especifico (ejemplo: "Préstamo").
2. Usa INDICE + COINCIDIR para obtener la Cantidad de una transacción en la región "Norte".
3. Usa DESREF para crear un rango dinámico que sume siempre las últimas 5 transacciones en la columna Valor Transacción.

# 3. Funciones estadísticas y financieras
Estas funciones son muy útiles cuando analizas datos de transacciones, consumos o tendencias financieras.

### * A. Funciones estadísticas más usadas
##### 1. PROMEDIO
```
=PROMEDIO(rango_celdas)
```
- Saca el valor promedio de los valores.

##### 2. MEDIANA
```
=MEDIANA(rango_celdas)
```
- Valor central (menos sensible a valores extremos).

##### 3. MAX y MIN
```
=MAX(rango_celdas) -> Mayor valor de transacción
=MIN(rango_celdas) -> Menor valor de transacción
```

##### 4. DESVEST.P o DESVEST.M
```
=DESVEST.P(rango_celdas)
```
- Mide cuanto varían los valores respecto al promedio.

##### 5. CONTAR.SI y CONTAR.SI.CONJUNTO
```
=CONTAR.SI(rango_celdas, valor_verdadero)
=CONTAR.SI.CONJUNTO(rango_1_celdas, valor_verdadero, ..., rango_n_celdas, valor_verdadero)
```
- Cuenta registros que cumplen condiciones.

### * B. Funciones financieras clave
Excel tiene funciones nativas para calculos financieros.
##### 1. VF (Valor Futuro)
```
=VF(tasa; nper; pago; [val]; [tipo])
```
* tasa: tasa de interés por periodo.
* nper: número de periodos.
* pago: pago periódico (con signo negativo si es egreso).
* va: valor actual (opcional).
* tipo: 0 = fin de periodo, 1 = inicio.

###### Ejemplo:
Quieres calcular cuánto tendrás ahorrado en 12 meses depositando $200 mensuales con 1% de interés mensual:
```
=VF(0.01; 12; -200; 0; 0)
```
- Resultado ≈ 2.543

##### 2. VNA (Valor Neto Actual)
```
=VNA(tasa; flujo1; flujo2; ...)
```
- Evalúa si una inversión es rentable con base en los flujos de caja futuros.

##### 3. TASA
```
=TASA(nper; pago; va; [vf]; [tipo]; [estimado])
```
- Encuentra la tasa de interés implícita en una inversión o préstamo.

##### Ejercicio práctico con tu dataset
1. Usa PROMEDIO para calcular el promedio de Valor Transacción.
2. Usa MAX y MIN para encontrar la transacción más grande y más pequeña.
3. Usa CONTAR.SI.CONJUNTO para contar cuántas transacciones en la Región Norte superan los 3000.
4. Crea un ejemplo simple de VF: simula que ahorras $500 cada mes durante 24 meses con una tasa de 2% mensual.

# 4. Power Query en Excel
#### ¿Qué es Power Query?
Es una herramienta de ETL (Extract, Transform, Load) que permite:
* Importar datos desde múltiples fuentes (CSV, Excel, SQL, Web, etc.).
* Limpiar y transformar datos sin necesidad de fórmulas.
* Automatizar procesos de limpieza -> si llega un nuevo dataset, solo das Actualizar y se limpia solo.

#### Cómo abrir Power Query
1. En excel ve a Datos -> Obtener y transfomar datos -> Obtener datos.
2. Elije la fuente (Ej: Desde archivo CSV, Excel, o incluso SQL Server).
3. Se abre el editor de Powwer Query.

#### * Operaciones Basicas en Power Query
1. Eliminar columnas o filas innecesarias.
   * Clic derecho -> Quitar columnas.
   * Filtrar datos nulos o vacíos.
2. Cambiar tipo de datos
   * Ejemplo: convetir texto en fecha o número.
3. Dividir columnas
   * Útil si tienes datos combinados (Ejemplo: "Juan-Pérez" en una sola celda -> separarlo en Nombre y Apellido).
4. Eliminar duplicados
   * Botón Quitar duplicados.
5. Columnas calculadas
   * Agregar columna personalizada, por ejemplo:
   ```
   [Cantidad] * [Precio Unitario]
   ```
   para calcular el valor de la transacción.
6. Combinar y anexar tablas
   * Combinar = JOIN entre dos tablas (ej: transacciones + clientes).
   * Anexar = UNION (ej: unir dataset de enero con febrero).

#### Ejemplo practico con tu dataset
1. Importa el archivo en Excel usando Datos -> Obtener datos -> Desde archivo -> Desde Excel.
2. En Power Query:
   * Elimina duplicados.
   * Convierte la columna Fecha al tipo Fecha.
   * Crea una columna calculada llamada Ingreso Total = [cantidad] * [Valor Transacción].
3. Cierra y carga el resultado a Excel para hacer tablas dinámicas limpias.

# Mini-Reto: Análisis de transacciones financieras
### Paso 1 - Cargar y limpiar datos con Power query
1. Abre Excel -> Datos -> Obtener datos -> Desde Archivo -> Desde Excel.
2. Importa dataset_transacciones.xlsx.
3. En el Editor de Power Query:
   * Cambia la columna Fecha al tipo Fecha.
   * Elimina duplicados si existen.
   * Agrega una columna calculada llamado Ingreso total:
      ```
      = [cantidad] * [Valor Transacción]
      ```
   * Filtra solo las transacciones con Valor Transacción > 500
4. Cierra y carga los datos en una nueva hoja.
### Paso 2 - Tablas dinámicas
1. Inserta una tabla dinamica con los datos limpios.
2. haz estos analisis:
   * Total de transacciones por Región y Producto.
   * Promedio del Valor por Región.
   * Evolución de las transacciones por mes (Agrupa las fechas por mes)
 - Agrega segmentación por Producto para filtrar fácilmente.
### Paso 3 - Fórmulas clave
en una celda aparte, calcula con fórmulas:
   1. Promedio de Valor Transacción.
   2. Transacción más grande y mas pequeña.
   3. Cantidad de transacciones en Norte > 3000.
   4. Indice + Coincidir -> devuelve la Cantidad de la primera transacción de la Región "Sur".
### Paso 4 - Función financiera extra
Simula que ahorras $500 mensuales durante 12 meses a una tasa de interés mensual del 2%.
- Esto te dará el capital acumulado al final del año.

✅ Objetivo Final: tener en tu Excel:
* Una hoja con datos limpios de Power Query.
* Una Tabla dinámica con reportes.
* Algunas fórmulas clave aplicadas al dataset.
* Un pequeño calculo financiero.