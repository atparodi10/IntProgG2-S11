
# sumar dos numeros

def sumar(num1, num2):
    return num1 + num2

def main():
    
    print("""
          ---> Suma de dos números
          Ingrese los numeros para realizar la suma
          
          """)
    
    n1 = float(input(">>> "))
    n2 = float(input(">>> "))
    
    print(f"{sumar(n1, n2): .2f}")
    
main()