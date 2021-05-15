def fatorial(x):
   fat = 1
   while x >= 1:
      fat = fat * x 
      x -= 1
   return fat

print("Sabendo que n >= p")

n = int(input("Digite o seu n: "))
p = int(input("Digite o seu p: "))

if n>=p:
   n_binomial = fatorial(n)/(fatorial(n-p)*fatorial(p))
   print("Resultado: ", n_binomial)
else:
   print("'n' deve ser maior que 'p'")
