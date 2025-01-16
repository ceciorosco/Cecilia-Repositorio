
-- Consultas SELECT

/*
*/

-- ¿Que bootcamp tiene más estudiantes?
USE bootcamps;
SELECT 
b.bootcamp as nombre_bootcamp, 
count(e.estudiante_id) as numero_estudiantes
FROM 
bootcamps b
INNER JOIN 
estudiantes e 
ON b.bootcamp_id = e.bootcamp_id
GROUP BY b.bootcamp 
ORDER BY COUNT(e.estudiante_id) DESC
LIMIT 1; -- para que saque solo el primero 

-- ¿Cuantos bootcamps no tienen estudiantes?
USE bootcamps;
SELECT 
b.bootcamp as nombre_bootcamp, 
count(e.estudiante_id) as numero_estudiantes
FROM 
bootcamps b
INNER JOIN 
estudiantes e 
ON b.bootcamp_id = e.bootcamp_id
GROUP BY b.bootcamp 
HAVING count(e.estudiante_id) = 0;

-- ¿Que estudiantes tienen más asistencias y cuales tiene menos?
--para el max
select a.estudiante_id, sum(a.asistencia)
from asistencias a
group by a.estudiante_id
order by sum(a.asistencia) desc;
--para el min
select a.estudiante_id, sum(a.asistencia)
from asistencias a
group by a.estudiante_id
order by sum(a.asistencia); --cambia si es ascendente o descendente

-- ¿Que modulo tiene mas puntuación de media y cual tiene menos puntuación de media?
Use bootcamps;
SELECT 
m.modulos, round(avg(puntuacion), 2) AS media
from
modulos m
join
modulo_bootcamp mb on m.modulo_id = mb.modulo_id
group by m.modulo_id
order by media desc -- el que menos es quitando el desc como en el ejemplo anterior
 ------------------------------- por bootcamp
use bootcamps;
select 
b.bootcamp,
m.modulos,
mb.puntuacion
FROM
modulos m
inner JOIN 
modulo_bootcamp mb on m.modulo_id = mb.modulo_id
INNER JOIN
bootcamps b on mb.bootcamp_id = b.bootcamp_id 
where
m.modulos = 'Machine Learning' and mb.puntuacion = 10;
-- ¿Qué bootcamp tiene mas asistencias y cual tiene menos asistencias? Los bootcamps sin estudiantes no cuentan.
select bootcamps.bootcamp, sum(asistencias.asistencia)
from bootcamps
inner join estudiantes on estudiantes.bootcamp_id = bootcamps.bootcamp_id
inner join asistencias on asistencias.estudiante_id = estudiantes.estudiante_id
group by bootcamps.bootcamp
order by sum(asistencias.asistencia) desc;

-- ¿Qué día tiene el mayor número de asistencias y cual tiene el menor número de asistencias?
use bootcamps;
select a.fecha, sum(a.asistencia)
from asistencias a
group by a.fecha
order by sum(a.asistencia) desc;

-- ¿Cuales bootcamps le dan 10 al modulo de **Machine Learning**?

use bootcamps;
select 
b.bootcamp,
m.modulos,
mb.puntuacion
FROM
modulos m
inner JOIN 
modulo_bootcamp mb on m.modulo_id = mb.modulo_id
INNER JOIN
bootcamps b on mb.bootcamp_id = b.bootcamp_id 
where
m.modulos = 'Machine Learning' and mb.puntuacion = 10;


-- Muestra los 10 estudiantes que tenga más asistencias (_subqueries_).
USE 
    bootcamps;
SELECT 
    e.estudiante_id, 
    sum(a.asistencia) 
FROM 
    estudiantes e
JOIN 
    asistencias a 
ON 
    e.estudiante_id = a.estudiante_id
GROUP BY 
    e.estudiante_id
ORDER BY 
    sum(a.asistencia) DESC
LIMIT 10;

EXPLAIN ANALYZE sirve para ver las estadisticas
