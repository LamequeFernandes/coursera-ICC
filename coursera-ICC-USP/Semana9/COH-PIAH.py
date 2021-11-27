import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

# Traços linguísticos
def tamanhoMedioPalavras(texto):
   i = 0
   somaCaracteres = 0
   palavras = separa_palavras(texto)
   qtdPalavras = len(separa_palavras(texto))
   while i < qtdPalavras:
      somaCaracteres += len(palavras[i])
      i += 1
   return somaCaracteres / qtdPalavras

def typeToke(texto):
   palavras = separa_palavras(texto)
   palavrasDiferentes = n_palavras_diferentes(palavras)
   return len(palavrasDiferentes) / len(palavras)

def hapaxLegomana(texto): 
   palavras = separa_palavras(texto)
   palavrasUnicas = n_palavras_unicas(palavras)
   return len(palavrasUnicas) / len(palavras)

def tamanhoMedioSentencas(texto):
   i = 0
   somaCaracteres = 0
   sentencas = separa_sentencas(texto)
   while i < len(sentencas):
      somaCaracteres += len(sentencas[i])
      i += 1 
   return somaCaracteres / len(sentencas)

def complexidadeSenteça(texto):
   i = 0
   somaFrases = 0
   sentencas = separa_sentencas(texto)
   while i < len(sentencas):
      somaFrases += len(separa_frases(sentencas[i]))
      i += 1 
   return somaFrases / len(sentencas)

def tamanhoMedioFrase(texto):
   i = 0
   j = 0
   k = 0
   numeroFrases = 0
   caracteresFrases = 0
   sentencas = separa_sentencas(texto)
   while i < len(sentencas):
      frases = separa_frases(sentencas[i])
      numeroFrases += len(frases)
      while j < len(frases):
         palavras = separa_palavras(frases[j])
         while k < len(palavras):
            caracteresFrases += len(palavras[k])
            k += 1  
         j += 1
      i += 1
   return caracteresFrases / numeroFrases

def compara_assinatura(as_a, as_b):
   tracosLinguisticos = [tamanhoMedioPalavras(as_a), tamanhoMedioPalavras(as_b), typeToke(as_a), typeToke(as_b), hapaxLegomana(as_a), hapaxLegomana(as_b), tamanhoMedioSentencas(as_a), tamanhoMedioSentencas(as_b), complexidadeSenteça(as_a), complexidadeSenteça(as_b), tamanhoMedioFrase(as_a), tamanhoMedioFrase(as_b)]
   i = 0
   while i < 12:
       soma = 0
       somatorio = tracosLinguisticos[i] - tracosLinguisticos[i + 1]
       soma += abs(somatorio)      
       i += 2
   return soma / 6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass

