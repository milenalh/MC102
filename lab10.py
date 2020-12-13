###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça-Palavras 2.0
# Nome: Milena Lumi Hangai
# RA: 184654
###################################################

# libera nois IC pelo amor de deus nao aguento mais
def horizontal(matriz, linha, coluna, palavra):
    i = 0
    flag = True #se a palavra for diferente da matriz, então flag falso
    #loop para comparar cada letra da palavra com a matriz
    for letra in palavra:
        if letra != matriz[linha][coluna + i].lower() and matriz[linha][coluna + i] != "*":
            flag = False
        i += 1
    i = 0
    # loop para jogar para letras maiúsculas
    if flag:
        for letra in palavra:
            if matriz[linha][coluna + i] != "*":
                matriz[linha][coluna + i] = matriz[linha][coluna + i].upper()
            i += 1
    return flag


def vertical(matriz, linha, coluna, palavra):
    i = 0
    flag = True
    for letra in palavra:
        if letra != matriz[linha + i][coluna].lower() and matriz[linha + i][coluna] != "*":
            flag = False
        i += 1
    i = 0
    if flag:
        for letra in palavra:
            if matriz[linha + i][coluna] != "*":
                matriz[linha + i][coluna] = matriz[linha + i][coluna].upper()
            i += 1
    return flag


def diagonal1(matriz, linha, coluna, palavra):
    i = 0
    flag = True
    for letra in palavra:
        if letra != matriz[linha + i][coluna + i].lower() and matriz[linha + i][coluna + i] != "*":
            flag = False
        i += 1
    i = 0
    if flag:
        for letra in palavra:
            if matriz[linha + i][coluna + i] != "*":
                matriz[linha + i][coluna + i] = matriz[linha + i][coluna + i].upper()
            i += 1
    return flag


def diagonal2(matriz, linha, coluna, palavra):
    i = 0
    flag = True
    for letra in palavra:
        if letra != matriz[linha - i][coluna + i].lower() and matriz[linha - i][coluna + i] != "*":
            flag = False
        i += 1
    i = 0
    if flag:
        for letra in palavra:
            if matriz[linha - i][coluna + i] != "*":
                matriz[linha - i][coluna + i] = matriz[linha - i][coluna + i].upper()
            i += 1
    return flag

# Leitura da matriz
matriz = []
linha = input()
largura = len(linha.split(" "))
comprimento = 0
while not(linha.isdigit()):
    comprimento += 1
    matriz.append(linha.split(" "))
    linha = input()


# Leitura e processamento das palavras
n = int(linha)
j = 0
ocorrencias = 0
lista_oc = [] #lista de ocorrencias de cada palavra
palavras = [] #lista de palavras
while n > j:
    palavra = str(input())
    j += 1
    lin = 0
    ocorrencias = 0
    palavras.append(palavra)
    # loop para ler a matriz
    while lin < comprimento:
        col = 0
        while col < largura:
            # verifica a primeira letra da palavra com a matriz para realizar buscas
            if palavra[0] == matriz[lin][col].lower() or matriz[lin][col] == "*":
                # condicao para busca horizontal, não pode ser maior que tamanho da matriz
                if (col + len(palavra)) <= largura:
                    ocorrencia_h = horizontal(matriz, lin, col, palavra)
                    if ocorrencia_h:
                        ocorrencias += 1
                # busca vertical
                if (lin + len(palavra)) <= comprimento:
                    ocorrencia_v = vertical(matriz, lin, col, palavra)
                    if ocorrencia_v:
                        ocorrencias += 1
                # busca diagonal1
                if (lin + len(palavra)) <= comprimento and (col + len(palavra)) <= largura:
                    ocorrencia_d1 = diagonal1(matriz, lin, col, palavra)
                    if ocorrencia_d1:
                        ocorrencias += 1
                # busca diagonal2
                if (lin - len(palavra)) >= -1 and (col +  len(palavra)) <= largura:
                    ocorrencia_d2 = diagonal2(matriz, lin, col, palavra)
                    if ocorrencia_d2:
                        ocorrencias += 1
            col += 1
        lin += 1
    lista_oc.append(ocorrencias)
    
print("-" * 40)
print("Lista de Palavras")
print("-" * 40) 

i = 0
while i<len(lista_oc):
    print("Palavra:", palavras[i])
    print("Ocorrencias:", lista_oc[i])
    print("-" * 40)
    i+=1

# Impressão da matriz
for linha in matriz:
  print(" ".join(linha))