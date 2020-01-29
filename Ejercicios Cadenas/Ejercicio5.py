# Escribir un programa python que dado una palabra diga si es un palíndromo. 
# Un palídromo Un palíndromo es una palabra, número o frase que se lee igual 
# hacia adelante que hacia atrás.

cadena = input("Dime una cadena: ")

if cadena.lower() == cadena[::-1].lower():
  print("La cadena '%s' es un palíndromo" % cadena)
else:
  print("La cadena '%s' no es un palíndromo" % cadena)
