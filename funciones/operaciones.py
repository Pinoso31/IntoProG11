def sumar (num1 = 0, num2 = 0):
    return num1 + num2

def restar (num1 = 0, num2 = 0):
    return num1 - num2

def multiplicar (num1 = 0, num2 = 0):
    return num1 * num2

def dividir (num1 = 0, num2 = 0):
    if num2 == 0:
        return " no se puede dividir por 0"
    return num1 / num2    


def limpiar():
    import os
    os.system ("cls")

def presionar():
    input("Presione enter para volver al menu...")

