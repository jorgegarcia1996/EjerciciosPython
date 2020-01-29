# Pedir un número por teclado y mostrar la tabla de multiplicar
numero = int(input("Numero: "))

for i in range(0, 11):
  print("%d * %d = %d" % (numero, i, numero * i))