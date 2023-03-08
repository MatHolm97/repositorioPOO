import tkinter as tk
from tkinter import messagebox
import string
import random

class PasswordGenerator:
    def __init__(self, length=8, include_uppercase=True, include_special=True):
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_special = include_special

    def generate_password(self):
        characters = string.ascii_lowercase
        if self.include_uppercase:
            characters += string.ascii_uppercase
        if self.include_special:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for i in range(self.length))
        return password

    def check_strength(self, password):
        score = 0
        if len(password) >= 8:
            score += 1
        if any(char.isupper() for char in password):
            score += 1
        if any(char.islower() for char in password):
            score += 1
        if any(char.isdigit() for char in password):
            score += 1
        if any(char in string.punctuation for char in password):
            score += 1

        return score

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Te voy a dar una Clave secreta")
        self.master.configure(bg="blue")

        self.password_generator = PasswordGenerator()

        # Longitud de la contraseña
        self.length_frame = tk.Frame(master)
        self.length_label = tk.Label(self.length_frame, bg="#FFA500" ,text="Longitud de la contraseña:")
        self.length_label.pack(side=tk.LEFT)
        self.length_entry = tk.Entry(self.length_frame)
        self.length_entry.insert(0, "8")
        self.length_entry.pack(side=tk.LEFT)
        self.length_frame.pack()

        # Incluir mayúsculas
        self.uppercase_var = tk.BooleanVar()
        self.uppercase_var.set(True)
        self.uppercase_checkbutton = tk.Checkbutton(master, bg="blue" ,text="Incluir mayúsculas", variable=self.uppercase_var)
        self.uppercase_checkbutton.pack()

        # Incluir caracteres especiales
        self.special_var = tk.BooleanVar()
        self.special_var.set(True)
        self.special_checkbutton = tk.Checkbutton(master, bg="blue" ,text="Incluir caracteres especiales", variable=self.special_var)
        self.special_checkbutton.pack()

        # Comprobar fortaleza de la contraseña
        self.strength_var = tk.BooleanVar()
        self.strength_checkbutton = tk.Checkbutton(master, bg="blue", text="Comprobar fortaleza de la contraseña", variable=self.strength_var)
        self.strength_checkbutton.pack()

        # Botón para generar la contraseña
        self.generate_button = tk.Button(master, bg="blue",fg="orange",  text="Generar contraseña", command=self.generate_password)
        self.generate_button.pack()
        
    

        # Contraseña generada
        self.password_frame = tk.Frame(master)
        self.password_label = tk.Label(self.password_frame, bg="orange" ,text="Contraseña generada:")
        self.password_label.pack(side=tk.BOTTOM)
        self.password_entry = tk.Entry(self.password_frame)
        self.password_entry.pack(side=tk.BOTTOM)
        self.password_frame.pack()
        
        
        
        
        
        
          
    
              

    def generate_password(self):
    # Obtener la longitud de la contraseña
        try:
            length = int(self.length_entry.get())
        except ValueError:
            messagebox.showerror("Error", "La longitud debe ser un número entero")
            return

    # Generar la contraseña
        self.password_generator.length = length
        self.password_generator.include_uppercase = self.uppercase_var.get()
        self.password_generator.include_special = self.special_var.get()
        password = self.password_generator.generate_password()

    # Mostrar la contraseña generada
        self.password_entry.config(state=tk.NORMAL)
        self.password_entry.delete(0, tk.END)
        #self.password_entry.insert(0, password )
        self.password_entry.insert(0,  messagebox.showinfo("Fortaleza de la contraseña", f" la contraseña es: {password}") )
        self.password_entry.config(state=tk.DISABLED)
        self.password_entry.config(bg="blue")
        

    # Comprobar la fortaleza de la contraseña
        if self.strength_var.get():
            score = self.password_generator.check_strength(password)
            if score == 0:
                strength = "Muy débil"
            elif score == 1:
                strength = "Débil"
            elif score == 2:
                strength = "Medio"
            elif score == 3:
                strength = "Fuerte"
            else:
                strength = "Muy fuerte"

        messagebox.showinfo("Fortaleza de la contraseña", f"La fortaleza de la contraseña es: {strength}")
        
root = tk.Tk()
gui = GUI(root)
root.mainloop()



