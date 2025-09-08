-- Insertar datos en DimCliente (20 clientes)
INSERT INTO dw.DimCliente (nombre, ciudad) VALUES
('Juan Pérez', 'Bogotá'),
('María García', 'Medellín'),
('Carlos Rodríguez', 'Cali'),
('Ana Martínez', 'Barranquilla'),
('Luis González', 'Cartagena'),
('Sofía López', 'Bucaramanga'),
('Miguel Hernández', 'Pereira'),
('Laura Díaz', 'Santa Marta'),
('Jorge Ramírez', 'Manizales'),
('Elena Fernández', 'Ibagué'),
('Pedro Sánchez', 'Villavicencio'),
('Carmen Torres', 'Cúcuta'),
('Diego Flores', 'Montería'),
('Isabel Reyes', 'Pasto'),
('Andrés Morales', 'Armenia'),
('Rosa Ortega', 'Sincelejo'),
('Fernando Silva', 'Valledupar'),
('Patricia Vargas', 'Tunja'),
('Ricardo Castro', 'Riohacha'),
('Mónica Rojas', 'Quibdó');

-- Insertar datos en DimProducto (15 productos)
INSERT INTO dw.DimProducto (nombre, categoria, precio) VALUES
('Arroz Diana 1kg', 'Granos', 2500),
('Leche Alpina 1L', 'Lácteos', 3200),
('Azúcar Incauca 1kg', 'Endulzantes', 1800),
('Aceite Gourmet 1L', 'Aceites', 8500),
('Café Juan Valdez 500g', 'Bebidas', 12500),
('Pan Bimbo', 'Panadería', 4500),
('Huevos AA x12', 'Proteínas', 7500),
('Queso Costeño 500g', 'Lácteos', 9800),
('Pasta Doria 500g', 'Pastas', 2200),
('Atún Van Camps 170g', 'Enlatados', 4200),
('Jabón Rey', 'Aseo', 2800),
('Shampoo Savital', 'Cuidado Personal', 11200),
('Detergente Fab', 'Limpieza', 6500),
('Cerveza Aguila', 'Bebidas Alcohólicas', 2500),
('Galletas Festival', 'Snacks', 1800);

-- Insertar datos en DimTiempo (30 días de enero y febrero 2024)
INSERT INTO dw.DimTiempo (id_tiempo, fecha, mes, anio) VALUES
(20240101, '2024-01-01', 1, 2024),
(20240102, '2024-01-02', 1, 2024),
(20240103, '2024-01-03', 1, 2024),
(20240104, '2024-01-04', 1, 2024),
(20240105, '2024-01-05', 1, 2024),
(20240106, '2024-01-06', 1, 2024),
(20240107, '2024-01-07', 1, 2024),
(20240108, '2024-01-08', 1, 2024),
(20240109, '2024-01-09', 1, 2024),
(20240110, '2024-01-10', 1, 2024),
(20240111, '2024-01-11', 1, 2024),
(20240112, '2024-01-12', 1, 2024),
(20240113, '2024-01-13', 1, 2024),
(20240114, '2024-01-14', 1, 2024),
(20240115, '2024-01-15', 1, 2024),
(20240201, '2024-02-01', 2, 2024),
(20240202, '2024-02-02', 2, 2024),
(20240203, '2024-02-03', 2, 2024),
(20240204, '2024-02-04', 2, 2024),
(20240205, '2024-02-05', 2, 2024),
(20240206, '2024-02-06', 2, 2024),
(20240207, '2024-02-07', 2, 2024),
(20240208, '2024-02-08', 2, 2024),
(20240209, '2024-02-09', 2, 2024),
(20240210, '2024-02-10', 2, 2024),
(20240211, '2024-02-11', 2, 2024),
(20240212, '2024-02-12', 2, 2024),
(20240213, '2024-02-13', 2, 2024),
(20240214, '2024-02-14', 2, 2024),
(20240215, '2024-02-15', 2, 2024);

