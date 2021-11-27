num = (input("Digite um número inteiro: "))
tam = len(num)
num = int(num)
aux = 0
aux_2 = 0
anterio = False

while tam != 1:
   aux = num % 10 
   num = num // 10
   aux_2 = num % 10
   if (aux == aux_2):
      anterio = True
   tam = tam -1 
   
if anterio == True:
   print("sim")
else:
   print("não")
