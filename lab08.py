###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Ocorrência de Palavras
# Nome: Milena Lumi Hangai
# RA: 184654
###################################################
import re
# Leitura de dados
l = int(input()) #numero de linhas do texto

# Processamento do texto
lines = '' #string vazia para preencher com o texto
for i in range(l): #for para ler as linhas indicadas por l
    lines+=input()+' ' #adicionando tudo na string lines
lines = re.sub(r'[.,:;!?]',' ', lines)
lines = lines.lower()
n = int(input()) #numero de palavras a serem procuradas
x = [] #lista vazia colocar as palavras a serem procuradas
q = 0 
while q <= (n-1):
  w = str(input())
  x.append(w)
  q = q + 1
e = lines.split() #transforma lines em uma lista
for procurada_original in x:
  procurada = procurada_original.lower()
  ocorrencia = 0
  similar = 0
  for palavra in e:
    if palavra == procurada:
      ocorrencia = ocorrencia + 1
    elif procurada in palavra:
      similar = similar + 1

  # Saída de dados
  print("Palavra buscada:", procurada_original)
  print("Ocorrencia:", ocorrencia)
  print("Palavras similares:", similar)