-- Insertar datos en FactVentas (50 ventas)
INSERT INTO dw.FactVentas (id_cliente, id_producto, id_tiempo, cantidad, monto) VALUES
-- Enero 2024
(1, 1, 20240101, 2, 5000),   -- Juan compra Arroz
(2, 2, 20240101, 1, 3200),   -- María compra Leche
(3, 3, 20240102, 1, 1800),   -- Carlos compra Azúcar
(4, 4, 20240102, 1, 8500),   -- Ana compra Aceite
(5, 5, 20240103, 1, 12500),  -- Luis compra Café
(6, 6, 20240103, 2, 9000),   -- Sofía compra Pan
(7, 7, 20240104, 1, 7500),   -- Miguel compra Huevos
(8, 8, 20240104, 1, 9800),   -- Laura compra Queso
(9, 9, 20240105, 3, 6600),   -- Jorge compra Pasta
(10, 10, 20240105, 2, 8400), -- Elena compra Atún

-- Más ventas de enero
(11, 11, 20240106, 1, 2800), -- Pedro compra Jabón
(12, 12, 20240106, 1, 11200),-- Carmen compra Shampoo
(13, 13, 20240107, 2, 13000),-- Diego compra Detergente
(14, 14, 20240107, 6, 15000),-- Isabel compra Cerveza
(15, 15, 20240108, 4, 7200), -- Andrés compra Galletas
(1, 2, 20240108, 1, 3200),   -- Juan compra Leche
(2, 3, 20240109, 2, 3600),   -- María compra Azúcar
(3, 4, 20240109, 1, 8500),   -- Carlos compra Aceite
(4, 5, 20240110, 1, 12500),  -- Ana compra Café
(5, 6, 20240110, 1, 4500),   -- Luis compra Pan

-- Febrero 2024
(6, 7, 20240201, 2, 15000),  -- Sofía compra Huevos
(7, 8, 20240201, 1, 9800),   -- Miguel compra Queso
(8, 9, 20240202, 2, 4400),   -- Laura compra Pasta
(9, 10, 20240202, 3, 12600), -- Jorge compra Atún
(10, 11, 20240203, 1, 2800), -- Elena compra Jabón
(11, 12, 20240203, 1, 11200),-- Pedro compra Shampoo
(12, 13, 20240204, 1, 6500), -- Carmen compra Detergente
(13, 14, 20240204, 4, 10000),-- Diego compra Cerveza
(14, 15, 20240205, 2, 3600), -- Isabel compra Galletas
(15, 1, 20240205, 1, 2500),  -- Andrés compra Arroz

-- Más ventas de febrero
(16, 2, 20240206, 2, 6400),  -- Rosa compra Leche
(17, 3, 20240206, 1, 1800),  -- Fernando compra Azúcar
(18, 4, 20240207, 1, 8500),  -- Patricia compra Aceite
(19, 5, 20240207, 2, 25000), -- Ricardo compra Café
(20, 6, 20240208, 1, 4500),  -- Mónica compra Pan
(1, 7, 20240208, 1, 7500),   -- Juan compra Huevos
(2, 8, 20240209, 1, 9800),   -- María compra Queso
(3, 9, 20240209, 2, 4400),   -- Carlos compra Pasta
(4, 10, 20240210, 1, 4200),  -- Ana compra Atún
(5, 11, 20240210, 3, 8400),  -- Luis compra Jabón

-- Últimas ventas
(6, 12, 20240211, 1, 11200), -- Sofía compra Shampoo
(7, 13, 20240211, 2, 13000), -- Miguel compra Detergente
(8, 14, 20240212, 6, 15000), -- Laura compra Cerveza
(9, 15, 20240212, 4, 7200),  -- Jorge compra Galletas
(10, 1, 20240213, 2, 5000),  -- Elena compra Arroz
(11, 2, 20240213, 1, 3200),  -- Pedro compra Leche
(12, 3, 20240214, 2, 3600),  -- Carmen compra Azúcar
(13, 4, 20240214, 1, 8500),  -- Diego compra Aceite
(14, 5, 20240215, 1, 12500), -- Isabel compra Café
(15, 6, 20240215, 1, 4500);  -- Andrés compra Pan