from controladores.controlador_productos import ControladorProductos
import os
from colorama import init

if __name__ == "__main__":
    if os.name == 'nt':
        init(autoreset=True)
    
    controlador = ControladorProductos()
    controlador.iniciar_sistema()