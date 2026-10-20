import sqlite3

import tkinter as tk



conexion=sqlite3.connect("/home/programador10/Desktop/archivis/base de datos en grupo.db")

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


def ver_lista():
    
    lista.delete(0, tk.END)
    cursor.execute("SELECT * FROM productos")

    for u in cursor.fetchall():
        lista.insert(tk.END, u)
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

def md_nombre_producto():
    
    t1=entrada1.get()
    t2=entrada2.get()  
    cursor.execute("UPDATE productos SET nombre_producto = ? WHERE id = ?", (t2,t1))
    conexion.commit()
    ver_lista()

def md_presio_producto():
    
    t1=entrada1.get()
    t2=entrada2.get()  
    cursor.execute("UPDATE productos SET nombre_producto = ? WHERE id = ?", (t2,t1))
    conexion.commit()
    ver_lista()
    
def md_stock_producto():
    
    t1=entrada1.get()
    t2=entrada2.get()  
    cursor.execute("UPDATE productos SET nombre_producto = ? WHERE id = ?", (t2,t1))
    conexion.commit()
    ver_lista()


def buscar():
    
    et=int(entrada1.get())

    print("holaaaaa1")

    cursor.execute("SELECT * FROM productos WHERE id = ?", (et,))
    print("holaaaaa2")

    idbusca=cursor.fetchall()
    for i in idbusca:
        print("holaaaaa")
        print("paa")
        if et in i:
            resultado.config(text=i) 
            print("sssssssss")
        else:
            resultado.config(text="contacto no encontrado")
            print("nnnnnnnnnn")
            

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
resultado=tk.Label(ventana, text="")
resultado.pack()

tk.Button(ventana,text="agregar producto",command=agragar_data).pack()
tk.Button(ventana,text="modificar nombre de producto",command=md_nombre_producto).pack()
tk.Button(ventana,text="modificar presio del producto",command=md_presio_producto).pack()
tk.Button(ventana,text="modificar stock del producto",command=md_stock_producto).pack()
tk.Button(ventana,text="buscador",command=buscar).pack()


lista=tk.Listbox(ventana)
lista.pack()


ver_lista()

ventana.mainloop()