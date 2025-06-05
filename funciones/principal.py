import operaciones as operation

def limpiar():
    import os
    os.system ("cls")
    
def presionar():
    input("Presione enter para volver al menu...")

def menu():
     print("1. Sumar \n2. Restar \n3. Multiplicar \n4. Dividir \n5. Salir \n6. Resuelve (x+2y)/z ")



    
def main():
    while(True):
        limpiar()
        menu()
        op = input("Digite una opcion : ")

        if op == "1":
            operation.limpiar()
            num1 = int(input("Primer valor : "))
            num2 = int(input("Segundo valor :"))
            suma = operation.sumar(num1, num2)
            print(f"{num1} + {num2} = {suma}")
            presionar()

        elif op == "2":
            operation.limpiar()
            num1 = int(input("Primer valor :"))
            num2 = int(input("Segundo valor : "))
            resta = operation.restar(num1, num2)
            print(f"{num1} - {num2} = {resta} ")
            presionar()

        elif op == "3":
            operation.limpiar()
            num1 = int(input("Primer valor : "))
            num2 = int(input("Segundo valor : "))
            multi = operation.multiplicar(num1, num2)
            print (f"{num1} * {num2} = {multi}")
            presionar()

        elif op == "4":
            operation.limpiar()
            num1 = int(input("Ingresa un valor : "))
            num2 =int(input("Ingresa otro valor : "))
            div = operation.dividir(num1, num2)
            print(f"{num1} / {num2} = {div}")
            presionar()

        elif op == "5":
            False
            break
        elif op == "6":
            x = int(input("Valor de X "))
            y = int(input("Valor de Y "))
            z = int(input("Valor de Z "))
            multi = operation.multiplicar(2, y)
            suma =operation.sumar(x, multi)
            div = operation.dividir(suma, z)
            print(div)
            operation.presionar()

        else:
            limpiar()
            print("Opcion no valida")
            presionar()
        
if __name__ == "__main__":   
    main()