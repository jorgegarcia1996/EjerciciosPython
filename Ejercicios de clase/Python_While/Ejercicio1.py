# Escribe un programa para jugar a adivinar un número 
# (el ordenador "piensa" el número y el usuario tiene que adivinarlo). 
# El programa empieza pidiendo entre qué números está el número a adivinar, 
# se "inventa" un número al azar y después el usuario va probando valores y 
# el programa va diciendo si son demasiado grandes o pequeños.

# Nota: Para generar el número a adivinar utiliza la función randrange(mínimo, máximo, paso) 
# del módulo random. Para poder utilizar la función randrange tendrás que incluir en el 
# programa la instrucción siguiente: from random import randrange

from random import randrange

intentos = 1
minimo = int(input("Valor mínimo: "))
maximo = int(input("Valor máximo: "))

secreto = randrange(minimo, maximo + 1)

num=int(input("Escribe un número:"))
while num!=secreto:
    if num>secreto:
        num=int(input("!Demasiado grande¡ Intentalo otra vez: "))
    else:
        num=int(input("!Demasiado pequeño¡ Intentalo otra vez: "))
    intentos += 1
print ("Has acertado al %d intento" % intentos)
