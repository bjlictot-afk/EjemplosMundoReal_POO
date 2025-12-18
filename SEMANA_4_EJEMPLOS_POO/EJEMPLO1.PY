# Nombre: Belgica Licto
# Asignatura: Programación orientada a ojetos
# Tema: Ejemplos del Mundo Real usando POO
"""
EJEMPLO 1: SISTEMA DE ESTUDIANTES Y CURSOS

Este ejercicio representa un sistema académico del mundo real.
Se utiliza Programación Orientada a Objetos para modelar estudiantes
y cursos mediante clases, atributos y métodos.
"""

class Estudiante:
    """
    Representa a un estudiante.
    """
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Carrera: {self.carrera}")


class Curso:
    """
    Representa un curso académico.
    """
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        print(f"Curso: {self.nombre_curso}")
        for estudiante in self.estudiantes:
            estudiante.mostrar_datos()


# Uso del programa
est1 = Estudiante("Ana", "Ingeniería")
est2 = Estudiante("Carlos", "Sistemas")

curso = Curso("Programación I")
curso.agregar_estudiante(est1)
curso.agregar_estudiante(est2)

curso.mostrar_estudiantes()
