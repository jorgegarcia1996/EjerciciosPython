# Crear un programa que lea por teclado una cadena y un carácter, 
# y reemplace todos los dígitos en la cadena por el carácter.

cadena=input("Escribe una cadena con números: ")
caracter=input("Dime un carácter: ")

for i in range(10):
  cadena = cadena.replace(str(i), caracter)

print(cadena)