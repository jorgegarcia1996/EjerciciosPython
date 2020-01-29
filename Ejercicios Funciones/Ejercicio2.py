# Realiza una función que dependiendo de los parámetros que reciba: convierte a segundos o a horas:
# - Si recibe un argumento, supone que son segundos y convierte a horas, mintos y segundos.
# - Si recibe 3 argumentos, supone que son hora, minutos y segundos y los convierte a segundos.

def timeConversor(*args):
  if len(args) == 3:
    return 3600 * args[0] + 60 * args[1] + args[2]
  elif len(args) == 1:
    seconds = args[0]
    minutes = seconds // 60
    seconds -= minutes*60
    hours = seconds // 3600
    seconds -= hours*3600
    return hours,minutes,seconds
  else:
    raise TypeError("Introduce 1 o 3 argumentos")

print(timeConversor(12, 23, 12))
print(timeConversor(601))
print(timeConversor(1234,423332))