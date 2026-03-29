#en este archivo almacenamos las funciones que permiten a las opciones del menu interactivo ejecutarse#


import csv

inventario=[]

def incluir_producto(nombre, precio_unidad, cantidad):
    producto = {
        "nombre":nombre,
        "precio_unidad": precio_unidad,
        "cantidad": cantidad
        }
    inventario.append(producto)

def eliminar_producto(nombre):
    for producto in inventario:
        if producto['nombre']== nombre:
            inventario.remove(producto)
            print(f"Producto {nombre} eliminado. ")

def actualizar_producto(nombre, precio_unidad=None, cantidad=None):
    for producto in inventario:
        if producto['nombre']==nombre:
            if precio_unidad is not None:
                producto['precio_unidad']=precio_unidad
        if cantidad is not None:
            producto['cantidad']=cantidad
        print(f"Producto {nombre} actualizado. ")
        return

    print(f"producto{nombre} no encontrado.")

def mostrar_producto(nombre):
    for producto in inventario:
        if producto['nombre']== nombre:
            print(f"Nombre: {producto['nombre']}, Precio unidad: {producto['precio_unidad']}, Cantidad: {producto['cantidad']}")
            return
    print(f"Producto {nombre} no encontrado")


def mostrar_inventario():
    for producto in inventario:
        print(f"Nombre:{producto['nombre']}, Precio unidad: {producto['precio_unidad']}, Cantidad: {producto['cantidad']}")
        
def guardar_inventario(archivo):
    with open(archivo, 'w', newline='') as csvfile:
        fieldnames=['nombre', 'precio_unidad', 'cantidad']
        writer= csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for producto in inventario:
            writer.writerow(producto)


def cargar_inventario(archivo):
    try:
        with open(archivo, 'r',newline='') as csvfile:
            reader= csv.DictReader(csvfile)
            inventario.clear()
            for row in reader:
                producto={
                    'nombre': row['nombre'],
                    'precio_unidad': float(row['precio_unidad']),
                    'cantidad': int(row['cantidad'])
                }
                inventario.append(producto)
                print(f"producto cargado: {producto}")
        print(f"inventario cargado desde {archivo}")
    except FileNotFoundError:
        print(f"Error: El archivo{archivo} no existe...")
    except Exception as e:
        print(f"Error al cargar inventario:{e}")

def estadisticas(inventario):
    if not inventario:
        print("Inventario vacío")
        return
    valor_total= sum(producto['precio_unidad']* producto['cantidad'] for producto in inventario)
    cantidad_total= sum(producto['cantidad'] for producto in inventario)
    producto_caro= max(inventario, key=lambda producto: producto['precio_unidad'])
    producto_cantidad= max(inventario, key=lambda producto:producto['cantidad'])
    print("\n=== Estadisticas del inventario ===")
    print(f"Valor total del inventario:  ${valor_total:.2f}")
    print(f"Cantidad total de unidades: {cantidad_total}")
    print(f"Producto mas caro: {producto_caro['nombre']} (${producto_caro['precio_unidad']:.2f})")
    print(f"Producto con mayor cantidad: {producto_cantidad['nombre']} ({producto_cantidad['cantidad']} unidades)")
    print("=================================================================\n")

