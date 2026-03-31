class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "[Completada]" if self.completada else "[Pendiente]"
        return f"{estado} {self.descripcion}"