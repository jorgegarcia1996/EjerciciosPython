# Las torres de Hanoi. 
# El rompecabezas de las Torres de Hanoi fue inventado por el matemático francés Edouard Lucas en 1883. 
# Se inspiró en una leyenda acerca de un templo hindú donde el rompecabezas fue presentado a los jóvenes sacerdotes. 
# Al priniipio de los tiempos, a los sacerdotes se les dieron tres postes y una pila de 64 discos de oro, 
# cada disco un poco más pequeño que el de debajo. Su misión era transferir los 64 discos de uno de los tres postes a otro, 
# con dos limitaciones importantes. Sólo podían mover un disco a la vez, 
# y nunca podían colocar un disco más grande encima de uno más pequeño. 
# Los sacerdotes trabajaban muy eficientemente, día y noche, moviendo un disco cada segundo. 
# Cuando terminaran su trabajo, dice la leyenda, el templo se desmenuzaría en polvo y el mundo se desvanecería. 
# Realiza un programa utilizando listas que nos permita resolver el problema. 
# Comienza con un límite de discos (por ejemplo, 3) y ve aumentando para lograr una solución general.

piezas = int(input("¿Cuantas piezas hay? "))

while piezas < 3:
  piezas = int(input("El número de piezas debe ser al menos de 3:"))

inicial = list(range(1, piezas + 1))
central, final = [], []

def hanoi(n, ini, cen, fin):
  if n == 0:
    return
  hanoi(n-1, ini, fin, cen)

  if ini:
    fin.append(ini.pop())
    print("-----------------------------------------","\nInicial: ", inicial,"\nCentral: ", central,"\nFinal:   ", final)
  hanoi(n-1, cen, ini, fin)


print("\nInicial: ", inicial,"\nCentral: ", central,"\nFinal:   ", final)
hanoi(piezas, inicial, central, final)