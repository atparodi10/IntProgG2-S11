"""Formula area de circulo = pi * (r*r)"""

import math 

def calcularArea(r):
    print(math.pi * r **2)

def main():
    
    print("""
          
        ----> Calcular Área de un circulo
        Ingrese radio de su circulo
              
          """)
    
    while True:
        radio = float(input(">>> "))
    
        if radio <= 0:
            print("Ingrese un radio valido.")

        else:
            break
    
    calcularArea(radio) 
    
main()   