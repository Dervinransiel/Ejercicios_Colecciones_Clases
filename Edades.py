# Crear una función que reciba una serie de edades y
# me retorne la cantidad que son mayores o iguales a 18

edades = [25,15,18]

iguales = None
mayor = None
for numero in edades:
    if mayor==None and iguales==None:
       mayor = numero
       iguales = numero
      
    else:
        if numero > mayor:
            mayor = numero
        if numero > iguales:
            iguales = numero


print(f"el numero mayor es: {mayor}")
print(f"el numero igual es: {iguales}")