# Nombre: Belgica Licto
# Asignatura: Programación
# Tema: Sistema de Tienda - Clase Cliente

class Cliente:
    """
    Clase Cliente:
    Representa a un cliente de una tienda.

    Atributos:
        nombre (str): Nombre del cliente.

    Métodos:
        mostrar_cliente(): Muestra la información del cliente por pantalla.
    """

    def __init__(self, nombre):
        """
        Inicializa un cliente con su nombre.

        Args:
            nombre (str): Nombre del cliente.
        """
        # Guardamos el nombre del cliente dentro del objeto
        self.nombre = nombre

    def mostrar_cliente(self):
        """
        Muestra la información del cliente por pantalla.
        """
        # Imprime el nombre del cliente
        print(f"Cliente: {self.nombre}")

