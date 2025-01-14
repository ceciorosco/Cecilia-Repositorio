DROP DATABASE IF EXISTS bootcamps;

CREATE DATABASE IF NOT EXISTS bootcamps;

USE bootcamps;

CREATE TABLE IF NOT EXISTS modulos (
    modulo_id INT AUTO_INCREMENT PRIMARY KEY,
    modulos VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS bootcamps (
    bootcamp_id INT AUTO_INCREMENT PRIMARY KEY,
    bootcamp VARCHAR(255), 
    inicio_bootcamp DATE,
    final_bootcamp DATE
);

CREATE TABLE IF NOT EXISTS estudiantes(
    estudiante_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50), 
    apellido VARCHAR(50),
    email VARCHAR(200),
    inscripcion DATE,
    beca BOOLEAN,
    bootcamp_id INT,
    -- Opcion 1:
    FOREIGN KEY (bootcamp_id) REFERENCES bootcamps(bootcamp_id) -- ON DELETE CASCADE

    -- Opcion 2:
    -- CONSTRAINT fk_estudiantes_bootcamps FOREIGN KEY (bootcamp_id) REFERENCES bootcamps(bootcamps_id) 

    -- Opcion 3:
    -- FOREIGN KEY (bootcamp_id)
    -- REFERENCES boorcamps(bootcamp_id)
    -- ON DELETE CASCADE
    -- ON UPDATE CASCADE 
);

CREATE TABLE IF NOT EXISTS modulo_bootcamp(
    bootcamp_id INT NOT NULL,
    modulo_id INT NOT NULL,
    puntuacion TINYINT UNSIGNED, 
    PRIMARY KEY (bootcamp_id, modulo_id),
    FOREIGN KEY (bootcamp_id) REFERENCES bootcamps(bootcamp_id) ON DELETE CASCADE,
    FOREIGN KEY (modulo_id) REFERENCES modulos(modulo_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS asistencias(
    asistencia_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT NOT NULL,
    asistencia BOOLEAN,
    fecha DATE,
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(estudiante_id) ON DELETE CASCADE
);