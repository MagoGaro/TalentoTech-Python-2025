import os

def limpiar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def listar(opcion,lista,titulos,busqueda = ''):
    if len(lista) != 0:
            print('|'.join(titulo.center(13) for titulo in titulos))
            print(55*'-')
            for i, producto in enumerate(lista , start=1):
                indice = [str(i)] + [str(item) for item in producto]
                print('|'.join(str(item).center(13) for item in indice))
    else:
        if opcion == '2':
            print("\n\nNo hay productos disponibles.\n\n")
        elif opcion == '3':
            print(f"\n\nNo hay productos que coincidan con su busqueda '{busqueda}'.\n\n")

    input("Presione 'enter' para continuar.")
    limpiar()

productos = []
encabezado = ['ID','Producto','Categoria','Precio']

print("\n\nSistema de gestion de productos\n\n".center(50))
while True:
    menu =input("Menu:\n1- Agregar producto\n2- Mostrar productos\n3- Buscar producto\n4- Eliminar producto\n5- salir\nSeleccione una opción: ")

    if menu == '1':
        while True:
            nombre = input("Ingrese nombre del producto: ")
            
            if nombre != '' and nombre != ' ':
                while True:
                    categoria = input("Ingrese categoria del producto: ")
                    if categoria != '' and categoria != ' ':
                        while True:
                            precio = input("Ingrese precio del producto: ")
                            if precio != '' and precio != ' ' and precio.isdigit():
                                productos.append([nombre.capitalize(),categoria.capitalize(),int(precio)])
                                print("Producto agregado exitosamente.")
                                input("Presione 'enter' para continuar.")
                                limpiar()
                            else:
                                continue
                            break
                    else:
                        continue
                    break 
            else:
                continue
            break
        
    elif menu == '2':
        listar(menu,productos,encabezado)
        
    elif menu == '3':
        buscar = input("Ingrese nombre completo o parcial del producto a buscar: ") 
        
        resultado = [registro for registro in productos if buscar.capitalize() in str(registro[0])] 
        
        listar(menu,resultado,encabezado, buscar)

    elif menu == '4':
        while True:
            borrar = input("Ingrese el ID del producto que desa borrar: ")

            if borrar.isdigit():
                if int(borrar) <= len(productos):
                    eliminado = productos.pop(int(borrar)-1)
                    print(f"Se ha eliminado '{eliminado[0]}' exitosamente.")
                    input("Presione 'enter' para continuar.")
                    limpiar()
                    break
                else:
                    print(f"\n\nEl ID '{borrar}' no existe.\n\n")
            else:
                print("\n\nEl ID debe ser un numero entero.\n\n")

    elif menu == '5':
        print("Saliendo del sistema...")
        break
    else:
        print("Opción invalida, ingrese una opción correcta")