def ehPrimo(n):
   fator = 2
   if n == 2:
      return True
   while n % fator != 0 and fator <= n:
      fator += 1
      if fator == n:
         return True
   return False     

def n_primos(x):
   i = 0
   qtsPrimos = 0
   while i <= x:   
      if ehPrimo(i) == True:
         qtsPrimos += 1
      i += 1
   return qtsPrimos

print(n_primos(121))






