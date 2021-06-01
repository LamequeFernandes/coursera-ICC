def clone(lista):
   clone = []
   for objeto in lista:
      clone.append(objeto)
   return clone

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  
lista2 = clone(lista) #clonando lista
lista3 = lista2[:] #outra maneira de clonar

print(lista[1:3])
print(lista[1:7])
print()
print(lista)
lista2[-1] = 0
print(lista2)
lista3[-1] = 21
print(lista3)

if 20 in lista: # utilizase para verificar se tal elemento esta presente em uma determinada lista ou vetor
   print("o numero 20 pertence a lista 1")
else:
   print("o numero 20 n pertence a esta lista")

meninos = ["lameque", "levi", "juliel"]
meninas = ["roni" ,"aurora", "clemilda"]
boysAndGirls = meninos + meninas #concatena os arrays
print(boysAndGirls)

meninos_triplicado = meninos *3 #repetição de listas, vetores e arrays
print(meninos_triplicado)

del boysAndGirls[2]
print(boysAndGirls)
del boysAndGirls[0:3]
print(boysAndGirls)
