lis = []
num = 1

while num != 0:
   num = int(input("Digite uma sequencia de numeros inteiros terminados por ZERO: "))
   if num != 0:
      lis.append(num)

i = len(lis) - 1

while i >= 0:
   print(lis[i], end=" ")
   i -= 1