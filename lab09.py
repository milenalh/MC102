#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Copa do Mundo de Futebol
# Nome: Milena Lumi Hangai
# RA: 184654
#####################################################

# Leitura da lista de seleções
selecoes = []
dic = {}
for i in range(4):
  selecao = input()
  selecoes.append(selecao)
  dic[selecao] = {"partidas": 0,
                  "vitorias": 0,
                  "derrotas": 0,
                  "penaltis": 0,
                  "normal": 0,
                  "marcados": 0,
                  "sofridos": 0}

# Leitura das partidas e processamento dos dados
for k in range(4):
    w = str(input())
    w = w.replace("(","")
    w = w.replace(")","")
    L = w.split()
    if len(L) == 5: #jogo normal
        dic[L[0]]["marcados"] = int(dic[L[0]]["marcados"]) + int(L[1]) 
        dic[L[4]]["marcados"] = int(dic[L[4]]["marcados"]) + int(L[3])
        dic[L[0]]["sofridos"] = int(dic[L[0]]["sofridos"]) + int(L[3])
        dic[L[4]]["sofridos"] = int(dic[L[4]]["sofridos"]) + int(L[1])

        dic[L[0]]["partidas"] = int(dic[L[0]]["partidas"]) + 1
        dic[L[4]]["partidas"] = int(dic[L[4]]["partidas"]) + 1

        dic[L[0]]["normal"] = dic[L[0]]["normal"] + 1
        dic[L[4]]["normal"] = dic[L[4]]["normal"] + 1

        if int(L[1]) > int(L[3]):  #se país 1 ganhou do país 2
            dic[L[0]]["vitorias"] = dic[L[0]]["vitorias"] + 1
            dic[L[4]]["derrotas"] = dic[L[4]]["derrotas"] + 1
        
        if int(L[1]) < int(L[3]): #se o país 1 perdeu do país 2
            dic[L[0]]["derrotas"] = dic[L[0]]["derrotas"] + 1
            dic[L[4]]["vitorias"] = dic[L[4]]["vitorias"] + 1

    else: #pênalti
        dic[L[0]]["partidas"] = int(dic[L[0]]["partidas"]) + 1
        dic[L[7]]["partidas"] = int(dic[L[7]]["partidas"]) + 1
        dic[L[0]]["penaltis"] = dic[L[0]]["penaltis"] + 1
        dic[L[7]]["penaltis"] = dic[L[7]]["penaltis"] + 1
        
        if int(L[4]) > int(L[6]):  #se país 1 ganhou do país 2 nos pênaltis
            dic[L[0]]["vitorias"] = dic[L[0]]["vitorias"] + 1
            dic[L[7]]["derrotas"] = dic[L[7]]["derrotas"] + 1
            dic[L[0]]["marcados"] = int(dic[L[0]]["marcados"]) + int(L[1])
            dic[L[7]]["marcados"] = int(dic[L[7]]["marcados"]) + int(L[3])
            dic[L[0]]["sofridos"] = int(dic[L[0]]["sofridos"]) + int(L[3])
            dic[L[7]]["sofridos"] = int(dic[L[7]]["sofridos"]) + int(L[1])
        
        if int(L[4]) < int(L[6]):  #se país 1 perdeu do país 2 nos pênaltis
            dic[L[0]]["derrotas"] = dic[L[0]]["derrotas"] + 1
            dic[L[7]]["vitorias"] = dic[L[7]]["vitorias"] + 1
            dic[L[0]]["marcados"] = int(dic[L[0]]["marcados"]) + int(L[1])
            dic[L[7]]["marcados"] = int(dic[L[7]]["marcados"]) + int(L[3])
            dic[L[0]]["sofridos"] = int(dic[L[0]]["sofridos"]) + int(L[3])
            dic[L[7]]["sofridos"] = int(dic[L[7]]["sofridos"]) + int(L[1])
    
for q in dic:
    if dic[q]["derrotas"] == 0:
        campeao = q


# Saída de dados

for selecao in selecoes:
  print("-" * 50)
  print("Pais:", selecao)
  print("Partidas:", dic[selecao]["partidas"])
  print("Partidas decididas em tempo normal de jogo:", dic[selecao]["normal"])
  print("Partidas decicidas nos penaltis:", dic[selecao]["penaltis"])
  print("Vitorias:", dic[selecao]["vitorias"])
  print("Derrotas:", dic[selecao]["derrotas"])
  print("Gols marcados:", dic[selecao]["marcados"])
  print("Gols sofridos:", dic[selecao]["sofridos"])

print("-" * 50)
print("Pais campeao:", campeao)
print("-" * 50)