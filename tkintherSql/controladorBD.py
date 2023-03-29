from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init(self):
        pass
    
    def conexionBD(self):
        try: 
            conexion= sqlite3.connect("/Users/matiashernandezdelolmo/Downloads/5CuatriUpq/POO/repositorio/DBusuarios.db")
            print("Conectado ")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
            
    def guardarUsuario(self,nom,cor,con):
        
        conx= self.conexionBD()
        
        if(nom == "" or cor == "" or con == ""):
            messagebox.showwarning("Aguas","Revisa tus datos")
            conx.close()
        else:
            cursor= conx.cursor()
            conH= self.encriptarCon(con)
            datos=(nom,cor,conH)
            qrInsert="insert into TBRegistrados(nombre,correo,contra) values(?,?,?)" 
            
            
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Exitoso")  
            
    
    def encriptarCon(self,con):
        conPlana= con 
        conPlana= conPlana.encode()
        sal= bcrypt.gensalt()
        conHa= bcrypt.hashpw(conPlana,sal)
        print(conHa)
        return conHa  
    
    def consultaUsuario(self,id):
        conx= self.conexionBD()
        
        if(id == ""):
            messagebox.showwarning("Cuidado", " Id vacio")
            
        else:
            try:
                cursor= conx.cursor()
                sqlSelect= "select * from TBRegistrados where id="+id
                
                cursor.execute(sqlSelect)
                RSusuario= cursor.fetchall()
                conx.close()
                
                return RSusuario
            except sqlite3.OperationError:
                print("Error Consulta")