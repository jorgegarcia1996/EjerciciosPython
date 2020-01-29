# Crea una aplicación que pida un número y calcule su factorial 
# (El factorial de un número es el producto de todos los enteros 
# entre 1 y el propio número y se representa por el número seguido 
# de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120

import math
numero = int(input("Numero: "))
fact = math.factorial

# for i in range(1, numero + 1):
#   fact *= i

print("El factorial es %d" % fact)
