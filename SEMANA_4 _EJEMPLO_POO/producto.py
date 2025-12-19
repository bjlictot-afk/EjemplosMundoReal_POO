# Nombre: Belgica Licto
# Asignatura: Programación
# Tema: Sistema de Tienda - Clase Producto

class Producto:
    """
    Clase Producto:
    Representa un producto disponible en la tienda.

    Atributos:
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        stock (int): Cantidad disponible en inventario.

    Métodos:
        mostrar_producto(): Muestra la información del producto por pantalla.
    """

    def __init__(self, nombre, precio, stock):
        """
        Inicializa un producto con nombre, precio y stock.

        Args:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            stock (int): Cantidad disponible.
        """
        # Guardamos el nombre del producto
        self.nombre = nombre
        # Guardamos el precio del producto
        self.precio = precio
        # Guardamos la cantidad disponible
        self.stock = stock

    def mostrar_producto(self):
        """
        Muestra la información del producto por pantalla.
        """
        print(f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}")

