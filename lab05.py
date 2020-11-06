###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Números da Mega-Sena
# Nome: Milena Lumi Hangai
# RA: 184654
###################################################

# Leitura de dados
x1 = int(input())
x3 = int(input())
x4 = int(input())
x6 = int(input())

# Impressão dos quatro números fornecidos como entrada

print("Primeiro:", "{:02}".format(x1))
print("Terceiro:", "{:02}".format(x3))
print("Quarto:", "{:02}".format(x4))
print("Sexto:", "{:02}".format(x6))


# Processamento e impressão da lista de possíveis apostas

print("Lista de apostas:")
m = (x1 + 1)
n = (x4 + 1)
for x2 in range(m, x3, 2): 
    for x5 in range(n, x6, 2):
        resto1 = (x1 + x2 + x3 + x4 + x5 + x6)%7 # se for divisível por 7, o resto vai ser igual a 0
        resto2 = (x1 + x2 + x3 + x4 + x5 + x6)%13 # se for divisível por 13, o resto vai ser igual a 0
        if resto1 and resto2 != 0:
            print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(x1, x2, x3, x4, x5, x6))