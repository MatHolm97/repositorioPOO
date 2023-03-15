import tkinter as tk
from tkinter import messagebox
from estudiante import Estudiante

class Interfaz:
    def __init__(self, master):
        self.master = master
        master.title("Generador de matrículas" )

        
        tk.Label(master, text="Nombre:" , bg="orange").grid(row=0)
        tk.Label(master, text="Apellido Paterno:" , bg="orange").grid(row=1)
        tk.Label(master, text="Apellido Materno:" , bg="orange").grid(row=2)
        tk.Label(master, text="Año de nacimiento:" , bg="orange").grid(row=3)
        tk.Label(master, text="Carrera:" , bg="orange").grid(row=4)
        tk.Label(master, text="Año de curso:" , bg="orange").grid(row=5)

        
        self.entry_nombre = tk.Entry(master)
        self.entry_apellido_paterno = tk.Entry(master)
        self.entry_apellido_materno = tk.Entry(master)
        self.entry_año_nacimiento = tk.Entry(master)
        self.entry_carrera = tk.Entry(master)
        self.entry_año_curso = tk.Entry(master)

       
        self.entry_nombre.grid(row=0, column=1)
        self.entry_apellido_paterno.grid(row=1, column=1)
        self.entry_apellido_materno.grid(row=2, column=1)
        self.entry_año_nacimiento.grid(row=3, column=1)
        self.entry_carrera.grid(row=5, column=1)
        self.entry_año_curso.grid(row=4, column=1)

       
        self.button_generar_matricula = tk.Button(master, text="Generar matrícula",   fg="green" , command=self.generar_matricula)
        self.button_generar_matricula.grid(row=6, columnspan=2)

    def generar_matricula(self):
        nombre = self.entry_nombre.get()
        apellido_paterno = self.entry_apellido_paterno.get()
        apellido_materno = self.entry_apellido_materno.get()
        año_nacimiento = int(self.entry_año_nacimiento.get())
        carrera = self.entry_carrera.get()
        año_curso = int(self.entry_año_curso.get())

        estudiante = Estudiante(nombre, apellido_paterno, apellido_materno, año_nacimiento, carrera , año_curso)
        matricula = estudiante.generar_matricula()

        messagebox.showinfo("Matricula generada", f"La matricula generada es: {matricula}")
        
    


    
  

