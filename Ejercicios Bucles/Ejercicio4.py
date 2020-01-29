# Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5

for numero in range(1,6):
    for cont in range(1,11):
        print ("%2d * %d = %2d" % (cont, numero, cont * numero))
    print()