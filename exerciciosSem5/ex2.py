def maior_primo(x):
   primo = 0
   while x != 0:
      if x == 2 or x == 3 or x == 5 or x == 7:
         return x
      if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
         primo = x
         return primo      
      x -= 1 

print(maior_primo(100))
