
## ENTORNO

### MYSQL

Usar el MySQL Installer: https://dev.mysql.com/downloads/installer/

Esto permite instalar:

* MySQL Community Server: sistema gestor de bases de datos MySQL
* MySQL Workbench: Herramienta GUI visual para entrar a MySQL


Esto permite instalar MySQL 8.4.0

Instalación: 

https://certidevs.com/tutorial-sql-mysql-instalacion

* Seleccionar opción de instalación: Full
* Type and networking lo dejamos tal cual en el puerto 3306
* Authentication method lo dejamos tal cual está
* Account and Roles: le escribimos una contraseña para el usuario root, por ejemplo: admin. No es necesario crear ningún otro usuario.
* en el resto de opciones le damos Execute y hacia delante

Una vez instalado buscamos en nuestro ordenador la aplicación: MySQL Workbench.

## MYSQL WORKBENCH

Programa de interfaz de usuario para conectarse a MySQL Server

* Pulsar en Schemas
* Aparecerán las bases de datos: sys, sakila, world

Sakila:

* Desplegar la base de datos sakila
* Desplegar sus tablas
* Desplegar una tabla y ver sus columnas
* Clic derecho en una tabla y hacer una consulta SELECT

Para ver modelo ER: 

* Pulsar en el icono de la casa de arriba a la izquierda 
* en el panel lateral izquierdo hay un icono de 3 tablas unidas por líneas, podemos pulsar 
* Se mostrarán los diagramas existentes, estará sakila y se puede pulsar y abrir


### PYTHON

python -m venv .mod4-sql

* Windows powershell: .mod4-sql\Scripts\activate
* Bash: source .mod4-sql/Scripts/activate

pip install -r requirements.txt

## PARA TRABAJAR SQL DESDE PYTHON

* No es necesario tener MySQL Workbench porque es un programa de interfaz de usuario para ver las bases de datos, no es el gestor de bases de datos en sí.

* Lo que sí necesitamos tener en ejecución es el MySQL Community Server el cuál está instalado como servicio y se ejecuta en el arranque. Se puede ver en el administrador de tareas en Servicios si buscamos MySQL

Alternativas a MySQL Workbench: DBeaver, JetBrains DataGrip, Extensiones de visual studio code.


## TIPOS DE SENTENCIAS SQL

* Data Definition Language (DDL): sentencias para crear bases de datos, crear tablas, modificar tablas, borrar tablas, borrar bases de datos. Ejemplo:
    * CREATE SCHEMA
    * CREATE TABLE
    * ALTER TABLE
    * DROP TABLE
    * SHOW TABLES
    * DROP DATABASE
    * SHOW DATABASES

* Data Manipulation Language (DDL): sentencias para crear y manipular datos dentro de las bases de datos:
    * SELECT
    * INSERT
    * UPDATE
    * DELETE


## CREAR UNA BASE DE DATOS:

* opción 1: desde mysql workbench, pulsar clic derecho en Schemas, y Create Schema, Pulsar Apply Changes
* opción 2: desde python ejecutar el código: CREATE SCHEMA .... 

## CREAR TABLAS

* opción 1: desde mysql workbench abrimos una base de datos, y donde pone Tables, pulsar clic derecho y Create table, esto abre un menú en el que permite agregar columnas y crear la tabla.
* opción 2: desde python ejecutar código: CREATE TABLE ...


## MODELOS DIAGRAMAS (Opcional)

## Reverse Engineer

Seleccionado la opción Database  y luego la opción Reverse Engineer.

Seleccionamos la base de datos que queramos, por ejemplo bootcamps.

Crear diagrama de la base de datos bootcamps.

El modelo luego se puede guardar como un archivo .mwb

## Forward Engineer

A partir de un modelo diagrama podemos pulsar Dabase y la opción Forward Engineer.

Esto nos permite generar el SQL a partir de un diagrama existente.


## ENUNCIADO EJERCICIO 

### 1. CREAR BASE DE DATOS (33%)

* Crear con código SQL una base de datos llamada supermercado.
* Código Python con mysql connector que ejecute el SQL para borrar y generar la base de datos vacía.

Tablas: 7 

tiendas
- id_tienda (PRIMARY KEY)
- nombre_tienda
- direccion
- ciudad

empleados
- id_empleado (PRIMARY KEY)
- nombre_empleado
- puesto (ej.: Cajero, Gerente, Reponedor)
- id_tienda (FOREIGN KEY que hace referencia a tiendas.id_tienda)

categorias
- id_categoria (PRIMARY KEY)
- nombre_categoria

productos
- id_producto (PRIMARY KEY)
- nombre_producto
- precio
- stock
- id_categoria (FOREIGN KEY que hace referencia a categorias.id_categoria)

clientes
- id_cliente (PRIMARY KEY)
- first_name
- last_name
- email
- codigo_postal

ordenes
- id_orden (PRIMARY KEY)
- id_cliente (FOREIGN KEY que hace referencia a clientes.id_cliente)
- id_empleado (FOREIGN KEY que hace referencia a empleados.id_empleado)
- fecha_orden
- metodo_pago (una enum que solo admita tres valores Tarjeta, Efectivo)

detalle_orden
- id_detalle (PRIMARY KEY)
- id_orden (FOREIGN KEY que hace referencia a ordenes.id_orden) NOT NULL
- id_producto (FOREIGN KEY que hace referencia a productos.id_producto) NOT NULL
- cantidad
- precio_unitario: mismo precio que en la tabla producto
- descuento (podría ser NULL si no se aplica)



### 2. Generar datos demo desde Python (33%)

* Generar datos aleatorios en listas con Python similar los realizados en clase.
    * Uso de datetime, timedelta, random para generar datos aleatorios
