# Escribe un programa que tome como entrada el radio y retorne el área de un círculo. 
# El área de un círculo es igual a su radio al cuadrado multiplicado por ´pi´.

import math

radio = float(input("Dime el radio del círculo: "))

area = math.pi * (radio**2)

print("El área del círculo es de %.2f" % area)