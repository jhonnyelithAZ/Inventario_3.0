#con esta linea de codigo permitimos utilizar las funciones alojadas en el archivo inventario.py#
from src.inventario import *

#aca utilizamos un ciclo while true para ejecutar el print del menu hasta que se seleccione la opcion salir#
while True:
    print("inventario de productos :\n")
    print("1.agregar producto")
    print("2.eliminar producto")
    print("3.actualizar producto")
    print("4.mostrar un producto")
    print("5.mostrar inventario completo")
    print("6.estadisticas")
    print("7.guardar inventario")
    print("8.cargar inventario")
    print("9.salir\n")
#se le pide al usuario que ingrese una opcion del menu,si la opcion no es valida se repetira el menu#
    opcion = input("elija una opcion caballero/dama: ")

    if opcion=="1":
        nombre=input ("ingrese el nombre: ")
        precio_unidad=float(input("ingrese el valor unitario: "))
        cantidad=int(input("ingrese cuantos: "))
        incluir_producto(nombre, precio_unidad, cantidad)

    elif opcion=="2":
        nombre=input("ingrese el nombre del producto a eliminar: ")
        eliminar_producto(nombre)

    elif opcion=="3":
        nombre=input("ingrese el nombre del producto a actualizar: ")
        precio_unidad=float(input("ingrese el nuevo precio por unidad: "))
        cantidad=int(input("ingrese la nueva cantidad de unidades: "))
        actualizar_producto(nombre, precio_unidad, cantidad)

    elif opcion=="4":
        nombre=input("ingrese el nombre del producto a mostrar:")
        mostrar_producto(nombre)

    elif opcion == "5":
        mostrar_inventario()


    elif opcion=="6":
        estadisticas()

    elif opcion == "7":
        guardar_inventario()
#con esta opcion detenemos el ciclo y salimos del programa#
    elif opcion == "9":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida. por favor, intente de nuevo.")


