import math

a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))

delta = b ** 2 - 4*a*c

if delta < 0:
  print("esta equação não possui raízes reais")
elif delta == 0:
  delta = math.sqrt(delta)
  x1 = (-b + delta) / (2*a)
  print("a raiz desta equação é", x1)
else:
  delta = math.sqrt(delta)
  x1 = (-b + delta) / (2*a)
  x2 = (-b - delta) / (2*a)
  if x1 > x2:    
    print("as raízes da equação são", x2,"e", x1)
  else:
    print("as raízes da equação são", x1,"e", x2)
