# Escribe un programa que lea una cadena y devuelva un diccionario 
# con la cantidad de apariciones de cada palabra en la cadena.

cad = input("Dime nua cadena: ")

lista = cad.split(" ")

cadDict = {}
for c in lista:
  if c in cadDict:
    cadDict[c] += 1
  else:
    cadDict[c] = 1

for k,v in cadDict.items():
  print(k, "->", v)