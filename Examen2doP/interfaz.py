import tkinter as tk
from tkinter import messagebox
from estudiante import Estudiante

class Interfaz:
    def __init__(self, master):
        self.master = master
        master.title("Generador de matrículas")

        # Crear etiquetas
        tk.Label(master, text="Nombre:").grid(row=0)
        tk.Label(master, text="Apellido Paterno:").grid(row=1)
        tk.Label(master, text="Apellido Materno:").grid(row=2)
        tk.Label(master, text="Año de nacimiento:").grid(row=3)
        tk.Label(master, text="Carrera:").grid(row=4)

        # Crear campos de entrada
        self.entry_nombre = tk.Entry(master)
        self.entry_apellido_paterno = tk.Entry(master)
        self.entry_apellido_materno = tk.Entry(master)
        self.entry_año_nacimiento = tk.Entry(master)
        self.entry_carrera = tk.Entry(master)

        # Colocar campos de entrada
        self.entry_nombre.grid(row=0, column=1)
        self.entry_apellido_paterno.grid(row=1, column=1)
        self.entry_apellido_materno.grid(row=2, column=1)
        self.entry_año_nacimiento.grid(row=3, column=1)
        self.entry_carrera.grid(row=4, column=1)

        # Crear botón
        self.button_generar_matricula = tk.Button(master, text="Generar matrícula", command=self.generar_matricula)
        self.button_generar_matricula.grid(row=5, columnspan=2)

    def generar_matricula(self):
        nombre = self.entry_nombre.get()
        apellido_paterno = self.entry_apellido_paterno.get()
        apellido_materno = self.entry_apellido_materno.get()
        año_nacimiento = int(self.entry_año_nacimiento.get())
        carrera = self.entry_carrera.get()

        estudiante = Estudiante(nombre, apellido_paterno, apellido_materno, año_nacimiento, carrera)
        matricula = estudiante.generar_matricula()

        messagebox.showinfo("Matrícula generada", f"La matrícula generada es: {matricula}")
        
    


    
  

