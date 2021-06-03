def maior_elemento(lista):
   maior = lista[0]
   for i in lista:
      if i >= maior:
         maior = i
   return maior

lista = [10, 5, 7, 11, 8]
lista2 = [-99, -27, -12]
l = maior_elemento(lista2)
print(l)
