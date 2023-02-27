from tkinter import Tk,Button,Frame,messagebox

def mostrarMensajes():
    messagebox.showinfo("Aviso","Presionaste boton azul")

#1 ventana
ventana= Tk()
ventana.title("Ejemplo de 3 frames")
ventana.geometry("600x400")

#2 agregamos frames
seccion1= Frame (ventana,bg="yellow")
seccion1.pack(expand=True,fill='both')

seccion2= Frame (ventana,bg="blue")
seccion2.pack(expand=True,fill='both')

seccion3= Frame (ventana,bg="red")
seccion3.pack(expand=True,fill='both')

#3 Agregar boton
botonAzul= Button(seccion1,text="boton azul",fg="blue" , command=mostrarMensajes)
botonAzul.place(x=250,y=45)

botonNaranja= Button(seccion2,text="boton naranja",fg="orange")
botonNaranja.grid(row=0, column=0)

botonRosa= Button(seccion2,text="boton rosa",fg="pink")
botonRosa.grid(row=1, column=0)

botonVerde= Button(seccion3,text="boton verde",fg="green")
botonVerde.pack()



# llamamos main
ventana.mainloop()