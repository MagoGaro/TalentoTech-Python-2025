import os

def limpiar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def gestionar_id(accion = 'obtener',archivo= os.path.join(os.path.dirname(__file__), 'archivos', 'id.txt')):
    try:
        if accion == 'obtener':
            try:
                with open(archivo, 'r') as f:
                    return int(f.read().strip())
            except (FileNotFoundError, ValueError):
                with open(archivo, 'w') as f:
                    f.write('0')
                return 0
        elif accion == 'incrementar':
            ultimo_id = gestionar_id('obtener')
            nuevo_id = ultimo_id + 1
            with open(archivo, 'w') as f:
                f.write(str(nuevo_id))
            return nuevo_id
    except Exception as e:
        print(f"Error gestionando ID: {e}")
        return 0


def listar(lista, accion='listar' , busqueda = ''):
    if not lista:
        print("\n\nNo hay productos disponibles.\n\n" if accion == 'listar' else 
              f"\n\nNo hay coincidencias para '{busqueda}'.\n\n")
        input("Presione 'enter' para continuar.")
        limpiar()
        return
    
    if accion == 'listar':
        cabecera = lista[0].keys()

        print('|'.join((encabezado.capitalize()).center(15) for encabezado in cabecera))
        print('-' * 65)

        for producto in lista:
            fila = [str(producto[clave]) for clave in cabecera]
            print('|'.join((str(dato).capitalize()).center(15) for dato in fila))
            
    elif accion == 'buscar':
        resultados = [producto for producto in lista 
                     if busqueda.lower() in producto['nombre'].lower()]
        
        if not resultados:
            print(f"\n\nNo hay coincidencias para '{busqueda}'.\n\n")
            input("Presione 'enter' para continuar.")
            limpiar()
            return
        
        cabecera = resultados[0].keys()
        
        print(f"\n\nResultados de búsqueda para '{busqueda}':")
        print('|'.join((encabezado.capitalize()).center(15) for encabezado in cabecera))
        print('-' * 65)

        for producto in resultados:
            fila = [str(producto[clave]) for clave in cabecera]
            print('|'.join((str(dato).capitalize()).center(15) for dato in fila))


def borrar(lista,id):
    producto_a_borrar = None
    for producto in lista:
        if producto['id'] == id:
            producto_a_borrar = producto
            break
    
    if producto_a_borrar is None:
        print(f"\n\nNo se encontró ningún producto con ID {id}.\n\n")
        input("Presione 'enter' para continuar.")
        limpiar()
        return
    
    print("\n\nProducto encontrado:")
    cabecera = producto_a_borrar.keys()
    print('|'.join((encabezado.capitalize()).center(15) for encabezado in cabecera))
    print('-' * 65)
    fila = [str(producto_a_borrar[clave]) for clave in cabecera]
    print('|'.join((str(dato).capitalize()).center(15) for dato in fila))
    
    while True:
        confirmacion = input("\n¿Está seguro que desea borrar este producto? (s/n): ").lower().strip()
        
        if confirmacion == 's':
            lista.remove(producto_a_borrar)
            print(f"\nProducto con ID {id} borrado exitosamente.\n\n")
            break
        elif confirmacion == 'n':
            print("\nOperación cancelada. El producto no fue borrado.\n\n")
            break
        else:
            print("\nOpción invalida.\n\n")
        
    input("Presione 'enter' para continuar.")
    limpiar()

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
                                    'id': gestionar_id('incrementar'),
                                    'nombre':nombre.lower(),
                                    'categoria':categoria.lower(),
                                    'precio': int(precio)
                                }
                                productos.append(nuevo_producto)
                                print(f"Producto {nombre.capitalize()} agregado exitosamente.")
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
        listar(productos,'listar')
        input("\nPresione 'enter' para continuar.")
        limpiar()

    elif menu == '3':
        buscar = input("Ingrese nombre completo o parcial del producto a buscar: ") 
        
        listar(productos,'buscar',buscar)
        input("\nPresione 'enter' para continuar.")
        limpiar()
        
    elif menu == '4':
        id_borrar = input("Ingrese el ID del producto que desa borrar: ")

        borrar(productos,id_borrar)

    elif menu == '5':
        print("Saliendo del sistema...")
        break
    else:
        print("Opción invalida, ingrese una opción correcta")
