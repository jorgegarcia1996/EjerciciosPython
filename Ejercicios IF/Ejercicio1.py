# Realiza un programa que pida dos números ‘a’ y ‘b’ e indique si su suma es positiva, negativa o cero.
a = float(input("Dime un número: "))
b = float(input("Dime otro número: "))

if (a + b) < 0:
  print("La suma es negativa: %d" % (a + b))
elif (a + b) > 0:
  print("La suma es positiva: %d" % (a + b))
else:
  print("La suma es %d" % (a + b))