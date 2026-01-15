from modelos.pelicula import Pelicula

class GestorContenido:
    def crear_pelicula(self, titulo, duracion, genero):
        return Pelicula(titulo, duracion, genero)


