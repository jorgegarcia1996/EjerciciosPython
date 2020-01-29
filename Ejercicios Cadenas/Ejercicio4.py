# Escribir funciones que dadas dos cadenas de caracteres:

cad1 = input("Dime una cadena: ")
cad2 = input("Dime otra cadena: ")

# Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, cadena es una subcadena de subcadena.
if cad1.find(cad2)>-1:
  print ("cad2 es subcadena de cad1")
else:
  print ("cad2 no es subcadena de cad1")            


# Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe kde y gnome debe devolver gnome.
print(cad1 if cad1<cad2 else cad2)


