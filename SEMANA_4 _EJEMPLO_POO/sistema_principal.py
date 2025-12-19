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

Se muestran ejemplos de:
- Creación de un cliente.
- Creación de productos.
- Mostrar la información de cliente y productos.
"""

def main():
    """
    Función principal que ejecuta el sistema de tienda.
    """
    # --- CREAR CLIENTE ---
    cliente1 = Cliente("Belgica")  # Creamos un cliente con nombre "Belgica"

    # --- CREAR PRODUCTOS ---
    producto1 = Producto("Arroz", 1.50, 20)  # Producto arroz: $1.50, 20 unidades
    producto2 = Producto("Leche", 0.80, 30)  # Producto leche: $0.80, 30 unidades

    # --- MOSTRAR INFORMACIÓN ---
    cliente1.mostrar_cliente()      # Mostrar nombre del cliente
    producto1.mostrar_producto()    # Mostrar información del primer producto
    producto2.mostrar_producto()    # Mostrar información del segundo producto

# Punto de entrada del programa
if __name__ == "__main__":
    main()

