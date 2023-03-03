from tkinter import Tk,Button,Frame,messagebox
import tkinter as tk



def validarDatosr( correo, contr):
    co = "123@hotmail.com"
    passw = "1234"
    if co == correo and passw == contr:
        messagebox.showinfo("Hola", "Bienvenido")
    else:
        messagebox.showerror("Hola","correo y contraseña incorrecta")
        print(correo)