# Suponga un diccionario que contiene como clave el nombre de una persona 
# y como valor una lista con todas sus “gustos”. 
# Desarrolle un programa que agregue “gustos” a la persona:
# Si la persona no existe la agregue al diccionario con una lista que contiene un solo elemento.
# Si la persona existe y el gusto existe en su lista, no tiene ningún efecto.
# Si la persona existe y el gusto no existe en su lista, agrega el gusto a la lista.

gustos={}
nombre = input("Nombre:")

while nombre!="*":
  gusto=input("Gusto:")
  lista_gustos=gustos.setdefault(nombre,gusto)
  if lista_gustos!=gusto:
    gustos[nombre].append(gusto)
  nombre = input("Nombre:")

print(gustos)