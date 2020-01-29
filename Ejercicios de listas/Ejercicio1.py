# Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo. 
# Muestra el máximo de los números guardado en la lista, muestra los números pares.
numero = int(input("Numero:"))
lista = []
while numero > 0:
  numero = int(input("Numero:"))
  lista.append(numero)

print("El máximo es: %d" % max(lista))

for n in lista:
  if (n % 2) == 0:
    print(n, end=" ")
print()

# List comprehension
for n in [x for x in lista if x % 2 == 0]:
  print(n)