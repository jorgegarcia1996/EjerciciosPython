# Crear un programa que lea por teclado una cadena y un carácter, 
# e inserte el carácter entre cada letra de la cadena.

cadena=input("Escribe una cadena: ")
caracter=input("Dime un carácter: ")

print(caracter.join(cadena))