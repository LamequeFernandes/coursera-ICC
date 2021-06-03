num = 1
lista = []
while num != 0:
   num = int(input("Digite um número: "))
   if num != 0:
      lista.append(num)

i = len(lista) - 1
while i >= 0:
   print(lista[i])
   i -= 1

