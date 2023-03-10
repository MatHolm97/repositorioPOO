from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
import string

class Cajero:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def eliminar_cuenta(self, cuenta):
        self.cuentas.remove(cuenta)

    def depositar(self, cuenta, cantidad):
        cuenta.saldo += cantidad

    def retirar(self, cuenta, cantidad):
        cuenta.saldo -= cantidad

    def transferir(self, cuenta_origen, cuenta_destino, cantidad):
        cuenta_origen.saldo -= cantidad
        cuenta_destino.saldo += cantidad

class Cuenta:
    def __init__(self, num_cuenta, titular, edad, saldo):
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.edad = edad
        self.saldo = saldo

class Interfaz:
    def __init__(self, master):
        self.master = master
        self.cajero = Cajero()

        # Crear widgets
        self.label_cuentas = Label(self.master, text="Cuentas")
        self.listbox_cuentas = Listbox(self.master, width=40)
        self.label_num_cuenta = Label(self.master, text="No. Cuenta:")
        self.entry_num_cuenta = Entry(self.master)
        self.label_titular = Label(self.master, text="Titular:")
        self.entry_titular = Entry(self.master)
        self.label_edad = Label(self.master, text="Edad:")
        self.entry_edad = Entry(self.master)
        self.label_saldo = Label(self.master, text="Saldo:")
        self.entry_saldo = Entry(self.master)
        self.button_crear_cuenta = Button(self.master, text="Crear Cuenta", command=self.crear_cuenta)
        self.button_eliminar_cuenta = Button(self.master, text="Eliminar Cuenta", command=self.eliminar_cuenta)
        self.label_info_cuenta = Label(self.master, text="Información de la cuenta seleccionada")
        self.label_info_num_cuenta = Label(self.master, text="No. Cuenta:")
        self.label_info_titular = Label(self.master, text="Titular:")
        self.label_info_edad = Label(self.master, text="Edad:")
        self.label_info_saldo = Label(self.master, text="Saldo:")
        self.label_info_saldo_valor = Label(self.master, text="")
        self.button_ingresar_efectivo = Button(self.master, text="Ingresar Efectivo", command=self.ingresar_efectivo)
        self.button_retirar_efectivo = Button(self.master, text="Retirar Efectivo", command=self.retirar_efectivo)
        self.button_depositar_otra_cuenta = Button(self.master, text="Depositar a otra Cuenta", command=self.depositar_otra_cuenta)

        # Organizar widgets en la ventana
        self.label_cuentas.grid(row=0, column=0, sticky=W)
        self.listbox_cuentas.grid(row=1, column=0, rowspan=4, sticky=NSEW)
        self.label_num_cuenta.grid(row=1, column=1, sticky=W)
        self.entry_num_cuenta.grid(row=1, column=2, sticky=W)
        self.label_titular.grid(row=2, column=1, sticky=W)
        self.entry_titular.grid(row=2, column=2, sticky=W)
        self.label_edad.grid(row=3, column=1, sticky=W)
        self.entry_edad.grid(row=3, column=2, sticky=W)
        self.label_saldo.grid(row=4, column=1, sticky=W)
        self.entry_saldo.grid(row=4, column=2, sticky=W)
        self.button_crear_cuenta.grid(row=5, column=0, columnspan=3)
        self.button_eliminar_cuenta.grid(row=6, column=0, columnspan=3)
        self.label_info_cuenta.grid(row=0, column=3, sticky=W)
        self.label_info_num_cuenta.grid(row=1, column=3, sticky=W)
        self.label_info_titular.grid(row=2, column=3, sticky=W)
        self.label_info_edad.grid(row=3, column=3, sticky=W)
        self.label_info_saldo.grid(row=4, column=3, sticky=W)
        self.label_info_saldo_valor.grid(row=4, column=4, sticky=W)
        self.button_ingresar_efectivo.grid(row=5, column=3, columnspan=2)
        self.button_retirar_efectivo.grid(row=6, column=3, columnspan=2)
        self.button_depositar_otra_cuenta.grid(row=7, column=3, columnspan=2)

        # Configurar eventos
        self.listbox_cuentas.bind('<<ListboxSelect>>', self.mostrar_info_cuenta)

    def crear_cuenta(self):
        num_cuenta = self.entry_num_cuenta.get()
        titular = self.entry_titular.get()
        edad = self.entry_edad.get()
        saldo = self.entry_saldo.get()
        cuenta = Cuenta(num_cuenta, titular, edad, saldo)
        self.cajero.agregar_cuenta(cuenta)
        self.listbox_cuentas.insert(END, cuenta.num_cuenta)

    def eliminar_cuenta(self):
        cuenta = self.obtener_cuenta_seleccionada()
        self.cajero.eliminar_cuenta(cuenta)
        self.listbox_cuentas.delete(ANCHOR)

    def mostrar_info_cuenta(self, event):
        cuenta = self.obtener_cuenta_seleccionada()
        self.label_info_num_cuenta.config(text="No. Cuenta: {}".format(cuenta.num_cuenta))
        self.label_info_titular.config(text="Titular: {}".format(cuenta.titular))
        self.label_info_edad.config(text="Edad: {}".format(cuenta.edad))
        self.label_info_saldo_valor.config(text=cuenta.saldo)

    def obtener_cuenta_seleccionada(self):
        index = self.listbox_cuentas.curselection()[0]
        num_cuenta = self.listbox_cuentas.get(index)
        for cuenta in self.cajero.cuentas:
            if cuenta.num_cuenta == num_cuenta:
                return cuenta

    def ingresar_efectivo(self):
        cuenta = self.obtener_cuenta_seleccionada()
        cantidad = simpledialog.askinteger("Ingresar Efectivo", "Cantidad a ingresar:")
        self.cajero.depositar(cuenta, cantidad)
        self.mostrar_info_cuenta(None)

    def retirar_efectivo(self):
        cuenta = self.obtener_cuenta_seleccionada()
        cantidad = simpledialog.askinteger("Retirar Efectivo", "Cantidad a retirar:")
        if cantidad is not None:
           retirado = self.cajero.retirar(cuenta, cantidad)
           
        if retirado:
            self.mostrar_info_cuenta(None)
            
        else:
         messagebox.showerror("Error", "No se puede retirar la cantidad especificada")
         
         
    def depositar_otra_cuenta(self):
        cuenta_origen = self.obtener_cuenta_seleccionada()
        cuenta_destino = simpledialog.askstring("Depositar en otra cuenta", "No. Cuenta destino:")
        cantidad = simpledialog.askinteger("Depositar en otra cuenta", "Cantidad a depositar:")
        if cuenta_destino is not None and cantidad is not None:
            depositado = self.cajero.depositar_otra_cuenta(cuenta_origen, cuenta_destino, cantidad)
            if depositado:
                self.mostrar_info_cuenta(None)
            else:
                messagebox.showerror("Error", "No se puede depositar la cantidad especificada")


app = Cajero()
root.mainloop()
cajero = Cajero(root)