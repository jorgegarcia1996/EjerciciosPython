# Escribir dos funciones que permitan calcular:
# - La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
# - La cantidad de horas, minutos y segundos de un tiempo dado en segundos.

def timeToSec(hours, minutes, seconds):
  return 3600 * hours + 60 * minutes + seconds

def secToTime(seconds): 
  minutes = seconds // 60
  seconds -= minutes*60
  hours = seconds // 3600
  seconds -= hours*3600
  return hours,minutes,seconds

print(timeToSec(12, 23, 12))
print(secToTime(601))