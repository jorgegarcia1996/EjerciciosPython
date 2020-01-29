# Realizar una función recursiva que reciba una lista y que calcule el producto de los elementos de la lista:

def producto(lista):
  if len(lista) == 1:
    return lista[0]
  else:
    return lista.pop() * producto(lista)

if __name__ == '__main__':
    print(producto([3,4,50]))