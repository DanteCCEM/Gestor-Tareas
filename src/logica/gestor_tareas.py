def __init__(self):
self.tareas = []
def agregar_tarea(self, titulo, descripcion):
if not titulo:
raise ValueError("El título no puede estar vacío")
tarea = Tarea(titulo, descripcion)
self.tareas.append(tarea)