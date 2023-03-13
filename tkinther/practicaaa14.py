import tkinter as tk
from tkinter import messagebox, simpledialog
import string

class Cuenta:
    def __init__(self, num_cuenta, titular, edad, saldo):
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.edad = edad
        self.saldo = saldo
    
    def consultar_saldo(self):
        return self.saldo
    
    def ingresar_efectivo(self, cantidad):
        self.saldo += cantidad
    
    def retirar_efectivo(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No hay suficiente saldo en la cuenta.")
        self.saldo -= cantidad
    
    def depositar_a_otra_cuenta(self, otra_cuenta, cantidad):
        self.retirar_efectivo(cantidad)
        otra_cuenta.ingresar_efectivo(cantidad)

class CajaPopularApp:
    def __init__(self, cuentas):
        self.cuentas = cuentas
        
        self.root = tk.Tk()
        self.root.title("Caja Popular App")
        
        self.label_num_cuenta = tk.Label(self.root, text="Número de cuenta:" ,   bg="orange") 
        self.label_num_cuenta.pack()
        self.entry_num_cuenta = tk.Entry(self.root)
        self.entry_num_cuenta.pack()
        
        self.label_titular = tk.Label(self.root, text="Titular:" , bg="orange")
        self.label_titular.pack()
        self.entry_titular = tk.Entry(self.root)
        self.entry_titular.pack()
        
        self.label_edad = tk.Label(self.root, text="Edad:" , bg="orange")
        self.label_edad.pack()
        self.entry_edad = tk.Entry(self.root)
        self.entry_edad.pack()
        
        self.label_saldo = tk.Label(self.root, text="Saldo:" , bg="orange")
        self.label_saldo.pack()
        self.entry_saldo = tk.Entry(self.root)
        self.entry_saldo.pack()
        
        self.btn_agregar_cuenta = tk.Button(self.root, text="Agregar cuenta",  fg="green" ,command=self.agregar_cuenta)
        self.btn_agregar_cuenta.pack()
        
        self.btn_eliminar_cuenta = tk.Button(self.root, text="Eliminar cuenta", fg="green" , command=self.eliminar_cuenta)
        self.btn_eliminar_cuenta.pack()
        
        self.btn_consultar_saldo = tk.Button(self.root, text="Consultar saldo",  fg="green" ,command=self.consultar_saldo)
        self.btn_consultar_saldo.pack()
        
        self.btn_ingresar_efectivo = tk.Button(self.root, text="Ingresar efectivo", fg="green" , command=self.ingresar_efectivo)
        self.btn_ingresar_efectivo.pack()
        
        self.btn_retirar_efectivo = tk.Button(self.root, text="Retirar efectivo",  fg="green" ,command=self.retirar_efectivo)
        self.btn_retirar_efectivo.pack()
        
        self.btn_depositar_otra_cuenta = tk.Button(self.root, text="Depositar a otra cuenta", fg="green" ,command=self.depositar_a_otra_cuenta)
        self.btn_depositar_otra_cuenta.pack()
        
    def run(self):
        self.root.mainloop()
        
    def get_selected_cuenta(self):
        num_cuenta = self.entry_num_cuenta.get()
        for cuenta in self.cuentas:
            if cuenta.num_cuenta == num_cuenta:
                return cuenta
        raise ValueError("No se encontró una cuenta con el número especificado.")
        
   

  

    def agregar_cuenta(self):
        try:
            num_cuenta = self.entry_num_cuenta.get()
            titular = self.entry_titular.get()
            edad = int(self.entry_edad.get())
            saldo = float(self.entry_saldo.get())
            cuenta = Cuenta(num_cuenta, titular, edad, saldo)
            self.cuentas.append(cuenta)
            messagebox.showinfo("Cuenta agregada", f"Se agregó la cuenta con número {num_cuenta}.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def eliminar_cuenta(self):
        try:
            cuenta = self.get_selected_cuenta()
            self.cuentas.remove(cuenta)
            messagebox.showinfo("Cuenta eliminada", f"Se eliminó la cuenta con número {cuenta.num_cuenta}.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def consultar_saldo(self):
        try:
            cuenta = self.get_selected_cuenta()
            saldo = cuenta.consultar_saldo()
            messagebox.showinfo("Saldo", f"El saldo de la cuenta {cuenta.num_cuenta} es {saldo}.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def ingresar_efectivo(self):
        try:
            cuenta = self.get_selected_cuenta()
            cantidad = simpledialog.askfloat("Ingresar efectivo", "Ingrese la cantidad de efectivo:")
            cuenta.ingresar_efectivo(cantidad)
            messagebox.showinfo("Operación exitosa", f"Se ingresó {cantidad} de efectivo a la cuenta {cuenta.num_cuenta}.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def retirar_efectivo(self):
        try:
            cuenta = self.get_selected_cuenta()
            cantidad = simpledialog.askfloat("Retirar efectivo", "Ingrese la cantidad de efectivo:")
            cuenta.retirar_efectivo(cantidad)
            messagebox.showinfo("Operación exitosa", f"Se retiró {cantidad} de efectivo de la cuenta {cuenta.num_cuenta}.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    

    def depositar_a_otra_cuenta(self):
        try:
            cuenta_origen = self.get_selected_cuenta()
            num_cuenta_destino = simpledialog.askstring("Depositar a otra cuenta", "Ingrese el número de cuenta de destino:")
            cuenta_destino = None
            for cuenta in self.cuentas:
                if cuenta.num_cuenta == num_cuenta_destino:
                    cuenta_destino = cuenta
                    break
            if cuenta_destino is None:
                raise ValueError("No se encontró una cuenta con el número especificado.")
            cantidad = simpledialog.askfloat("Depositar a otra cuenta", "Ingrese la cantidad de efectivo a depositar:")
            cuenta_origen.depositar_a_otra_cuenta(cuenta_destino, cantidad)
            messagebox.showinfo("Éxito", "Efectivo depositado exitosamente.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except TypeError:
            pass
    
app = CajaPopularApp([])
app.run()