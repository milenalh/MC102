###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Tetris 2020
# Nome: Milena Lumi Hangai
# RA: 184654
###################################################

"""
Esta função recebe seis parâmetros:
- tabuleiro: a configuração inicial do tabuleiro;
- altura_tabuleiro: o valor da altura do tabuleiro;
- largura_tabuleiro: o valor da largura do tabuleiro;
- peca: a configuração da peça a ser inserida;
- altura_peca: o valor da altura da peça a ser inserida;
- largura_peca: o valor da largura da peça a ser inserida.

A função deve retornar a configuração atualizada do tabuleiro 
e o status do jogo ("O jogo deve continuar" ou "Fim de jogo")
"""

#funcao que descobre o primeiro ponto da peça que é ocupado (#)
def primeira_peca(peca, altura_peca, largura_peca):

    flag = True
    for k in range(altura_peca):
        for m in range(largura_peca):
            if peca[k][m]=="#":
                return k, m
    
    return k, m


#funcao que verifica se a peça cabe na posicao analisada
def verifica_peca(tabuleiro, altura_tabuleiro, largura_tabuleiro, lin_tabuleiro, col_tabuleiro, peca, lin_ocupada,
    col_ocupada, altura_peca, largura_peca):
    i = 0
    flag = True

    while (i + lin_ocupada) < altura_peca and i+lin_tabuleiro < altura_tabuleiro:
        j = -col_ocupada
        while (j + col_ocupada) < largura_peca and j+col_tabuleiro < largura_tabuleiro:
            if peca[i+lin_ocupada][j+col_ocupada] == "#" and tabuleiro[i+lin_tabuleiro][j+col_tabuleiro] != ".":
                flag = False
            j+=1

        i += 1
    
    return flag


def verifica_jogo(tabuleiro, altura_tabuleiro, largura_tabuleiro,
                  peca, altura_peca, largura_peca):
    flag = False

    lin_ocupada, col_ocupada = primeira_peca(peca, altura_peca, largura_peca)
    for i in range(altura_tabuleiro):
        for j in range(largura_tabuleiro):
            if tabuleiro[i][j]==".":
                flag = verifica_peca(tabuleiro, altura_tabuleiro, largura_tabuleiro, i, j, peca, lin_ocupada, col_ocupada, altura_peca, largura_peca)
                if flag == True:
                    return muda_tabuleiro(tabuleiro, altura_tabuleiro, largura_tabuleiro, i, j, peca, lin_ocupada, col_ocupada, altura_peca, largura_peca)
    fim = "Fim de jogo"
    return tabuleiro, fim


def muda_tabuleiro(tabuleiro, altura_tabuleiro, largura_tabuleiro, lin_tabuleiro, col_tabuleiro, peca, lin_ocupada,
    col_ocupada, altura_peca, largura_peca):
    i = 0

    while (i + lin_ocupada) < altura_peca and i+lin_tabuleiro < altura_tabuleiro:
        j = -col_ocupada
        while (j + col_ocupada) < largura_peca and j+col_tabuleiro < largura_tabuleiro:
            if peca[i+lin_ocupada][j+col_ocupada] == "#" and tabuleiro[i+lin_tabuleiro][j+col_tabuleiro] == ".":
                tabuleiro[i+lin_tabuleiro][j+col_tabuleiro] = "#"
            j += 1

        i += 1
    
    return tabuleiro, "O jogo deve continuar"



# Leitura de dados
 
altura_tabuleiro, largura_tabuleiro = [int(x) for x in input().split()]
tabuleiro = []

for k in range(altura_tabuleiro):
    l_tabuleiro = str(input())
    tabuleiro.append(list(l_tabuleiro))

# Leitura do tabuleiro

# Dica: use a função list() para transformar uma srting numa lista de caracteres

altura_peca, largura_peca = [int(x) for x in input().split()]
peca = []
for k in range(altura_peca):
    l_peca = str(input())
    peca.append(list(l_peca))
    


# Leitura da peça

# Dica: use a função list() para transformar uma srting numa lista de caracteres

# Impressão da configuração atualizada do tabuleiro

tabuleiro, status_do_jogo = verifica_jogo(tabuleiro, altura_tabuleiro, largura_tabuleiro,
                                          peca, altura_peca, largura_peca)

for linha in tabuleiro:
	print("".join(linha))

# Impressão do status do jogo
print(status_do_jogo)