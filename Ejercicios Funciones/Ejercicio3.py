# Queremos hacer una función que añada a una lista los contactos de una agenda.
# Los contactos se van a guardar en un diccionario, y al menos debe tener el campo de nombre,
# el campo del teléfono, aunque puede tener más campos.
# Los datos se irán pidiendo por teclado, se pedirá de antemanos cuantos contactos se van a guardar.
# Si vamos a guardar más información en el contacto, se irán pidiendo introduciendo campos hasta que introduzcamos el “*”.


def guardar_agenda(l_agenda, **kwargs):
  l_agenda.append(kwargs)
  return l_agenda


def main():
  agenda = []
  cantidad = int(input("¿Cuántos contactos vas a introducir?"))
  for i in range(cantidad):
    contacto = {}
    contacto["nombre"] = input("Indica el nombre:")
    contacto["telefono"] = input("Indica el teléfono:")
    campo = input("Introuzca otro campo:")
    while campo != "*":
      contacto[campo] = input("Introuzca valor:")
      campo = input("Introuzca otro campo:")
    agenda = guardar_agenda(agenda, **contacto)
  print(agenda)


if __name__ == '__main__':
  main()
