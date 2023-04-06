from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk 
from controladorBD import * 

controlador = controladorBD()

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())
    messagebox.showinfo("Éxito", "Registro guardado con éxito.")

def ejecutarSelect():
    textConsulta.delete('1.0', END) # Elimina contenido anterior
    rsUsuario = controlador.consultaUsuario(varBus.get())
    
    for usu in rsUsuario:
        cadena = str(usu[0]) + " " + usu[1] + " " + usu[2] + " " + str(usu[3])
        textConsulta.insert(END, cadena + "\n")
        
def ejecutaUpdate():
    controlador.actualizarUsuario(varNomUpdate.get(), varCorUpdate.get(), varConUpdate.get(), varIdUpdate.get())
    messagebox.showinfo("Éxito", "Registro actualizado con éxito.")
    varIdUpdate.set("")
    varNomUpdate.set("")
    varCorUpdate.set("")
    varConUpdate.set("")

def ejecutaDelete():
    result = messagebox.askyesno("Confirmación", "¿Seguro que desea eliminar este registro?")
    if result:
        controlador.eliminarUsuario(varIdDelete.get())
        messagebox.showinfo("Éxito", "Registro eliminado con éxito.")
        varIdDelete.set("")

Ventana = Tk()
Ventana.title("CRUD Usuarios")
Ventana.geometry("500x500")

panel = ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)

titulo = Label(pestana1, text="Registro de Usuarios", fg="blue" ,font=("Modern",18) )
titulo.pack()

varNom = tk.StringVar()
lblNom = Label(pestana1, text="Nombre: ")
lblNom.pack()
txtNom = Entry(pestana1, textvariable=varNom)
txtNom.pack() 

varCor = tk.StringVar()
lblCor = Label(pestana1, text="Correo: ")
lblCor.pack()
txtCor = Entry(pestana1, textvariable=varCor)
txtCor.pack()

varCon = tk.StringVar()
lblCon = Label(pestana1, text="Contraseña: ")
lblCon.pack()
txtCon = Entry(pestana1, textvariable=varCon)
txtCon.pack()

btnGuardar = Button(pestana1, text="Guardar", command=ejecutaInsert)
btnGuardar.pack()

titulo2 = Label(pestana2, text="Buscar Usuario", fg="blue", font=("Modern",18))
titulo2.pack()

varBus = tk.StringVar()
lbid = Label(pestana2, text="ID de Usuario: ")
lbid.pack()
txtid = Entry(pestana2, textvariable=varBus)
txtid.pack()
btnBusqueda = Button(pestana2, text="Buscar", command=ejecutarSelect)
btnBusqueda.pack()

suBus = Label(pestana2,text="Registrado:",fg="blue",font=("Modern",18))
suBus.pack()
textBus = tk.Text(pestana2, height=5, width=52)
textBus.pack()



frameConsulta = Frame(pestana2)
frameConsulta.pack()

varBus = tk.StringVar()
lblBus = Label(frameConsulta, text="Buscar por ID: ")
lblBus.pack(side=LEFT)
txtBus = Entry(frameConsulta, textvariable=varBus)
txtBus.pack(side=LEFT)

btnBuscar = Button(frameConsulta, text="Buscar", command=ejecutarSelect)
btnBuscar.pack(side=LEFT)

resultados = Label(frameConsulta, text="Resultados:")
resultados.pack()

textConsulta = tk.Text(frameConsulta, height=5, width=52)
textConsulta.pack()




titulo3 = Label(pestana3, text="Actualizar / Eliminar Usuario", fg="blue", font=("Modern",18))
titulo3.pack()

# Frame para actualizar usuario
frameUpdate = Frame(pestana3)
frameUpdate.pack()

varIdUpdate = tk.StringVar()
lblIdUpdate = Label(frameUpdate, text="ID de Usuario: ")
lblIdUpdate.grid(row=0, column=0)
varIdUpdate.set("")
txtIdUpdate = Entry(frameUpdate, textvariable=varIdUpdate)
txtIdUpdate.grid(row=0, column=1)

varNomUpdate = tk.StringVar()
lblNomUpdate = Label(frameUpdate, text="Nombre: ")
lblNomUpdate.grid(row=1, column=0)
txtNomUpdate = Entry(frameUpdate, textvariable=varNomUpdate)
txtNomUpdate.grid(row=1, column=1)

varCorUpdate = tk.StringVar()
lblCorUpdate = Label(frameUpdate, text="Correo: ")
lblCorUpdate.grid(row=2, column=0)
txtCorUpdate = Entry(frameUpdate, textvariable=varCorUpdate)
txtCorUpdate.grid(row=2, column=1)

varConUpdate = tk.StringVar()
lblConUpdate = Label(frameUpdate, text="Contraseña: ")
lblConUpdate.grid(row=3, column=0)
txtConUpdate = Entry(frameUpdate, textvariable=varConUpdate)
txtConUpdate.grid(row=3, column=1)

btnActualizar = Button(frameUpdate, text="Actualizar", command=ejecutaUpdate)
btnActualizar.grid(row=4, column=0)


frameDelete = Frame(pestana3)
frameDelete.pack()

varIdDelete = tk.StringVar()
lblIdDelete = Label(frameDelete, text="ID de Usuario: ")
lblIdDelete.grid(row=0, column=0)
varIdDelete.set("")
txtIdDelete = Entry(frameDelete, textvariable=varIdDelete)
txtIdDelete.grid(row=0, column=1)

btnEliminar = Button(frameDelete, text="Eliminar", command=ejecutaDelete)
btnEliminar.grid(row=1, column=0)

panel.add(pestana1, text="Registrar Usuario")
panel.add(pestana2, text="Buscar Usuario/Consulta")
panel.add(pestana3, text="Actualizar / Eliminar Usuario")

Ventana.mainloop()