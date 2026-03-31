from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTarea

if __name__ == "__main__":
    # Inyectar el servicio en la UI (Inyección de dependencias básica)
    servicio = TareaServicio()
    app = AppTarea(servicio)
    app.mainloop()