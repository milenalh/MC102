###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Nota de MC102
# Nome: Milena Lumi  Hangai
# RA: 184654
###################################################

# Leitura de dados
n = int(input()) #quantidade de labs
notas = [float(input()) for i in range(n)] #notas obtidas em cada lab (n entradas)
pesos = [int(input()) for j in range(n)]
# Cálculo da média ponderada dos laboratórios
##preciso pegar cada elemento da lista notas e multiplicar pelo correspondente da lista pesos, depois somar todos
P = []
for i in range (len(notas)):
    P.append(notas[i] * pesos[i])

nf = sum(P)/sum(pesos)

# Verificação da situação do aluno
if nf >= 5: # Caso o aluno tenha sido aprovado por nota
    print("Media laboratorios:", format(nf, ".1f").replace(".", ","))
    print("Situacao: Aprovado por nota")
    print("Nota final:", format(nf, ".1f").replace(".", ","))

if nf < 2.5: # Caso o aluno tenha sido reprovado por nota
    print("Media laboratorios:", format(nf, ".1f").replace(".", ","))
    print("Situacao: Reprovado por nota")
    print("Nota final:", format(nf, ".1f").replace(".", ","))

# Cálculo da nota do exame, caso o aluno tenha ido para o exame
if 2.5 <= nf < 5:
    m = int(input())
    lista = []
    for i in range(m):
        labs_exame = int(input())
        lista.append(labs_exame)
    pesos_exame = []
    for i in range(m):
        p = lista[i]
        pesos_exame.append(pesos[p-1])
    notas_exame = [float(input()) for l in range(m)]
    soma_exame = []
    for k in range(m):
        soma_exame.append(pesos_exame[k] * notas_exame[k])
        contaf = sum(soma_exame)/sum(pesos_exame)
        nf_exame = (nf + contaf)/2
    if nf_exame >= 5: # Caso o aluno tenha sido aprovado no exame
        print("Media laboratorios:", format(nf, ".1f").replace(".", ","))
        print("Situacao: Aprovado no exame")
        print("Nota final: 5,0")
    if nf_exame < 5: # Caso o aluno tenha sido reprovado no exame
        print("Media laboratorios:", format(nf, ".1f").replace(".", ","))
        print("Situacao: Reprovado no exame")
        print("Nota final:", format(nf_exame, ".1f").replace(".", ","))