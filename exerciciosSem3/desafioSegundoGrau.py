import math

a = int(input("digite o valor de a: "))
b = int(input("digite o valor de b: "))
c = int(input("digite o valor de c: "))


delta = b ** 2 - 4*a*c


if delta < 0:
  print("Esta equação não possui raizes reais")
elif delta == 0:
  delta = math.sqrt(delta)
  x1 = (-b + delta) / (2*a)
  print("A unica raiz é:", x1)
else:
  print("Primeira raiz:", x1," Segunda raiz:", x2)
  delta = math.sqrt(delta)
  x1 = (-b + delta) / (2*a)
  x2 = (-b - delta) / (2*a)
