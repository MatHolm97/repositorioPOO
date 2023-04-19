import tkinter as tk
import sqlite3
from tkinter import messagebox


conn = sqlite3.connect('BD_Banco.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS TBCuentas (IDCuenta INTEGER PRIMARY KEY AUTOINCREMENT, NoCuenta INTEGER, Saldo INTEGER)')


def agregar_cuenta():
    no_cuenta = no_cuenta_entry.get()
    saldo = saldo_entry.get()
    c.execute('INSERT INTO TBCuentas (NoCuenta, Saldo) VALUES (?, ?)', (no_cuenta, saldo))
    conn.commit()
    no_cuenta_entry.delete(0, tk.END)
    saldo_entry.delete(0, tk.END)
    messagebox.showinfo("Éxito", "Registro guardado con éxito.")



def mostrar_cuentas():
    c.execute('SELECT * FROM TBCuentas')
    cuentas = c.fetchall()
    mensaje = ''
    for cuenta in cuentas:
        mensaje += str(cuenta) + '\n'
    messagebox.showinfo("Cuentas", mensaje)
    

root = tk.Tk()
root.title('Banco')
no_cuenta_label = tk.Label(root, text='Número de Cuenta:')
no_cuenta_label.grid(row=0, column=0)
no_cuenta_entry = tk.Entry(root)
no_cuenta_entry.grid(row=0, column=1)
saldo_label = tk.Label(root, text='Saldo:')
saldo_label.grid(row=1, column=0)
saldo_entry = tk.Entry(root)
saldo_entry.grid(row=1, column=1)
agregar_button = tk.Button(root, text='Agregar cuenta', command=agregar_cuenta)
agregar_button.grid(row=2, column=0)
mostrar_button = tk.Button(root, text='Mostrar cuentas', command=mostrar_cuentas)
mostrar_button.grid(row=2, column=1)


root.mainloop()

     
conn.close()