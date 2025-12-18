# Nombre: Belgica Licto
# Asignatura: Programación
# Tema: Sistema de Tienda - Archivo Principal

from cliente import Cliente
from producto import Producto

"""
EJEMPLO DEL MUNDO REAL: SISTEMA DE TIENDA

Este programa integra las clases Cliente y Producto
para modelar una tienda del mundo real aplicando
Programación Orientada a Objetos (POO).
"""

def main():
    # Crear cliente
    cliente1 = Cliente("Belgica")

    # Crear productos
    producto1 = Producto("Arroz", 1.50)
    producto2 = Producto("Azúcar", 1.20)

    # Mostrar información
    cliente1.mostrar_cliente()
    producto1.mostrar_producto()
    producto2.mostrar_producto()

# Punto de entrada del programa
if __name__ == "__main__":
    main()
