def calcular_monto(precio = 0, cantidad = 0):
    return precio * cantidad

precio = float(input("Ingrese el precio del producto : "))
cantidad = int(input("ingrese la  cantidad de producto : "))

resultado = calcular_monto(precio, cantidad)
print(f"El monto totaal a pagar es : {resultado}")