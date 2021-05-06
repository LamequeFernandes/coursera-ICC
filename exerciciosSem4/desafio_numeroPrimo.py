n = int(input("Digite um número inteiro: "))

if n % 2 == 0:
   print("não primo")
elif n == 5:
   print("primo")
elif n % 10 == 0 or n % 10 == 5:
   print("não primo")
elif n % 7 == 0:
   print("não primo")
elif n % 11 == 0:
   print("não primo")
else:
   print("primo")