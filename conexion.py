import mysql.connector


def insertar_datos(tabla, columnas, valores):
    # Conectar a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="escuela"
    )
    # Crear un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()

    # Construir la consulta SQL
    placeholders = ', '.join(['%s'] * len(valores))
    consulta = f"INSERT INTO {tabla} ({', '.join(columnas)}) VALUES ({placeholders})"

    # Ejecutar la consulta SQL para insertar datos en la tabla
    cursor.execute(consulta, valores)

    # Hacer commit para guardar los cambios en la base de datos
    conexion.commit()

    # Cerrar la conexión y el cursor
    cursor.close()
    conexion.close()


def reset():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="escuela"
    )
    cursor = conexion.cursor()

    consulta = "DELETE FROM alumnos;"
    cursor.execute(consulta)

    consulta = "ALTER TABLE alumnos AUTO_INCREMENT = 1;"
    cursor.execute(consulta)

    consulta = "DELETE FROM cursos;"
    cursor.execute(consulta)

    consulta = "ALTER TABLE cursos AUTO_INCREMENT = 1;"
    cursor.execute(consulta)

    conexion.commit()

    cursor.close()
    conexion.close()


def prome(lista):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="escuela"
    )
    cursor = conexion.cursor()

    query = """
    SELECT cursos.nombre_curso, SUM(alumnos.nota)/COUNT(alumnos.id_curso) AS promedio
    FROM cursos
    INNER JOIN alumnos ON cursos.id_curso = alumnos.id_curso
    GROUP BY cursos.nombre_curso
    ORDER BY cursos.nombre_curso asc;
    """

    cursor.execute(query)

    for fila in cursor.fetchall():
        lista.append(fila)

    conexion.close()


def maxProm(lista):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="escuela"
    )

    cursor = conexion.cursor()

    query = """
    SELECT cursos.nombre_curso, SUM(alumnos.nota)/COUNT(alumnos.id_curso) AS promedio
    FROM cursos
    INNER JOIN alumnos ON cursos.id_curso = alumnos.id_curso
    GROUP BY cursos.nombre_curso
    ORDER BY promedio DESC
	LIMIT 1;
    """

    cursor.execute(query)

    for fila in cursor.fetchall():
        lista.append(fila)

    conexion.close()


def genios(lista):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="escuela"
    )

    cursor = conexion.cursor()

    query = "SELECT nombre_alumno, apellido_alumno, max(nota), id_curso FROM alumnos  GROUP BY id_curso;"

    cursor.execute(query)

    for fila in cursor.fetchall():
        lista.append(fila)

    conexion.close()
