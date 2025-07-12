from colorama import Fore
from modelos.modelo_productos import ModeloProductos
from vistas.vista_productos import VistaProductos
from utilidades.gestor_archivos import GestorArchivos

class ControladorProductos:
    def __init__(self):
        self.modelo = ModeloProductos()
        self.vista = VistaProductos()
        self.gestor_archivos = GestorArchivos()
    
    def iniciar_sistema(self):
        self.vista.mostrar_mensaje_bienvenida()
        self.modelo.cargar_productos()
        
        while True:
            opcion = self.vista.mostrar_menu_principal()
            
            if opcion == '1':
                self.agregar_producto()
            elif opcion == '2':
                self.mostrar_productos()
            elif opcion == '3':
                self.editar_producto()
            elif opcion == '4':
                self.buscar_producto()
            elif opcion == '5':
                self.stock_producto()
            elif opcion == '6':
                self.eliminar_producto()
            elif opcion == '7':
                self.vista.mostrar_mensaje("Saliendo del sistema...", color=Fore.MAGENTA)
                break
            else:
                self.vista.mostrar_mensaje("Opción inválida, ingrese una opción correcta", color=Fore.LIGHTRED_EX)

    def agregar_producto(self):
        datos_producto = self.vista.obtener_datos_producto()
        nuevo_producto = self.modelo.crear_producto(datos_producto)
        self.modelo.productos.append(nuevo_producto)
        self.gestor_archivos.guardar_productos(self.modelo.productos)
        self.vista.mostrar_mensaje(f"Producto {datos_producto['nombre'].capitalize()} agregado exitosamente.", color=Fore.LIGHTGREEN_EX)
        self.vista.pausar()

    def mostrar_productos(self):
        productos = self.modelo.obtener_todos_productos()
        self.vista.mostrar_lista_productos(productos, 'listar')
        self.vista.pausar()

    def editar_producto(self):
        termino_busqueda = self.vista.obtener_termino_busqueda("Ingrese nombre o ID del producto a editar: ")
        resultados = self.modelo.buscar_producto(termino_busqueda)

        if not resultados:
            self.vista.mostrar_mensaje("No se encontró el producto.", color=Fore.RED)
        elif len(resultados) > 1:
            self.vista.mostrar_lista_productos(resultados, 'buscar', termino_busqueda)
            self.vista.mostrar_mensaje("Se encontraron múltiples coincidencias. Sea más específico para editar.", color=Fore.YELLOW)
        else:
            producto = resultados[0]
            nuevos_datos = self.vista.obtener_datos_edicion()
            self.modelo.actualizar_producto(producto, nuevos_datos)
            self.gestor_archivos.guardar_productos(self.modelo.productos)
            self.vista.mostrar_mensaje("Producto actualizado correctamente.", color=Fore.LIGHTGREEN_EX)
        
        self.vista.pausar()

    def buscar_producto(self):
        termino_busqueda = self.vista.obtener_termino_busqueda("Ingrese nombre o ID del producto a buscar: ")
        resultados = self.modelo.buscar_producto(termino_busqueda)
        self.vista.mostrar_lista_productos(resultados, 'buscar', termino_busqueda)
        self.vista.pausar()

    def eliminar_producto(self):
            id_producto = self.vista.obtener_id_eliminar()
            productos = self.modelo.buscar_producto(id_producto)
            
            if productos:
                producto = productos[0]
                if self.vista.confirmar_eliminacion(producto):
                    self.modelo.eliminar_producto([producto])
                    self.gestor_archivos.guardar_productos(self.modelo.productos)
                    self.vista.mostrar_mensaje("Producto eliminado correctamente.", color=Fore.LIGHTGREEN_EX)
                else:
                    self.vista.mostrar_mensaje("Operación cancelada por el usuario.", color=Fore.YELLOW)
            else:
                self.vista.mostrar_mensaje("Producto no encontrado.", color=Fore.RED)

            self.vista.pausar()
    
    def stock_producto(self):
        valor_minimo = self.vista.obtener_valor_minimo_stock()
        productos_filtrados = self.modelo.filtrar_por_stock(valor_minimo)
        
        if valor_minimo is not None:
            mensaje = f"Productos con stock {Fore.CYAN}≤ {valor_minimo}{Style.RESET_ALL}, ordenados por stock:"
            self.vista.mostrar_mensaje(mensaje)
        
        self.vista.mostrar_lista_productos(productos_filtrados, 'stock')
        self.vista.pausar()