* Pasar los datos a DataFrames de Pandas
* Pasar los DataFrames de Pandas a MySQL usando la función to_sql de Pandas con SQLAlchemy o usando MySQL Connector con sentencias INSERT.


tiendas

* id_tienda: valores enteros consecutivos (por ejemplo, 1, 2, 3...).
* nombre_tienda: nombres ficticios o genéricos (p. ej. "Tienda Centro", "Super Norte", "Super Sur").
* direccion: direcciones simples (p. ej. “Calle Falsa 123”).
* ciudad: usar nombres de ciudades ficticias o reales (p. ej. “Madrid”, “Barcelona”, “México DF”, etc.).

En total 5 o 10 tiendas.


empleados

* id_empleado: valores enteros consecutivos (1, 2, 3...).
* nombre_empleado: nombres y apellidos ficticios (p. ej. “Laura Gutiérrez”, “Juan Pérez”).
* puesto: limitarse a un conjunto reducido de valores (p. ej. {‘Cajero’, ‘Gerente’, ‘Reponedor’, ‘Vendedor’}).
* id_tienda: debe hacer referencia a una tienda existente (por ejemplo, un número entre 1 y 3 si solo tienes 3 tiendas).

En total 20 empleados por tienda.

categorias

* id_categoria: valores enteros consecutivos (1, 2, 3...).
* nombre_categoria: selección de categorías (p. ej. “Lácteos”, “Carnes”, “Frutas”, “Verduras”, “Bebidas”, “Snacks”).

En total 10 categorías.


productos

* id_producto: valores enteros consecutivos (1, 2, 3...).
nombre_producto: nombres como “Leche Entera”, “Manzana Roja”, “Refresco de Cola”, etc.
* precio: valores DECIMAL entre 0.50 y 50.00, por ejemplo.
* stock: valores INT entre 0 y 500 (o el rango que quieras).
* id_categoria: debe hacer referencia a las categorías que hayas definido (1, 2, 3, etc.).

En total 4 productos de cada categoría.


clientes

* id_cliente: valores enteros consecutivos (1, 2, 3...).
* nombre_cliente: nombres y apellidos ficticios (p. ej. “Carlos López”, “María Gil”).
* email: podrías generar correos ficticios (p. ej. “carlos.lopez@test.com”).
* telefono: número de 9 o 10 dígitos (dependiendo del país).
* direccion: calles y números ficticios (p. ej. “Av. Siempre Viva 742”).

En total: 2000.

ordenes

* id_orden: valores enteros consecutivos (1, 2, 3...).
* id_cliente: haz referencia a los IDs existentes de la tabla clientes.
* id_empleado: haz referencia a los IDs existentes de la tabla empleados.
* fecha_orden: genera fechas aleatorias o secuenciales (p. ej. entre ‘2024-01-01’ y ‘2025-01-01’).
* metodo_pago: escoge entre {‘Tarjeta’, ‘Efectivo’}.

En total: 10000.

detalle_orden

* id_detalle: valores enteros consecutivos (1, 2, 3...).
* id_orden: referencia al ID de alguna orden válida.
* id_producto: referencia al ID de algún producto válido.
* cantidad: valores entre 1 y 20, por ejemplo.
* precio_unitario: usar el mismo precio que está en la tabla productos o uno ligeramente distinto si quieres simular ofertas.
* descuento: valores DECIMAL bajos (p. ej. 0.00, 1.00, 2.50) o NULL.

En total: 30000.


### 3. Consultas SQL (34%)

1. Listado de órdenes con detalles de cliente y empleado
* Muestra el ID de la orden, la fecha, el nombre del cliente, el nombre del empleado que atendió la compra y el método de pago.
* Utiliza un JOIN entre las tablas ordenes, clientes y empleados.


2. Productos con stock bajo
* Filtra aquellos productos cuyo stock sea menor a 10.
* Muestra nombre del producto, categoría y stock.


3. Ventas totales por categoría
* Muestra el nombre de la categoría y la suma total de las ventas (ej.: multiplicando cantidad * precio_unitario) para cada categoría.
* Realiza el JOIN con detalle_orden, productos y categorias.
* Utiliza agrupación (GROUP BY).


4. Clientes con mayores gastos acumulados
* Muestra el nombre del cliente y el monto total que ha gastado (suma de todas sus órdenes).
* Asegúrate de tener en cuenta posibles descuentos (descuento) si se ha definido. Por ejemplo, la fórmula podría ser (cantidad * precio_unitario) - descuento.
* Ordena el resultado de mayor a menor gasto acumulado.


5. Empleados y número de órdenes gestionadas
* Muestra el nombre del empleado, el puesto y la cantidad de órdenes que ha gestionado.
* Utiliza GROUP BY y COUNT.


6. Ordenes filtradas por fecha y tienda
* Muestra todas las órdenes que se realizaron en un rango de fechas determinado (ej.: del 1 de enero de 2025 al 31 de enero de 2025) y en una tienda específica.
* Incluye datos de la tienda y del cliente.


7. Ranking de productos más vendidos en cada tienda
* Para cada tienda, muestra los 3 productos más vendidos (en términos de cantidad total).
* Tendrás que unir tiendas, empleados, ordenes y detalle_orden, además de productos.
* Usa GROUP BY y ordena por la cantidad sumada (y opcionalmente, un LIMIT 3).


Opcional: añadir alguna consulta con subconsultas o algo que no se abarque en las anteriores consulta.


### FORMATO ENTREGA:

m4_nombre_apellido.ipynb que tenga todo el código Python y todo el código SQL en el mismo archivo .ipynb para poder descargarlo mejor.