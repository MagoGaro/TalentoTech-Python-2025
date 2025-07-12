from colorama import Fore, Style

class Validaciones:
    def validar_nombre(self, mensaje):
        while True:
            nombre = input(mensaje).strip()
            if nombre and nombre.replace(" ", "").isalpha():
                return nombre
            print(f"{Fore.RED}Nombre inválido. Solo se permiten letras y espacios.{Style.RESET_ALL}")
    
    def validar_categoria(self, mensaje):
        while True:
            categoria = input(mensaje).strip()
            if categoria and categoria.replace(" ", "").isalpha():
                return categoria
            print(f"{Fore.RED}Categoría inválida. Solo se permiten letras y espacios.{Style.RESET_ALL}")
    
    def validar_precio(self, mensaje):
        while True:
            precio = input(mensaje).strip()
            if precio and precio.isdigit():
                return int(precio)
            print(f"{Fore.RED}Precio inválido. Solo se permiten números enteros.{Style.RESET_ALL}")