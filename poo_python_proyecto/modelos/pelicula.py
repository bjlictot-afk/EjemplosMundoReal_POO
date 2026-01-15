# Clase base Persona
# Aplica encapsulación y define atributos y métodos

from modelos.contenido import Contenido

class Pelicula(Contenido):
    def __init__(self, titulo, duracion, genero):
        super().__init__(titulo, duracion)
        self.genero = genero

    # Polimorfismo (método sobrescrito)
    def descripcion(self):
        return f"Película: {self.titulo} | Género: {self.genero}"

