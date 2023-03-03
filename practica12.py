from tkinter import Tk,Button,Frame,messagebox
import tkinter as tk
import validarDatos

class Usuario:
    def __init__(self, correo, contraseña):
        self.correo = correo
        self.contraseña = contraseña
    
    
    

class LoginApp:
    def __init__(self, master): 
        self.master = master
        master.title("Login")
        master.geometry("450x300")
        self.master.configure(bg="white")

        self.label_correo = tk.Label(master, text="Correo:")
        self.label_correo.grid(row=0, column=0)

        self.entry_correo = tk.Entry(master)
        self.entry_correo.grid(row=0, column=1)

        self.label_contraseña = tk.Label(master, text="Contraseña:")
        self.label_contraseña.grid(row=1, column=0)

        self.entry_contraseña = tk.Entry(master, show="*")
        self.entry_contraseña.grid(row=1, column=1)

        self.button_login = tk.Button(master, text="Iniciar sesión", bg="red",fg="green", command=self.iniciar_sesion)
        self.button_login.grid(row=2, column=1)

        self.label_mensaje = tk.Label(master, text="")
        self.label_mensaje.grid(row=3, column=1)

    def iniciar_sesion(self):
        correo = self.entry_correo.get()
        contraseña = self.entry_contraseña.get()

        # Validación de campos vacíos
        if correo == "" or contraseña == "":
            #self.label_mensaje.config(text="Por favor, ingrese su correo y contraseña.")
            messagebox.showerror("Error","Por favor, ingrese su correo y contraseña")
            return
        else:
            validarDatos.validarDatosr(correo, contraseña)
        
       
            
root = tk.Tk()
app = LoginApp(root)
root.mainloop()
