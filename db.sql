
-- crear la base de datos
CREATE DATABASE escuela;

--usar la base de datos
USE escuela;

--creo la tabla cursos con la clave primaria id_curso
CREATE TABLE cursos(
	id_curso INT AUTO_INCREMENT UNIQUE,
	nombre_curso VARCHAR(255) NOT NULL,
	PRIMARY KEY(id_curso)
);

--creo la tabla cursos con la clave primaria id_alumno y una foreign key id_curso con referencia a la tabla cursos
CREATE TABLE alumnos(
	id_alumno INT AUTO_INCREMENT UNIQUE,
	id_curso INT,
	nombre_alumno VARCHAR(255) NOT NULL,
	PRIMARY KEY(id_alumno),
	FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);

--agrego una columna con el apellido del alumno
ALTER TABLE alumnos
	ADD apellido_alumno VARCHAR(255) NOT NULL

ALTER TABLE alumnos
	ADD nota int NOT NULL