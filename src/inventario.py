inventario={}

def incluir_producto(nombre, precio_unidad, cantidad):
    inventario[nombre] = {"precio_unidad": precio_unidad, "cantidad": cantidad}

def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"producto '{nombre}' eliminado del inventario. ")
    else:
        print(f"producto '{nombre}' no encontrado en el inventario.")

def actualizar_producto(nombre, precio_unidad, cantidad):
    if nombre in inventario:
        inventario[nombre]["precio_unidad"] = precio_unidad
        inventario[nombre]["cantidad"] = cantidad
    else:
        print("producto no encontrado")

def mostrar_producto(nombre):
    if nombre in inventario:
        print(f"Nombre: {nombre}, Precio unidad: {inventario[nombre]["precio_unidad"]}, Cantidad: {inventario[nombre]["cantidad"]}")
    else:
        print("producto no encontrado.")

def mostrar_inventario():
    print("Inventario completo:")
    for nombre,producto in inventario.items():
        print(f"Nombre:{nombre}, Precio unidad: {producto['precio_unidad']}, Cantidad: {producto['cantidad']}")



#en este archivo almacenamos las funciones que permiten a las opciones del menu interactivo ejecutarse#