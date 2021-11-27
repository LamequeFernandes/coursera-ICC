larguraRetangulo = int(input("digite a largura: "))
alturaRetangulo = int(input("digite a altura: "))
i = 1
j = 1
while i <= alturaRetangulo:
   if i == 1 or i == alturaRetangulo:
      while j <= larguraRetangulo:
         print("#", end="")
         j += 1
   else:
      while j <= larguraRetangulo:
         if j == 1 or j == larguraRetangulo:
            print("#", end="")
         else:
            print(" ", end="")
         j += 1
   i += 1
   j = 1
   print()
