# Un programa que almacene en una lista el número de días que tiene cada mes 
# (supondremos que es un año no bisiesto), pida al usuario que le indique un mes 
# (1=enero, 12=diciembre) y muestre en pantalla el número de días que tiene ese mes.

import calendar

y=int(input("introduce un año:\n"))

print("Ahora...")

m=int(input("introduce un mes:"))

print(calendar.month(y,m))

