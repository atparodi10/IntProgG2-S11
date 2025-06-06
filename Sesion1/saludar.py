# Ejemplo de saludar

def saludar(nombre):
    print(f"Hola {nombre.title()}, bienvenido")


def main():
    
    print("Ingrese su nombre")
    
    while True:
        nombre = input(">>> ").strip()
        
        if not nombre:
            print("Campo vacío.")
        
        elif not nombre.replace(" ", "").isalpha():
            print("ERROR. Datos no validos.")
        
        else:
            break
        
    saludar(nombre)

main()