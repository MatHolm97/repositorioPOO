from tkinter import *
from tkinter import ttk
import tkinter as tk 
from controladorBD import * 

controlador= controladorBD()

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get, varCor.get, varCon.get())
    
def ejecutarSelect():
    rsUsuario= controlador.consultaUsuario(varBus.get())
    
    for usu in rsUsuario:
        cadena= str(usu[0])+" "+ usu[1]+" "+ usu[2]+" " + str(usu[3])
        
        if(rsUsuario):
            print(cadena)
        else:
            messagebox.showinfo("Success","Success")
        
       

Ventana= Tk()
Ventana.title("CRUD Usuarios")
Ventana.geometry("500x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)

titulo= Label(pestana1, text="Registro de Usuarios", fg="blue" ,font=("Modern",18) ).pack()

varNom= tk.StringVar()
lblNom= Label(pestana1, text="Nombre: ").pack()
txtNom= Entry(pestana1, textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor= Label(pestana1, text="Correo: ").pack()
txtCor= Entry(pestana1, textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon= Label(pestana1, text="NombreContraseña: ").pack()
txtCon= Entry(pestana1, textvariable=varCon).pack()

btnGuardar= Button(pestana1, text="Guardar" , command=ejecutaInsert).pack()



titulo= Label(pestana2, text=" Buscar usuario", fg="blue" ,font=("Modern",18) ).pack()

varBus= tk.StringVar()
lbid= Label(pestana2, text="id de usuario: ").pack()
txtid= Entry(pestana2, textvariable=varBus).pack()
btnBusqueda= Button(pestana2, text="Buscar", command=ejecutaSelectU).pack()

suBus=Label(pestana2,text="Registrado:",fg="blue",font=("Modern",18) ).pack()
textBus= tk.Text(pestana2,height=5,width=52).pack()


panel.add(pestana1,text="Formulario de usuarios")
panel.add(pestana2,text="Buscar Usuarios")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Actualizar Usuarios")



Ventana.mainloop()