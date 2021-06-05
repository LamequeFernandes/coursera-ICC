def minima(temps):
   min = temps[0]
   i = 1
   while i < len(temps):
      if temps[i] < min:
         min = temps[i]
      i = i +1
   return min

def maxima(temps):
   max = temps[0]
   i = 1
   while i < len(temps):
      if temps[i] > max:
         max = temps[i]
      i = i +1
   return max

def minMax(temperaturas):
   print("A menor temperatura do mês foi: ", minima(temperaturas), "C.")
   print("A maior temperatura do mês foi: ", maxima(temperaturas), "C.")

def teste_pontual(temp, valor_esperado):
   valor_calculado = minima(temp)
   if valor_calculado != valor_esperado:
      print("Valor errado para array ", temp)
      print("Valor esperado: ", valor_esperado, ". Valor calculado: ", valor_calculado)

def testa_minima():
   print("Iniciando os testes")
   teste_pontual([0], 0)
   teste_pontual([0, 0, 0, 0, 0], 0)
   teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
   teste_pontual([30, 21, 22, 33, 44, 25, 36, 27, 18, 11, 10], 10)
   teste_pontual([0, 12, 20, 3, 20, -15], -15)
   print("Finalizando os testes")

temps = [30, 21, 22, 33, 44, 25, 36, 27, 18, 11, 10]
minMax(temps)