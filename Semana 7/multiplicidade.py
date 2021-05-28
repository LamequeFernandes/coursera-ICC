
fator = 2
multiplicidade = 0
n=int(input("Numero q dejesa obter multiplicidade: "))
while n > 1:
   while n % fator == 0:
      multiplicidade = multiplicidade + 1
      n = n / fator
   if multiplicidade > 0:
      print(fator, "^", multiplicidade, "*" ,end=" ")
   fator = fator + 1
   multiplicidade = 0
print(1)