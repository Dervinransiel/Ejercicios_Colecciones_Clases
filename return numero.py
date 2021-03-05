#Crear una función que le enviemos como parámetros dos enteros y nos retorne el mayor.

mayor = None

for i in range(2):
    n = int(input("Ingrese un numero:"))
    if mayor is None or n > mayor:
        mayor = n
print("El numero mayor es:", mayor)