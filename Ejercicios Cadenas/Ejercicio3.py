# Crea un programa python que lea una cadena de caracteres y muestre la siguiente información:

cadena = input("Dime una cadena: ")
lista = cadena.title().split(" ")

# La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
for palabra in lista:
  print(palabra[0], end="")
print()

# Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe república
# argentina debe devolver República Argentina.
print(cadena.title())

# Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.
for palabra in lista:
  if palabra.startswith("A"):
    print(palabra, end=",")
print()
