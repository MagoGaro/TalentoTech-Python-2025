from utilidades.gestor_archivos import GestorArchivos

class ModeloProductos:
    def __init__(self):
        self.gestor_archivos = GestorArchivos()
        self.productos = []
    
    def cargar_productos(self):
        self.productos = self.gestor_archivos.cargar_productos()
    
    def crear_producto(self, datos_producto):
        nuevo_id = self.gestor_archivos.obtener_siguiente_id()
        return {
            'id': nuevo_id,
            'nombre': datos_producto['nombre'],
            'categoria': datos_producto['categoria'],
            'precio': datos_producto['precio'],
            'cantidad': datos_producto['cantidad']
        }
    
    def obtener_todos_productos(self):
        return self.productos
    
    def buscar_producto(self, termino_busqueda):
        if str(termino_busqueda).isdigit():
            return [p for p in self.productos if termino_busqueda == str(p['id'])]
        return [p for p in self.productos if termino_busqueda.lower() in p['nombre'].lower()]
    
    def actualizar_producto(self, producto_existente, nuevos_datos):
        producto_existente['nombre'] = nuevos_datos.get('nombre', producto_existente['nombre'])
        producto_existente['categoria'] = nuevos_datos.get('categoria', producto_existente['categoria'])
        producto_existente['precio'] = nuevos_datos.get('precio', producto_existente['precio'])
        producto_existente['cantidad'] = nuevos_datos.get('cantidad', producto_existente['cantidad'])

    def eliminar_producto(self, productos_a_eliminar):
        for producto in productos_a_eliminar:
            if producto in self.productos:
                self.productos.remove(producto)

    def filtrar_por_stock(self, valor_minimo=None):
        if valor_minimo is None:
            return sorted(self.productos, key=lambda x: x['cantidad'], reverse=True)
        
        productos_filtrados = [p for p in self.productos if p['cantidad'] <= valor_minimo]
        return sorted(productos_filtrados, key=lambda x: x['cantidad'], reverse=True)
