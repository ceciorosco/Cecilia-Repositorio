-- Tabla para la entidad `Marca`
CREATE TABLE marca 
(
  marca_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL
);

-- Tabla para la entidad `Categoría`
CREATE TABLE categoria 
(
  categoria_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL
);

-- Tabla para la entidad `Modelo`
CREATE TABLE modelo 
(
  modelo_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  marca_id INT NOT NULL,
  FOREIGN KEY (marca_id) REFERENCES marca(marca_id)
);

-- Tabla para la entidad `Cliente`
CREATE TABLE cliente 
(
  cliente_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  direccion VARCHAR(255) NOT NULL,
  correo_electronico VARCHAR(255) NOT NULL
);

-- Tabla para la entidad `Producto`
CREATE TABLE producto (
  producto_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  descripcion TEXT,
  precio DECIMAL(10, 2) NOT NULL,
  stock INT NOT NULL,
  marca_id INT,
  categoria_id INT,
  modelo_id INT,
  FOREIGN KEY (marca_id) REFERENCES marca(marca_id),
  FOREIGN KEY (categoria_id) REFERENCES categoria(categoria_id),
  FOREIGN KEY (modelo_id) REFERENCES modelo(modelo_id)
);

-- Tabla para la entidad `Característica`
CREATE TABLE caracteristica 
(
  caracteristica_id INT AUTO_INCREMENT PRIMARY KEY,
  tipo VARCHAR(255) NOT NULL,
  valor VARCHAR(255) NOT NULL,
  producto_id INT(11) NOT NULL,
  FOREIGN KEY (producto_id) REFERENCES producto(producto_id)
);

-- Tabla para la entidad `Venta`
CREATE TABLE venta 
(
  id INT AUTO_INCREMENT PRIMARY KEY,
  fecha_venta DATE NOT NULL,
  cantidad INT NOT NULL,
  producto_id INT,
  cliente_id INT,
  FOREIGN KEY (producto_id) REFERENCES producto(producto_id),
  FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id)
);

-- Tabla para la entidad `Devolución`
CREATE TABLE devolucion 
(
  devolucion_id INT AUTO_INCREMENT PRIMARY KEY,
  fecha_devolucion DATE NOT NULL,
  cantidad INT NOT NULL,
  producto_id INT,
  cliente_id INT,
  FOREIGN KEY (producto_id) REFERENCES producto(producto_id),
  FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id)
);

-- Tabla para la entidad `Historial de precios`
CREATE TABLE historial_precio 
(
  historial_precio_id INT AUTO_INCREMENT PRIMARY KEY,
  fecha_cambio_precio DATE NOT NULL,
  precio_anterior DECIMAL(10, 2) NOT NULL,
  precio_actual DECIMAL(10, 2) NOT NULL,
  producto_id INT,
  FOREIGN KEY (producto_id) REFERENCES producto(producto_id)
);
