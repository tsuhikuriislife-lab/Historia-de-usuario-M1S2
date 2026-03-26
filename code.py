def agregarProducto(nombre, cantidad, precio, lista):
    if nombre not in lista: #Verificamos que el nombre no este en la lista
        lista[nombre] = {"cantidad":cantidad,"precio":precio}
    else:
        lista[nombre]["cantidad"] = cantidad
        lista[nombre]["precio"] = precio

def mostrarInventario(lista):
    for i, (nombre, datos) in enumerate(lista.items(), start=1):
                print(f"Articulo #{i}\nNombre: {nombre}, cantidad: {datos["cantidad"]}, precio: {datos["precio"]}")

def calcularEstadisticas(opcion, lista):
    if opcion == "valor": #Apartado para calcular el valor total
        total = 0
        for nombre, datos in lista.items():
            calculo = datos["cantidad"]*datos["precio"]
            total += calculo
        print(f"El valor total del inventario es de: ${total}")
    elif opcion == "cantidad": #Apartado para calcular la cantidad de productos
        total = 0
        for nombre, datos in lista.items():
            calculo = datos["cantidad"]
            total += calculo
        print(f"La cantidad de productos registrados es de: {total}")
    elif opcion == "salir":
        print("Saliendo...")
    else:
        print("Ingrese una opcion valida...")

inventario = { #Creamos el diccionario donde guardaremos los valores de cada uno de los productos ingresados

}
opciones = { #Declaramos los posibles ingresos del usuario para mejor validacion de entradas
    "1":"agregar",
    "agregar":"agregar",
    "a":"agregar",
    "2":"inventario",
    "inventario":"inventario",
    "i":"inventario",
    "3":"estadisticas",
    "estadisticas":"estadisticas",
    "e":"estadisticas",
    "4":"salir",
    "salir":"salir",
    "s":"salir",
    }

opcionesCalculos = { #Declaramos los posibles ingresos del usuario para mejor validacion de entradas
    "1":"valor",
    "valor":"valor",
    "v":"valor",
    "2":"cantidad",
    "cantidad":"cantidad",
    "c":"cantidad",
    "3":"salir",
    "salir":"salir",
    "s":"salir"
}
menu_principal = True
while menu_principal:
    opcion = input("Que desea hacer?\n1. Agregar producto\n2. Mostrar inventario\n3. Calcular estadisticas\n4. Salir\n--- ") #Pedimos la opcion al usuario
    if opcion not in opciones: #Verificamos que sea una opcion valida
        print("Ingresa una opcion valida...")
        continue
    else:
        opcion = opciones[opcion]
    if opcion == "agregar": #Iniciamos con el apartado de agregar productos
        nombre = ""
        while nombre == "":#Verificamos que el usuario no deje el espacio vacio
            nombre = input("Ingresa el nombre del producto: ").lower().strip()
            if nombre == "":
                print("No puedes dejar este campo en blanco...")
        cantidad = ""
        while cantidad == "":#Verificamos que el usuario no deje el espacio vacio
            cantidad = int(input("Ingresa la cantidad del producto: ").strip())
            if cantidad == "":
                print("No puedes dejar este espacio en blanco...")
        precio = ""
        while precio == "":#Verificamos que el usuario no deje el espacio vacio
            precio = float(input("Ingrese el precio del producto: ").strip())
            if precio == "":
                print("No puedes dejar este espacio en blanco...")
        agregarProducto(nombre, cantidad, precio, inventario) #Agregamos el producto
    elif opcion == "inventario": #Apartado para mostrar el inventario
        if not inventario:
            print("El inventario está vacio...")
        else:
            mostrarInventario(inventario)
    elif opcion == "estadisticas": #Apartado para mostrar estadisticas
        opcion_estadisticas = 0
        while opcion_estadisticas != 3:
            opcion_estadisticas = input("Que estadisticas desea averiguar?\n1. Valor total de inventario\n2. Cantidad de productos registrados\n3. Salir")
            if opcion_estadisticas in opcionesCalculos:
                opcion_estadisticas =  opcionesCalculos[opcion_estadisticas]
            calcularEstadisticas(opcion_estadisticas, inventario)#Calculamos las estadisticas que el usuario quiso
    else:
        print("Ingrese una opcion valida...")
