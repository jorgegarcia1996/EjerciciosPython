# Escribe un programa que diga si un número introducido por teclado es o no primo.
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad.

num = int(input("Número: "))
primo = True
for cont in range(2, num):
    if num % cont == 0:
        primo = False
        break
if primo:
    print("Es primo")
else:
    print("No es primo")
