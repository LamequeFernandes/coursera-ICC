larguraRetangulo = int(input("digite a largura: "))
alturaRetangulo = int(input("digite a altura: "))
i = 1
j = 1
while i <= alturaRetangulo:
   while j <= larguraRetangulo:
      print("#", end="")
      j += 1
   i += 1
   j = 1
   print()
