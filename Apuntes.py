# # IF
# numero = int(input("Numero: "))
# if numero < 0:
#   print("Número es negativo")
# elif numero > 0:
#   print("Número es positivo")
# else:
#   print("Número es 0")

# # WHILE
# año = 2001
# while año <= 2017:
#     print ("Informes del Año", año)
#     año += 1
# else:
#     print ("Hemos terminado")

# #FOR
# for i in range(1,10):
#     print (i)
# else:
#     print ("Hemos terminado")

# # zip()
# lista = list(zip(range(1,4),["ana","juan","pepe"]))
# print(lista)

# for x,y in zip(range(1,4),["ana","juan","pepe"]):
#   print(x, y)

# # map()
# lista = [1, 2, 3, 4, 5]
# print(lista)
# def sqr(x):
#     return x**2

# cuadrados = list(map(sqr, lista))
# print(cuadrados)

# # filter()
# lista = [1, 2, 3, 4, 5]
# print(lista)
# def odd(x):
#     return x % 2 == 0

# pares = list(filter(odd, lista))
# print(pares)

# # reduce()
# from functools import reduce
# lista = [1,2,3,4,5,6,7,8]
# print(lista)
# def add(x,y): return x + y
# red = reduce(add, lista)
# print(red)

# # list comprehension
# lista1 = [x ** 3 for x in [1,2,3,4,5]]
# lista2 = [x for x in range(10) if x % 2 == 0]
# lista3 = [x + y for x in [1,2,3] for y in [4,5,6]]

# print(lista1)
# print(lista2)
# print(lista3)

# # Tuplas
# tupla = 1,2,3
# a,b,c = tupla
# print(a,b,c)

# # Rangos
# lista = list(range(10))
# print(lista)
# lista = list(range(1, 11))
# print(lista)
# lista = list(range(0, 30, 5))
# print(lista)
# lista = list(range(0, 10, 3))
# print(lista)
# lista = list(range(0, -10, -1))
# print(lista)