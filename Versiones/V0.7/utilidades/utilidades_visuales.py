import os
from colorama import Fore, Style

class UtilidadesVisuales:
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_mensaje(self, mensaje, color=Fore.WHITE):
        print(color + mensaje + Style.RESET_ALL)