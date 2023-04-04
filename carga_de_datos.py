from conexion import insertar_datos, reset
from random import randint


def crear():
    for i in range(1, 11):
        tabla = "cursos"
        columnas = ["id_curso", "nombre_curso"]
        valores = [None, f"grupo {i}"]
        insertar_datos(tabla, columnas, valores)

    # inicializacion de variables
    apellidos = []
    nombres = []

    # lectura de apellidos.txt
    with open("apellidos.txt", "r", encoding="utf-8") as archivo:
        for i in archivo:
            apellidos.append(i.rstrip())

    # lectura de nombres.txt
    with open("nombres.txt", "r", encoding="utf-8") as archivo:
        for i in archivo:
            nombres.append(i.rstrip())

    # llena la tabla alumnos
    for i in range(1, 11):
        for j in range(1, 31):
            aleatorioApellido = randint(0, 99)
            aleatorioNombre = randint(0, 99)
            aleatorioNota = randint(1, 10)
            tabla = "alumnos"
            columnas = ["id_alumno", "id_curso",
                        "nombre_alumno", "apellido_alumno", "nota"]
            valores = [None, i, nombres[aleatorioNombre],
                       apellidos[aleatorioApellido], aleatorioNota]
            insertar_datos(tabla, columnas, valores)
