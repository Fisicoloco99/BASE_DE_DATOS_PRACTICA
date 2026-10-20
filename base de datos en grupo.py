#pautas: Productos(supermercado). Un campo para ingresar nombre de producto, un campo para cargar precios, un campo para cargar stock. Un boton agregar producto. una tabla de productos registrados. Un boton para eliminar productos.
# Tabla productos con id, nom, precio, stock. Las funciones asociadas a los botones
import sqlite3

import tkinter as tk



conexion=sqlite3.connect("base de datos.db")

cursor=conexion.cursor()
cursor.execute(""" 
         
CREATE TABLE IF NOT EXISTS productos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre_producto TEXT,
presio INTEGER,
stock INTEGER

)            
""")   
conexion.commit()

def limpiar_entry():
    entrada1.delete(0,tk.END)
    entrada2.delete(0,tk.END)
    entrada3.delete(0,tk.END)
    entrada4.delete(0,tk.END)

def ver_lista():
    
    
    lista.delete(0, tk.END)
    cursor.execute("SELECT * FROM productos")


    cursor.execute("SELECT * FROM productos")
    for alumno in cursor.fetchall():
        lista.insert(tk.END, alumno)
        print("222")

def agragar_data():
    t1=entrada2.get()
    t2=entrada3.get()
    t3=entrada4.get()

    cursor.execute(
                
    "INSERT INTO productos (nombre_producto,presio,stock) VALUES (?,?,?)",(t1,t2,t3)
                
    )
    conexion.commit()   
    ver_lista()
    limpiar_entry()

def md_nombre_producto():
    
    t1=entrada1.get()
    t2=entrada2.get()  
    cursor.execute("UPDATE productos SET nombre_producto = ? WHERE id = ?", (t2,t1))
    conexion.commit()
    ver_lista()
    limpiar_entry()

def md_presio_producto():
    
    t1=entrada1.get()
    t2=entrada2.get()  
    cursor.execute("UPDATE productos SET presio = ? WHERE id = ?", (t2,t1))
    conexion.commit()
    ver_lista()
    limpiar_entry()
    
def md_stock_producto():
    t1=entrada1.get()
    t2=entrada2.get()  
    cursor.execute("UPDATE productos SET stock = ? WHERE id = ?", (t2,t1))
    conexion.commit()
    ver_lista()
    limpiar_entry()
    
def eliminar():
    t1=entrada1.get()
    cursor.execute("DELETE FROM productos WHERE id = ?",(t1,))
    conexion.commit()
    ver_lista()
    limpiar_entry()

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
tk.Button(ventana,text="eliminar producto",command=eliminar).pack()


lista=tk.Listbox(ventana)
lista.pack()

ventana.mainloop()