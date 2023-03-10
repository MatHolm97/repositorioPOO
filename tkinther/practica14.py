import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
import string

class Cuenta:
    def __init__(self, numero, titular, edad, saldo):
        self.numero = numero
        self.titular = titular
        self.edad = edad
        self.saldo = saldo

    def ingresar_efectivo(self, cantidad):
        self.saldo += cantidad

    def retirar_efectivo(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Error: Saldo insuficiente")

    def depositar_otra_cuenta(self, cuenta_destino, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            cuenta_destino.ingresar_efectivo(cantidad)
        else:
            print("Error: Saldo insuficiente")

class CajaPopular:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def eliminar_cuenta(self, numero):
        for cuenta in self.cuentas:
            if cuenta.numero == numero:
                self.cuentas.remove(cuenta)
                break

    def buscar_cuenta(self, numero):
        for cuenta in self.cuentas:
            if cuenta.numero == numero:
                return cuenta
        return None

class InterfazGrafica:
    def __init__(self, caja_popular):
        self.caja_popular = caja_popular

        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Caja Popular")

        # Crear los widgets
        self.etiqueta_numero = tk.Label(self.ventana, text="Número de cuenta:")
        self.cuadro_numero = tk.Entry(self.ventana)

        self.etiqueta_titular = tk.Label(self.ventana, text="Titular:")
        self.cuadro_titular = tk.Entry(self.ventana)

        self.etiqueta_edad = tk.Label(self.ventana, text="Edad:")
        self.cuadro_edad = tk.Entry(self.ventana)

        self.etiqueta_saldo = tk.Label(self.ventana, text="Saldo:")
        self.cuadro_saldo = tk.Entry(self.ventana)

        self.boton_agregar = tk.Button(self.ventana, text="Agregar cuenta", command=self.agregar_cuenta)
        self.boton_eliminar = tk.Button(self.ventana, text="Eliminar cuenta", command=self.eliminar_cuenta)
        self.boton_consultar = tk.Button(self.ventana, text="Consultar saldo", command=self.consultar_saldo)
        self.boton_ingresar = tk.Button(self.ventana, text="Ingresar efectivo", command=self.ingresar_efectivo)
        self.boton_retirar = tk.Button(self.ventana, text="Retirar efectivo", command=self.retirar_efectivo)
        self.boton_depositar = tk.Button(self.ventana, text="Depositar a otra cuenta", command=self.depositar_otra_cuenta)

        # Colocar los widgets en la ventana
        self.etiqueta_numero.grid(row=0, column=0)
        self.cuadro_numero.grid(row=0, column=1)

        self.etiqueta_titular.grid(row=1, column=0)
        self.cuadro_titular.grid(row=1, column=1)

        self.etiqueta_edad.grid(row=2, column=0)
        self.cuadro_edad.grid(row=2, column=1)

        self.etiqueta_saldo.grid(row=3, column=0)
        self.cuadro_saldo.grid(row=3, column=1)

        self.boton_agregar.grid(row=4, column=0)
        self.boton_eliminar.grid(row=4, column=1)
        self.boton_consultar.grid(row=5, column=0)
        self.boton_ingresar.grid(row=5, column=1)
        self.boton_retirar.grid(row=6, column=0)
        self.boton_depositar.grid(row=6, column=1)

    def agregar_cuenta(self):
        numero = self.cuadro_numero.get()
        titular = self.cuadro_titular.get()
        edad = self.cuadro_edad.get()
        saldo = self.cuadro_saldo.get()
        messagebox.showinfo("Cuenta nueva", f" LA cuenta nueva es : {numero}")
        
        cuenta = Cuenta(numero, titular, edad, saldo)
        self.caja_popular.agregar_cuenta(cuenta)
        

    def eliminar_cuenta(self):
        numero = self.cuadro_numero.get()

        self.caja_popular.eliminar_cuenta(numero)
        messagebox.showinfo("Cuenta eliminar", f" cuenta eliminada : {numero}")

    def consultar_saldo(self):
        numero = self.cuadro_numero.get()

        cuenta = self.caja_popular.buscar_cuenta(numero)
        

        if cuenta is not None:
            saldo = cuenta.saldo
            tk.messagebox.showinfo("Saldo", f"El saldo de la cuenta {numero} es de {saldo}")
        else:
            tk.messagebox.showerror("Error", "No se encontró la cuenta")

    def ingresar_efectivo(self):
        numero = self.cuadro_numero.get()
        cantidad = simpledialog.askfloat("Ingresar efectivo", "Cantidad a ingresar:")

        cuenta = self.caja_popular.buscar_cuenta(numero)

        if cuenta is not None:
            cuenta.ingresar_efectivo(cantidad)
            tk.messagebox.showinfo("Éxito", f"Se ingresó {cantidad} a la cuenta {numero}")
        else:
            tk.messagebox.showerror("Error", "No se encontró la cuenta")

    def retirar_efectivo(self):
        numero = self.cuadro_numero.get()
        cantidad = simpledialog.askfloat("Retirar efectivo", "Cantidad a retirar:")

        cuenta = self.caja_popular.buscar_cuenta(numero)

        if cuenta is not None:
            if cuenta.saldo >= cantidad:
                cuenta.retirar_efectivo(cantidad)
                tk.messagebox.showinfo("Éxito", f"Se retiró {cantidad} de la cuenta {numero}")
            else:
                tk.messagebox.showerror("Error", "Saldo insuficiente")
        else:
            tk.messagebox.showerror("Error", "No se encontró la cuenta")

    def depositar_otra_cuenta(self):
        numero_origen = self.cuadro_numero.get()
        numero_destino = simpledialog.askstring("Depositar a otra cuenta", "Número de cuenta destino:")
        cantidad = simpledialog.askfloat("Depositar a otra cuenta", "Cantidad a depositar:")
        messagebox.showinfo("Cuenta", f" La cantidad es : {cantidad}")

        cuenta_origen = self.caja_popular.buscar_cuenta(numero_origen)
        cuenta_destino = self.caja_popular.buscar_cuenta(numero_destino)

        if cuenta_origen is not None and cuenta_destino is not None:
            if cuenta_origen.saldo >= cantidad:
                cuenta_origen.retirar_efectivo(cantidad)
                cuenta_destino.ingresar_efectivo(cantidad)
                tk.messagebox.showinfo("Éxito", f"Se depositaron {cantidad} de la cuenta {numero_origen} a la cuenta {numero_destino}")
            else:
                tk.messagebox.showerror("Error", "Saldo insuficiente")
        else:
            tk.messagebox.showerror("Error", "No se encontró una de las cuentas")

       
root = tk.Tk()
interfazgrafica = InterfazGrafica(root)
root.mainloop()

