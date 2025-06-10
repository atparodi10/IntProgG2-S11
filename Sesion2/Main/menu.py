import Models.classes as c
import Dao.funciones as f

productos = f.ProdcutDao()

def menu():
    print("""
          -----> Selecciona lo que desea hacer:
          
          1) Agregar
          2) Mostrar
          6) Salir
          
          """)
    
def main():
    while True:
        menu()
        opcion = input(">>> ")
            
        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese las cantidades en existencias del prodcuto: "))
            producto = c.Prodcut(nombre, precio, stock)
            productos.add(producto)
        
        elif opcion == "2":
            print("Productos:")
            productos.show()

        elif opcion == "6":
            print("Saliendo del programa...")
            input("Presione enter para confirmar...")
            print("Adios")
            break
        
        else:
            print("Opcion no valida.")
                