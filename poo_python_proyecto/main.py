from servicios.servicio_contenido import GestorContenido

gestor = GestorContenido()

pelicula1 = gestor.crear_pelicula("Interestelar", 169, "Ciencia ficción")
pelicula2 = gestor.crear_pelicula("Coco", 105, "Animación")

print(pelicula1.descripcion())
print("Duración:", pelicula1.get_duracion(), "min")

print(pelicula2.descripcion())
print("Duración:", pelicula2.get_duracion(), "min")

