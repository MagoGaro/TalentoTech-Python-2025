import os
import json

def limpiar():
    """
    Limpia la consola, independientemente del sistema en el que estemos
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def gestionar_id(accion = 'obtener',archivo= os.path.join(os.path.dirname(__file__), '../archivos', 'id.txt')):
    """
    Puede recibir dos parametros:
    Acción  -> Nos dira si obtenemos o incrementamos el ID
               Por defecto es Obtener
    Archivo -> Espera un archivo donde se guarda el ID
    """
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
    """
    Esepera un array

    Tambien puede recibir una accion y un parametro de busqueda
    """
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
    """
    Recibe una Lista y un ID
    Elimina el elemento con ese ID
    """
    producto_a_borrar = None
    for producto in lista:
        if producto['id'] == int(id):
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

def cargar_productos(archivo=os.path.join(os.path.dirname(__file__), '../archivos', 'productos.json')):
    """
    Recibe un archivo JSON y lo rertona
    """
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def guardar_productos(lista, archivo=os.path.join(os.path.dirname(__file__), '../archivos', 'productos.json')):
    """
    Recibe una lista y un archivo
    guarda la lista en el archivo
    """
    try:
        with open(archivo, 'w') as f:
            json.dump(lista, f, indent=4)
    except Exception as e:
        print(f"Error al guardar productos: {e}")