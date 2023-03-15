import tkinter as tk
from alumno import Alumno



class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Crear etiquetas y campos de entrada para cada dato del alumno
        self.etiqueta_nombre = tk.Label(self, text="Nombre:")
        self.campo_nombre = tk.Entry(self)
        
        self.etiqueta_apellido_paterno = tk.Label(self, text="Apellido paterno:")
        self.campo_apellido_paterno = tk.Entry(self)
        
        self.etiqueta_apellido_materno = tk.Label(self, text="Apellido materno:")
        self.campo_apellido_materno = tk.Entry(self)
        
        self.etiqueta_año_nacimiento = tk.Label(self, text="Año de nacimiento:")
        self.campo_año_nacimiento = tk.Entry(self)
        
        self.etiqueta_carrera = tk.Label(self, text="Carrera:")
        self.campo_carrera = tk.Entry(self)
        
        # Crear un botón para generar la matrícula
        self.boton_generar_matricula = tk.Button(self, text="Generar matrícula", command=self.generar_matricula)
        
        # Crear una etiqueta para mostrar la matrícula generada
        self.etiqueta_matricula = tk.Label(self, text="")
        
    def generar_matricula(self):
        # Obtener los datos ingresados por el usuario
        nombre = self.campo_nombre.get()
        apellido_paterno = self.campo_apellido_paterno.get()
        apellido_materno = self.campo_apellido_materno.get()
        año_nacimiento = self.campo_año_nacimiento.get()
        carrera = self.campo_carrera.get()
        
        # Crear un objeto Alumno con los datos ingresados
        alumno = Alumno(nombre, apellido_paterno, apellido_materno, año_nacimiento, carrera)
        
        # Generar la matrícula y mostrarla en la etiqueta correspondiente
        matricula = alumno.generar_matricula()
       
