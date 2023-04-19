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
    messagebox.showinfo("Éxito", "Cuenta guardada con éxito.")



def mostrar_cuentas():
    c.execute('SELECT * FROM TBCuentas')
    cuentas = c.fetchall()
    mensaje = ''
    for cuenta in cuentas:
        mensaje += 'ID: ' + str(cuenta[0]) + '\n'  
        mensaje += 'No. de cuenta: ' + str(cuenta[1]) + '\n' 
        mensaje += 'Saldo: ' + str(cuenta[2]) + '\n\n'  
    messagebox.showinfo("Cuentas", mensaje)
    

def actualizar_cuenta():
    no_cuenta = no_cuenta_entry.get()
    saldo = saldo_entry.get()
    c.execute('UPDATE TBCuentas SET Saldo = ? WHERE NoCuenta = ?', (saldo, no_cuenta))
    conn.commit()
    no_cuenta_entry.delete(0, tk.END)
    saldo_entry.delete(0, tk.END)
    messagebox.showinfo("Éxito", "Cuenta actualizada con éxito.")

     

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
agregar_button = tk.Button(root, text='Insertar cuenta', command=agregar_cuenta)
agregar_button.grid(row=2, column=0)
mostrar_button = tk.Button(root, text='Consultar cuentas', command=mostrar_cuentas)
mostrar_button.grid(row=2, column=1)
actualizar_button = tk.Button(root, text='Actualizar cuenta', command=actualizar_cuenta)
actualizar_button.grid(row=2, column=2)


root.mainloop()

     
conn.close()