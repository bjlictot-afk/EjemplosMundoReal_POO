# Nombre: Belgica Licto
# Asignatura: Programación
# Tema: Sistema de Tienda - Clase Producto

class Producto:
    """
    Representa un producto que se vende en una tienda.
    """

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_producto(self):
        """
        Muestra la información del producto.
        """
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")
