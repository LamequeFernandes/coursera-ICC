def maior_elemento(lista):
   aux = 0
   maior = 0
   for i in lista:
      if i >= aux:
         maior = i
      aux = i
   return maior

lista = [10, 5, 7, 11, 8]
l = maior_elemento(lista)
print(l)
