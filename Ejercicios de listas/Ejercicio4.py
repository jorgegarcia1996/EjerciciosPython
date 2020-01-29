# Dado una lista, hacer un programa que indique si está ordenada o no.

lista = [1,2,3,4,5,2]

listaOrdenada = lista[:]
listaOrdenada.sort()

if lista == listaOrdenada:
  print("La lista está ordenada")
else:
  print("La lista no está ordenada")
