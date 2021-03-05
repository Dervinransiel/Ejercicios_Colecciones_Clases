# Crear una lista. La lista tiene que tener 3 elementos. 
# Cada elemento debe ser una lista de 5 enteros. Calcular y 
# mostrar la suma de cada lista contenida en la lista principal.

lista_1 = [10,50,30,60,100]
lista_2 = [20,40,50,60,200]
lista_3 = [400,600,1000,100,700]

def sumar (lista_1):
    suma = 0
    for numero in lista_1:
         suma += numero
    return suma

print(sumar(lista_1))


