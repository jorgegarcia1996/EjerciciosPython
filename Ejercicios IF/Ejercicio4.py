# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” 
# se indica “Has entrado al sistema”, sino se da un error.
user = str(input("Usuario: "))
password = str(input("Contraseña:"))

if user == "pepe" and password =="asdasd":
  print("Has entrado al sistema")
else:
  print("Usuario o contraseña incorrectos")