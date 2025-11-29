'''
El sistema debe permitir ingresar datos básicos de los productos: nombre, categoría, y precio (sin centavos). 
Estos datos deben almacenarse en una lista, donde cada producto sea representado/a como una sublista de tres 
elementos (nombre, categoría, y precio).

Funciones: 
- Agregar productos

- Buscar productos por nombre. Si encuentra coincidencias, debe mostrar la información completa
de los productos que coincidan. Si no hay coincidencias, debe informar que no se encontraron resultados.

- Eliminación de productos: El sistema debe permitir eliminar un producto de la lista, identificándolo por 
su posición (número) en la lista.

- Visualizar productos

- Salir'''

productos = []

menu = """
Aplicación para gestión de productos
Opciones:
1 - Agregar producto
2 - Mostrar productos
3 - Buscar producto
4 - Eliminar producto
5 - Salir
"""

print(menu)
opcion = input("Elija la opción deseada: ")

while opcion != "5":
    match opcion:
        case "1":   
            print("Ingrese los datos del producto a agregar:")
            nombre = input("Nombre: ").strip().lower()
            if nombre == "":
                print("El nombre no puede estar vacío")
                continue
            categoria = input("Categoría: ").strip().lower()
            if categoria == "":
                print("La categoría no puede estar vacía")
                continue
            try:
                precio = int(input("Precio: "))
                if precio < 0:
                    print("El precio no puede ser un número negativo")
                    continue
            except ValueError:
                print("El precio debe ser un número")
                continue
            
            productos.append([nombre, categoria, precio])
            print("Producto agregado correctamente")

        case "2":
            print("Lista de productos:")
            for i in range(0, len(productos), 1):
                print(f"{i} - Producto: {productos[i][0].capitalize()} - Categoria: {productos[i][1].capitalize()} - Precio: ${productos[i][2]}")
        
        case "3":   
            print("Ingrese el nombre del producto a buscar:")
            nombre = input("Nombre: ").strip().lower()
            if nombre == "":
                print("El nombre no puede estar vacío")
                continue
            encontrado = False
            for i in range(0, len(productos), 1):
                if productos[i][0].lower() == nombre:
                    print(f"Producto encontrado: \n{productos[i][0].capitalize()} - Categoria: {productos[i][1].capitalize()} - Precio: ${productos[i][2]}")
                    encontrado = True
            if not encontrado:
                print("Producto no encontrado")
        
        case "4":
            print("Verifique la posición del producto a eliminar:")
            for i in range(0, len(productos), 1):
                print(f"Posición {i}: {productos[i][0].capitalize()}")
            try:
                posicion = int(input("Posición del producto a eliminar: "))
                if posicion < 0 or posicion >= len(productos):
                    print("Posición no válida")
                    continue
                productos.pop(posicion)
                print("Producto eliminado correctamente")
            except ValueError:
                print("Posición debe ser un número")
            
        
        case _:
            print("Opción no válida")

    print(menu)
    opcion = input("Elija la opción deseada: ")