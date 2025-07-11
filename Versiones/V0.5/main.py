import funcionalidad.funciones as f
import os
from colorama import Fore, Back, Style, init

if os.name == 'nt':
        init(autoreset=True)


productos = f.cargar_productos()

print("\n\n")
print(Fore.WHITE+Back.BLUE+"Sistema de gestión de productos".center(50))
print("\n\n")

while True:
    menu =input("Menu:\n1- Agregar producto\n2- Mostrar productos\n3- Editar producto\n4- Buscar producto\n5- Eliminar producto\n6- Salir\nSeleccione una opción: ")

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
                                f.guardar_productos(productos)
                                print(f"{Fore.LIGHTGREEN_EX}Producto {nombre.capitalize()} agregado exitosamente.")
                                input(f"Presione {Fore.BLUE}'enter'{Style.RESET_ALL} para continuar.")
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
        print("\n")
        input(f"Presione {Fore.BLUE}'enter'{Style.RESET_ALL} para continuar.")
        f.limpiar()
    
    elif menu == '3':
        
        while True:
            buscar = input("Ingrese nombre o ID del producto: ")
            if buscar.strip().isdigit() or buscar.strip():
                retorno = f.editar_producto(productos,buscar)
            else:
                print(f"\n{Fore.BLUE}El valor ingresado es incorrecto, intente de nuevo.{Style.RESET_ALL}")
            
            if retorno:
                break
            else:
                input(f"\n{Fore.RED}Ocurrio un error al actualizar el producto {buscar} presione 'enter' para vovler al menu.{Style.RESET_ALL}")
                break
        print("\n")
        input(f"Presione {Fore.BLUE}'enter'{Style.RESET_ALL} para continuar.")
        f.limpiar()

    elif menu == '4':
        buscar = input("Ingrese nombre completo o parcial del producto a buscar: ") 
        
        f.listar(productos,'buscar',buscar)
        print("\n")
        input(f"Presione {Fore.BLUE}'enter'{Style.RESET_ALL} para continuar.")
        f.limpiar()
    
    elif menu == '5':
        id_borrar = input("Ingrese el ID del producto que desa borrar: ")

        f.borrar(productos,id_borrar)
        f.guardar_productos(productos)

    elif menu == '6':
        print(f"{Fore.MAGENTA}Saliendo del sistema...")
        break
    else:
        print(f"{Fore.LIGHTRED_EX}Opción invalida, ingrese una opción correcta")