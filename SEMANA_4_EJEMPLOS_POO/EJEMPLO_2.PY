"""
EJEMPLO 2: SISTEMA DE TIENDA Y PRODUCTOS

Este ejercicio modela una tienda del mundo real utilizando
Programación Orientada a Objetos, aplicando clases y objetos.
"""

class Producto:
    """
    Representa un producto de una tienda.
    """
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f"Producto: {self.nombre} - Precio: ${self.precio}")


class Tienda:
    """
    Representa una tienda.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"Tienda: {self.nombre}")
        for producto in self.productos:
            producto.mostrar_info()


# Uso del programa
prod1 = Producto("Arroz", 1.50)
prod2 = Producto("Azúcar", 1.20)

tienda = Tienda("Tienda Don Luis")
tienda.agregar_producto(prod1)
tienda.agregar_producto(prod2)

tienda.mostrar_productos()
