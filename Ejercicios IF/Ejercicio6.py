# Programa que lea un carácter por teclado y compruebe si es una letra mayúscula.
letra = str(input("Letra: "))

if letra.isupper():
  print("Mayúscula")
else:
  print("Minúscula")