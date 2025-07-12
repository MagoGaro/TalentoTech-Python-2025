import sqlite3
from pathlib import Path

class GestorDB:
    def __init__(self):
        self.directorio_datos = Path(__file__).parent.parent / 'ddbb'
        self.directorio_datos.mkdir(exist_ok=True)
        self.db_path = self.directorio_datos / 'productos.db'
        self._crear_tablas()

    def _crear_tablas(self):
        with self._get_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    precio INTEGER NOT NULL,
                    cantidad INTEGER NOT NULL
                )
            ''')
    
    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def ejecutar_consulta(self, consulta, parametros=(), fetch=False, fetch_lastrowid=False):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(consulta, parametros)
            
            if fetch:
                return cursor.fetchall()
            if fetch_lastrowid:
                return cursor.lastrowid
            
            conn.commit()