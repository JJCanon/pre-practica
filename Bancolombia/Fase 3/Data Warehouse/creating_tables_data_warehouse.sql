-- Crear el schema dw
CREATE SCHEMA IF NOT EXISTS dw;

-- Crear tabla DimCliente
CREATE TABLE IF NOT EXISTS dw.DimCliente (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100)
);

-- Crear tabla DimProducto
CREATE TABLE IF NOT EXISTS dw.DimProducto (
    id_producto SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    precio NUMERIC(10,2)
);

-- Crear tabla DimTiempo
CREATE TABLE IF NOT EXISTS dw.DimTiempo (
    id_tiempo INT PRIMARY KEY,
    fecha DATE NOT NULL,
    mes INT,
    anio INT
);

-- Crear tabla FactVentas
CREATE TABLE IF NOT EXISTS dw.FactVentas (
    id_venta SERIAL PRIMARY KEY,
    id_cliente INT REFERENCES dw.DimCliente(id_cliente),
    id_producto INT REFERENCES dw.DimProducto(id_producto),
    id_tiempo INT REFERENCES dw.DimTiempo(id_tiempo),
    cantidad INT,
    monto NUMERIC(12,2)
);

-- Crear índices para mejor performance
CREATE INDEX idx_factventas_cliente ON dw.FactVentas(id_cliente);
CREATE INDEX idx_factventas_producto ON dw.FactVentas(id_producto);
CREATE INDEX idx_factventas_tiempo ON dw.FactVentas(id_tiempo);