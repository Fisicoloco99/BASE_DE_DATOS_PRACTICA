import sqlite3

import tkinter as tk



conexion=sqlite3.connect("/home/programador10/Desktop/archivis/base de datos.db")

cursor=conexion.cursor()
cursor.execute(""" 
         
CREATE TABLE IF NOT EXISTS usuario (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre_producto TEXT,
presio INTEGER,
stock INTEGER

)            
""")   
conexion.commit()


def ver_lista():
    
    lista.delete(0, tk.END)
    cursor.execute("SELECT * FROM usuario")


    cursor.execute("SELECT * FROM usuario")
    for alumno in cursor.fetchall():
        lista.insert(tk.END, alumno)
        print("222")

def agragar_data():
    t1=entrada2.get()
    t2=entrada3.get()
    t3=entrada4.get()

    cursor.execute(
                
    "INSERT INTO usuario (nombre_producto,presio,stock) VALUES (?,?,?)",(t1,t2,t3)
                
    )
    conexion.commit()   
    ver_lista() 

def md_nombre_producto():
    
    t1=entrada1.get()
    t2=entrada2.get()  
    cursor.execute("UPDATE usuario SET nombre_producto = ? WHERE id = ?", (t2,t1))
    conexion.commit()
    ver_lista()

def md_presio_producto():
    
    t1=entrada1.get()
    t2=entrada2.get()  
    cursor.execute("UPDATE usuario SET nombre_producto = ? WHERE id = ?", (t2,t1))
    conexion.commit()
    ver_lista()
    
def md_stock_producto():
    
    t1=entrada1.get()
    t2=entrada2.get()  
    cursor.execute("UPDATE usuario SET nombre_producto = ? WHERE id = ?", (t2,t1))
    conexion.commit()
    ver_lista()
    



ventana = tk.Tk()
ventana.title("Prueba Multiprocessing")
ventana.geometry("400x650")

resultado=tk.Label(ventana, text="ID")
resultado.pack()
entrada1=tk.Entry(ventana)
entrada1.pack()
resultado=tk.Label(ventana, text="nombre_producto")
resultado.pack()
entrada2=tk.Entry(ventana)
entrada2.pack()
resultado=tk.Label(ventana, text="presio")
resultado.pack()
entrada3=tk.Entry(ventana)
entrada3.pack()
resultado=tk.Label(ventana, text="stock")
resultado.pack()
entrada4=tk.Entry(ventana)
entrada4.pack()


tk.Button(ventana,text="agregar producto",command=agragar_data).pack()
tk.Button(ventana,text="modificar nombre de producto",command=md_nombre_producto).pack()
tk.Button(ventana,text="modificar presio del producto",command=md_presio_producto).pack()
tk.Button(ventana,text="modificar stock del producto",command=md_stock_producto).pack()



lista=tk.Listbox(ventana)
lista.pack()

ventana.mainloop()