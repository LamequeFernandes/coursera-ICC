# N é o numero de peças iniciais e M o numero maximo de peças que é possivel retirar em uma rodada 

def computador_escolhe_jogada(n, m): #qts peças o computador deve tirar do tabuleiro para ganhar
   num = 1
   aux = m+1
   while num < m and num <= n:
      if num == n:
         return n
      if num % aux == 0:
         return num
      num += 1
   return m

def usuario_escolhe_jogada(n, m): #validar se a jogada é validade, caso n seja pedir para o mesmo fazer uma diferente
   num = int(input("\nQuantas peças você vai tirar? "))
   while True:
      if num > m or num > n or num < 1:
         print("\nOops! Jogada Inválida! Tente de novo.")
         num = int(input("\nQuantas peças você vai tirar? "))
      else:
         return num

def partida():
   n = int(input("Quantas peças? "))
   m = int(input("Limite de peças por jogada? "))
   aux = m+1
   
   if n % aux == 0:
      print("\nVocê começa!")
      while n > 0:
         u = usuario_escolhe_jogada(n, m)
         print("\nVocê tirou", u, "peça(s).")
         n = n - u
         if n <1:
            print("Fim de Jogo! Você ganhou")
            break
         print("Agora restam", n, "peças no tabuleiro.")

         c = computador_escolhe_jogada(n, m)
         print("\nO computador tirou", c, "peça(s).")
         n = n - c
         if n < 1:
            print("Fim de Jogo! O computador ganhou!")
            break
         print("Agora restam", n, "peças no tabuleiro.")
   else:
      print("\nComputador começa!")
      while n > 0:
         c = computador_escolhe_jogada(n, m)
         print("\nO computador tirou", c, "peça(s).")
         n = n - c
         if n < 1:
            print("Fim de Jogo! O computador ganhou!")
            break
         print("Agora restam", n, "peças no tabuleiro.")
      
         u = usuario_escolhe_jogada(n, m)
         print("\nVocê tirou", u, "peça(s).")
         n = n - u
         if n < 1:
            print("Fim de Jogo! Você ganhou")
            break
         print("Agora restam", n, "peças no tabuleiro.")

def main():
   print("Bem-vindo ao jogo do NIM! Escolha:\n")
   print("1 - para jogar uma partida isolada")
   escolha = int(input("2 - para jogar um coampeonato "))
   if escolha == 1:
      print("\nVocê escolheu uma partida")
      partida()
   elif escolha == 2:
      print("\nVocê escolheu um campeonato!")
      rodada = 1
      while rodada < 4:
         print("\n**** Rodada", rodada,"****\n")
         partida()
         rodada+=1

      print("\n**** Final do campeonato! ****")
      print("\nPlacar: Você 0 X 3 Computador")

main()
