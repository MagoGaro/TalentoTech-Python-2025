from colorama import Fore, Back, Style
from utilidades.utilidades_visuales import UtilidadesVisuales
from utilidades.validaciones import Validaciones

class VistaProductos:
    def __init__(self):
        self.utilidades_visuales = UtilidadesVisuales()
        self.validaciones = Validaciones()
    
    def mostrar_mensaje_bienvenida(self):
        self.utilidades_visuales.limpiar_pantalla()
        print("\n\n")
        print(Fore.WHITE + Back.BLUE + "Sistema de gestión de productos".center(50))
        print("\n\n")
    
    def mostrar_menu_principal(self):
        return input(
            "Menú:\n1- Agregar producto\n2- Mostrar productos\n"
            "3- Editar producto\n4- Buscar producto\n"
            "5- Stock producto\n"
            "6- Eliminar producto\n7- Salir\n"
            "Seleccione una opción: "
        )
    
    def mostrar_mensaje(self, mensaje, color=Fore.WHITE):
        print(color + mensaje + Style.RESET_ALL)
    
    def pausar(self):
        input(f"\nPresione {Fore.BLUE}'enter'{Style.RESET_ALL} para continuar.")
        self.utilidades_visuales.limpiar_pantalla()
    
    def obtener_datos_producto(self):
        self.utilidades_visuales.limpiar_pantalla()
        nombre = self.validaciones.validar_nombre("Ingrese nombre del producto: ")
        categoria = self.validaciones.validar_categoria("Ingrese categoría del producto: ")
        precio = self.validaciones.validar_precio("Ingrese precio del producto: ")
        cantidad = self.validaciones.validar_precio("Ingrese cantidad del producto: ")
        
        return {
            'nombre': nombre.lower(),
            'categoria': categoria.lower(),
            'precio': precio,
            'cantidad': cantidad
        }
    
    def obtener_termino_busqueda(self, mensaje):
        return input(mensaje).strip()
    
    def obtener_datos_edicion(self):
        nombre = input("Ingrese nuevo nombre del producto (dejar vacío para no cambiar): ").strip()
        categoria = input("Ingrese nueva categoría del producto (dejar vacío para no cambiar): ").strip()
        precio = input("Ingrese nuevo precio del producto (dejar vacío para no cambiar): ").strip()
        cantidad = input("Ingrese la nueva cantidad del producto (dejar vacío para no cambiar): ").strip()
        
        datos = {}
        if nombre:
            datos['nombre'] = nombre.lower()
        if categoria:
            datos['categoria'] = categoria.lower()
        if precio:
            datos['precio'] = int(precio)
        if cantidad:
            datos['cantidad'] = int(cantidad)
        
        return datos
    
    def obtener_id_eliminar(self):
        while True:
            id_input = input("Ingrese el ID del producto a eliminar: ").strip()
            if id_input.isdigit():
                return id_input
            print(f"{Fore.RED}ID inválido. Debe ser un número.{Style.RESET_ALL}")
    
    def confirmar_eliminacion(self, producto):
        print(f"\nProducto encontrado:")
        self.mostrar_lista_productos([producto])
        
        while True:
            confirmacion = input("\n¿Está seguro que desea eliminar este producto? (s/n): ").lower().strip()
            if confirmacion == 's':
                return True
            elif confirmacion == 'n':
                return False
            print(f"{Fore.RED}Opción inválida. Ingrese 's' o 'n'.{Style.RESET_ALL}")
    
    def mostrar_lista_productos(self, productos, accion='listar', termino_busqueda=''):
        self.utilidades_visuales.limpiar_pantalla()
        
        if not productos:
            mensaje = "No hay productos disponibles." if accion == 'listar' else f"No hay coincidencias para '{termino_busqueda}'"
            print(f"\n\n{Fore.YELLOW}{mensaje}\n\n")
            return
        
        if accion == 'buscar':
            print(f"\n\nResultados de búsqueda para {Fore.YELLOW}'{termino_busqueda}':")
        
        encabezados = productos[0].keys()
        print('|'.join((encabezado.capitalize()).center(15) for encabezado in encabezados))
        print('-' * 80)

        for producto in productos:
            fila = [str(producto[clave]) for clave in encabezados]
            print('|'.join((str(dato).capitalize()).center(15) for dato in fila))