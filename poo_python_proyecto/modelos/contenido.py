# Clase base
class Contenido:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.__duracion = duracion  # Encapsulación

    def get_duracion(self):
        return self.__duracion

    def descripcion(self):
        return f"Contenido: {self.titulo}"

