import funcionalidad.funciones as f

productos = []

print("\n\nSistema de gestion de productos\n\n".center(50))
while True:
    menu =input("Menu:\n1- Agregar producto\n2- Mostrar productos\n3- Buscar producto\n4- Eliminar producto\n5- salir\nSeleccione una opción: ")

    if menu == '1':
        while True:
            nombre = input("Ingrese nombre del producto: ")
            
            if nombre.strip() and nombre.isalpha():
                while True:
                    categoria = input("Ingrese categoria del producto: ")
                    if categoria.strip() and categoria.isalpha():
                        while True:
                            precio = input("Ingrese precio del producto: ")
                            if precio.strip() and precio.isdigit():
                                nuevo_producto = {
                                    'id': f.gestionar_id('incrementar'),
                                    'nombre':nombre.lower(),
                                    'categoria':categoria.lower(),
                                    'precio': int(precio)
                                }
                                productos.append(nuevo_producto)
                                print(f"Producto {nombre.capitalize()} agregado exitosamente.")
                                input("Presione 'enter' para continuar.")
                                f.limpiar()
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
        f.listar(productos,'listar')
        input("\nPresione 'enter' para continuar.")
        f.limpiar()

    elif menu == '3':
        buscar = input("Ingrese nombre completo o parcial del producto a buscar: ") 
        
        f.listar(productos,'buscar',buscar)
        input("\nPresione 'enter' para continuar.")
        f.limpiar()
        
    elif menu == '4':
        id_borrar = input("Ingrese el ID del producto que desa borrar: ")

        f.borrar(productos,id_borrar)

    elif menu == '5':
        print("Saliendo del sistema...")
        break
    else:
        print("Opción invalida, ingrese una opción correcta")