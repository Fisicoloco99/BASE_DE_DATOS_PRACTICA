import sqlite3
import tkinter as tk

conexion = sqlite3.connect("base de datos en grupo.db")
cursor = conexion.cursor()
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

def agregar_data():
    t1 = entrada_nombre.get()
    t2 = entrada_precio.get()
    t3 = entrada_stock.get()
    cursor.execute("INSERT INTO productos (nombre_producto, presio, stock) VALUES (?, ?, ?)", (t1, t2, t3))
    conexion.commit()   
    ver_lista() 

def eliminar_data():
    t1 = entrada_id.get()
    cursor.execute("DELETE FROM productos WHERE id = ?", (t1,))
    conexion.commit()
    ver_lista()

# ==========================================
# VENTANA PRINCIPAL
# ==========================================
ventana = tk.Tk()
ventana.title("Supermercado")
ventana.geometry("700x600")

# --- PALETA DE COLORES ---
COLOR_FONDO = "lightgreen" 
COLOR_TEXTO = "#003300" # Un verde bosque oscuro,esto es para probar asi contrasta

ventana.config(bg=COLOR_FONDO)

# 1. FRAME SUPERIOR
frame_superior = tk.Frame(ventana, bg=COLOR_FONDO)
frame_superior.pack(pady=20) 

tk.Label(frame_superior, text="Nombre del producto", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=0, column=0, padx=10)
tk.Label(frame_superior, text="Precio", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=0, column=1, padx=10)
tk.Label(frame_superior, text="Stock", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=0, column=2, padx=10)

entrada_nombre = tk.Entry(frame_superior)
entrada_nombre.grid(row=1, column=0, padx=10)
entrada_precio = tk.Entry(frame_superior)
entrada_precio.grid(row=1, column=1, padx=10)
entrada_stock = tk.Entry(frame_superior)
entrada_stock.grid(row=1, column=2, padx=10)

# 2. LISTBOX
lista = tk.Listbox(ventana, width=60, height=15, font=("Arial", 11))
lista.pack(pady=10)

# 3. FRAME DEL ID
frame_id = tk.Frame(ventana, bg=COLOR_FONDO)
frame_id.pack(pady=10)

tk.Label(frame_id, text="ID a eliminar:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(side=tk.LEFT, padx=5)
entrada_id = tk.Entry(frame_id, width=10)
entrada_id.pack(side=tk.LEFT)

# 4. FRAME INFERIOR (Botones)
frame_botones = tk.Frame(ventana, bg=COLOR_FONDO)
frame_botones.pack(fill="x", padx=50, pady=20) 

# Fijate que aca le agregue fg="white" al boton azul para que se lea
boton_agregar = tk.Button(frame_botones, text="AGREGAR PRODUCTO", command=agregar_data, font=("Arial", 12), bg="blue", fg="white")
boton_agregar.pack(side=tk.LEFT)

# Y aca tambien le puse fg="white" para que resalte mas
boton_eliminar = tk.Button(frame_botones, text="ELIMINAR PRODUCTO", command=eliminar_data, font=("Arial", 12), bg="red", fg="white")
boton_eliminar.pack(side=tk.RIGHT)

ver_lista()

ventana.mainloop()