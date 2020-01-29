# Dada una lista de palabras, pide una cadenena por teclado e indica si está en la lista,
# indica cuantas veces aparece en la lista, lee otra palabra y sustituye la primera por la segunda en la lista,
# y por último borra la palabra de la lista.

lista = ['Di', 'buen', 'dia', 'a', 'papa', "hola", "papa", "buen", "dia"]

palabra = input("Palabra:")
if palabra in lista:
  print("La palabra está en la lista")
  print(lista.count(palabra))
  palabra2 = input("palabra a reemplazar:")
  apariciones = lista.count(palabra)
  pos = 0
  for i in range(0, apariciones):
    pos = lista.index(palabra, pos)
    lista[pos] = palabra2
  print(lista)

else:
    print("La palabra no está en la lista")
