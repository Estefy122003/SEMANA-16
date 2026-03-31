import tkinter as tk
from tkinter import messagebox

class AppTarea(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio
        self.title("Gestor de Tareas - Semana 16")
        self.geometry("400x450")

        # Componentes UI
        self.entry_tarea = tk.Entry(self, font=("Arial", 12))
        self.entry_tarea.pack(pady=10, padx=10, fill=tk.X)
        
        # Atajo: Añadir con Enter
        self.entry_tarea.bind("<Return>", lambda event: self.añadir_tarea())

        self.btn_añadir = tk.Button(self, text="Añadir Tarea (Enter)", command=self.añadir_tarea)
        self.btn_añadir.pack(pady=5)

        self.lista_visual = tk.Listbox(self, font=("Arial", 11), selectmode=tk.SINGLE)
        self.lista_visual.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Controles inferiores
        self.btn_completar = tk.Button(self, text="Marcar Completada (C)", command=self.completar_tarea)
        self.btn_completar.pack(side=tk.LEFT, padx=20, pady=10)

        self.btn_eliminar = tk.Button(self, text="Eliminar (Delete/D)", command=self.eliminar_tarea)
        self.btn_eliminar.pack(side=tk.RIGHT, padx=20, pady=10)

        # Configuración de Atajos Globales
        self.bind("<KeyPress-c>", lambda event: self.completar_tarea())
        self.bind("<KeyPress-C>", lambda event: self.completar_tarea())
        self.bind("<Delete>", lambda event: self.eliminar_tarea())
        self.bind("<KeyPress-d>", lambda event: self.eliminar_tarea())
        self.bind("<KeyPress-D>", lambda event: self.eliminar_tarea())
        self.bind("<Escape>", lambda event: self.destroy())

    def actualizar_lista(self):
        self.lista_visual.delete(0, tk.END)
        for tarea in self.servicio.obtener_todas():
            item = str(tarea)
            self.lista_visual.insert(tk.END, item)
            # Feedback visual: color gris para completadas
            if tarea.completada:
                self.lista_visual.itemconfig(tk.END, fg="gray")

    def añadir_tarea(self):
        descripcion = self.entry_tarea.get()
        if self.servicio.añadir_tarea(descripcion):
            self.entry_tarea.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Atención", "La tarea no puede estar vacía.")

    def completar_tarea(self):
        try:
            indice = self.lista_visual.curselection()[0]
            self.servicio.marcar_como_completada(indice)
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Selección", "Selecciona una tarea de la lista primero.")

    def eliminar_tarea(self):
        try:
            indice = self.lista_visual.curselection()[0]
            if messagebox.askyesno("Confirmar", "¿Deseas eliminar esta tarea?"):
                self.servicio.eliminar_tarea(indice)
                self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Selección", "Selecciona una tarea para eliminar.")