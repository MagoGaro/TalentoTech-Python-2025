import os
import json

class GestorArchivos:
    def __init__(self):
        self.directorio_datos = os.path.join(os.path.dirname(__file__), '../archivos')
        self.archivo_productos = os.path.join(self.directorio_datos, 'productos.json')
        self.archivo_id = os.path.join(self.directorio_datos, 'id.txt')
    
    def cargar_productos(self):
        try:
            with open(self.archivo_productos, 'r') as archivo:
                return json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def guardar_productos(self, productos):
        with open(self.archivo_productos, 'w') as archivo:
            json.dump(productos, archivo, indent=4)
    
    def obtener_siguiente_id(self):
        try:
            with open(self.archivo_id, 'r+') as archivo:
                id_actual = int(archivo.read().strip())
                nuevo_id = id_actual + 1
                archivo.seek(0)
                archivo.write(str(nuevo_id))
                return nuevo_id
        except (FileNotFoundError, ValueError):
            with open(self.archivo_id, 'w') as archivo:
                archivo.write('1')
            return 1