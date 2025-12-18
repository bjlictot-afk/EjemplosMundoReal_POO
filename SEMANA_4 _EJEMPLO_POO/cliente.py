# Nombre: Belgica Licto
# Asignatura: Programación
# Tema: Sistema de Tienda - Clase Cliente

class Cliente:
    """
    Representa a un cliente de una tienda.
    """

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_cliente(self):
        """
        Muestra la información del cliente.
        """
        print(f"Cliente: {self.nombre}")
