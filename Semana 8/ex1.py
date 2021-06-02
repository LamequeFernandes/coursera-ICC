''' 
treinando

lista = [2, 4, 2, 2, 3, 3, 1]
l = sorted(lista)

lista.sort()

print(lista)
print(l)
'''

def remove_repetidos(lista):
   lista2 = []
   for i in lista:
      if i not in lista2:
         lista2.append(i)
   lista2.sort()
   return lista2

lista = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 2, 10 ,9]

lista = remove_repetidos(lista)
print (lista)