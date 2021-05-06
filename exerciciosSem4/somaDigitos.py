n = int(input("Digite um número inteiro: "))
resto = 0
soma = 0

while n != 0:
   resto = n % 10
   soma += resto
   n = n // 10

print(soma)