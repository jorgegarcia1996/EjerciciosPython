
print("Calcular área y perímetro de un RECTÁNGULO \n")
base = float(input("Dime la base: "))
altura = float(input("Dime la altura: "))
perimetro = 2*base + 2*altura
area = base * altura
print("Resultado: Area=%.2f Perimetro=%.2f\n" % (area, perimetro))


print("Calcular área y perímetro de un TRIÁNGULO\n")
base = float(input("Dime la base: "))
lado1 = float(input("Dime el lado 1: "))
lado2 = float(input("Dime el lado 2: "))
altura = float(input("Dime la altura: "))
perimetro = base + lado1 + lado2
area = (base * altura) / 2
print("Resultado: Area=%.2f Perimetro=%.2f\n" % (area, perimetro))
