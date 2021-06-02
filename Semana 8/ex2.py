def soma_elementos(lista):
   soma = 0
   for i in lista:
      soma += i
   return soma

vet = [1, 2, 3, 4, 5]
somaa = soma_elementos(vet)
print(somaa)