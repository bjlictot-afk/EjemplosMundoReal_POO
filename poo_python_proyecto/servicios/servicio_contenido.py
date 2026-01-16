# Clase derivada que sobrescribe métodos (polimorfismo)
# Clase base que define atributos y métodos comunes
from modelos.pelicula import Pelicula

class GestorContenido:
    def crear_pelicula(self, titulo, duracion, genero):
        return Pelicula(titulo, duracion, genero)


