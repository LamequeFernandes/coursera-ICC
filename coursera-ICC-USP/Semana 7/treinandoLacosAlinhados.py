while True:
   numFat = int(input("Digite o número que deseja obter fatorial: "))
   fatorial = 1
   i = 1
   while i <= numFat:
      fatorial = fatorial * i
      i+=1
   print(fatorial)