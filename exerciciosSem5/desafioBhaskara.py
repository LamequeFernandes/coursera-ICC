import math

def delta(a, b, c):
#   delta = math.sqrt(b**2 - 4*a*c)
   return math.sqrt(b**2 - 4*a*c)

a = int(input("Digite o 'a' do bhaskara: "))
b = int(input("Digite o 'b' do bhaskara: "))
c = int(input("Digite o 'c' do bhaskara: "))

x1 = (-b + delta(a,b,c))/ 2*a
x2 = (-b - delta(a,b,c))/ 2*a

print("Raizes: ", x1, x2)