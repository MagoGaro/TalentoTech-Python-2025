from utilidades.gestor_db import GestorDB

class ModeloProductos:
    def __init__(self):
        self.gestor_db = GestorDB()
       
    def crear_producto(self, datos_producto):
        consulta = '''
            INSERT INTO productos (nombre, categoria, precio, cantidad)
            VALUES (?, ?, ?, ?)
        '''
        nuevo_id = self.gestor_db.ejecutar_consulta(
            consulta,
            (
                datos_producto['nombre'],
                datos_producto['categoria'],
                datos_producto['precio'],
                datos_producto['cantidad']
            ),
            fetch_lastrowid=True
        )
    
        return {
            'id': nuevo_id,
            **datos_producto
        }
    
    def obtener_todos_productos(self):
        return self.gestor_db.ejecutar_consulta(
            'SELECT * FROM productos ORDER BY cantidad DESC',
            fetch=True
        )
    
    def buscar_producto(self, termino_busqueda):
        if str(termino_busqueda).isdigit():
            return self.gestor_db.ejecutar_consulta(
                'SELECT * FROM productos WHERE id = ?',
                (int(termino_busqueda),),
                fetch=True
            )
        return self.gestor_db.ejecutar_consulta(
            'SELECT * FROM productos WHERE nombre LIKE ?',
            (f'%{termino_busqueda}%',),
            fetch=True
        )
    
    def actualizar_producto(self, id_producto, nuevos_datos):
        campos = []
        parametros = []
        
        for campo, valor in nuevos_datos.items():
            campos.append(f"{campo} = ?")
            parametros.append(valor)
        
        parametros.append(id_producto)
        
        consulta = f'''
            UPDATE productos 
            SET {', '.join(campos)}
            WHERE id = ?
        '''
        self.gestor_db.ejecutar_consulta(consulta, parametros)
    
    def eliminar_producto(self, id_producto):
        self.gestor_db.ejecutar_consulta(
            'DELETE FROM productos WHERE id = ?',
            (id_producto,)
        )
    
    def filtrar_por_stock(self, valor_minimo=None):
        if valor_minimo is None:
            return self.obtener_todos_productos()
        
        return self.gestor_db.ejecutar_consulta(
            'SELECT * FROM productos WHERE cantidad <= ? ORDER BY cantidad DESC',
            (valor_minimo,),
            fetch=True
        )